from flask import Flask,render_template,url_for,request
from ableist_language_detector import detector
from termcolor import colored
from functools import reduce
from itertools import chain

## Things to do in back-end:
## - Maintain the formatting
## - Highlight the words

app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = message
        ableist_language = detector.find_ableist_language(data)
        alternatives = {}
        examples = {}
        for i, ableist_term in enumerate(ableist_language):
            term = str(ableist_term)
            alternatives[term] = ableist_term.data.alternative_verbs
            examples[term] = str(ableist_term.data.example)
            # print(
            #     f"Match #{i+1}\n"
            #     f"PHRASE: {ableist_term} | LEMMA: {ableist_term.lemma} | "
            #     f"POSITION: {ableist_term.start}:{ableist_term.end} | "
            #     f"ALTERNATIVES: {ableist_term.data.alternative_verbs} | "
            #     f"EXAMPLE: {ableist_term.data.example}\n"
            # )

        ## Finding number of ableist words
        length = len(ableist_language)

        ls = [word.text for word in ableist_language]

        for word in ls:
            data = data.replace(word, '<mark style="background: #00ced1!important">%s</mark>' % word)
    
    return render_template('result.html',prediction = ableist_language, length=length, ls=ls, result=data, alternatives=alternatives, examples=examples)

if __name__ == '__main__':
	app.run(debug=True)
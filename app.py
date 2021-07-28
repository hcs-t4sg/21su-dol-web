from flask import Flask,render_template,url_for,request
from termcolor import colored
from functools import reduce
from itertools import chain
import ableist_language_module.ableist_language_detector.detector as detector
from highlight import highlight, AbleistLanguage

app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.form['message']
        # retreive spacy output
        ableist_language = detector.find_ableist_language(data)

        # format and process spacy output
        ableist_terms = []
        alternatives = {}
        examples = {}
        term_id = {}
        for i, ableist_term in enumerate(ableist_language):
            term = str(ableist_term)
            ableist_terms.append(AbleistLanguage(
                text=term, 
                start=ableist_term.start, 
                end=ableist_term.end, 
            ))
            term_id[term] = term.replace(" ", "")
            alternatives[term] = ableist_term.data.alternative_verbs
            examples[term] = str(ableist_term.data.example)
        

        # convert list of dataclasses to sorted list of (start, end) indices
        sorted_idx_list = sorted([(data.start, data.end) for data in ableist_language])

        # mark each ableist term in input
        result = highlight(data, sorted_idx_list)

        # Finding number of ableist words
        length = len(ableist_language)

        # ls = [word.text for word in ableist_language]

        # for word in ls:
        #     data = data.replace(word, '<mark style="background: #00ced1!important">%s</mark>' % word)

    return render_template('result.html',prediction = ableist_language, length=length, result=result, alternatives=alternatives, examples=examples, term_id=term_id)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

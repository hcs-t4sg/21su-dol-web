from flask import Flask,render_template,url_for,request
from ability_skills_decoder import decoder
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

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = message
        ableist_language = decoder.find_ableist_language(data)

        ## Finding number of ableist words
        length = len(ableist_language)

        ls = [word.text for word in ableist_language]

        for word in ls:
            data = data.replace(word, '<mark style="background: #00ced1!important">%s</mark>' % word)

    
    return render_template('result.html',prediction = ableist_language, length=length, ls=ls, data=data, result=data)

if __name__ == '__main__':
	app.run(debug=True)
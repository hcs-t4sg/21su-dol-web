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

        newlist = [word for line in ls for word in line.split()]

        ## highlighting words python function
        ## def analyze():
            ## print(reduce(lambda t, x: t.replace(*x), chain([data.lower()], ((t, colored(t,'white','on_red')) for t in ls))))
        
        boldened = " ".join(["<mark>{}</mark>".format(word) if word in newlist else word for word in data.split()])

        
        def highlight(paragraph):
            for word in ls:
                if word in paragraph:
                    paragraph.replace(word, '<b>{}</b>'.format(word))
                else:
                    return paragraph
        
        s2=highlight(data)

    
    return render_template('result.html',prediction = ableist_language, length=length, ls=ls, newlist=newlist, data=data, result=boldened, s2=s2)

if __name__ == '__main__':
	app.run(debug=True)
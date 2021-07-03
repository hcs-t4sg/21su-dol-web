from flask import Flask,render_template,url_for,request
from ability_skills_decoder import decoder
import spacy

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
        length = len(ableist_language)


    return render_template('result.html',prediction = ableist_language, length=length)

if __name__ == '__main__':
	app.run(debug=True)
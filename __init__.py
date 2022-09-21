from flask import Flask, render_template
from googletrans import Translator 
import requests

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        translator = Translator()
        r = requests.get('https://api.adviceslip.com/advice')
        data = r.json()
        advice = data.get('slip')['advice']
        traduzido = translator.translate(advice, dest='pt').text
        id = data.get('slip')['id']

        return render_template('advice_slip.html', ad = traduzido, id =id)
    
    return app
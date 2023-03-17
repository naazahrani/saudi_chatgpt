from flask import Flask, render_template, request, Markup
import http.client
from api import pipeline

app = Flask(__name__)

conn = http.client.HTTPSConnection("experimental.willow.vectara.io")
api_key = "zqt_luPhYvx4vwvktQg1xkgrbpeCbqv1LGak1QfrNQ"
customer_id = "2531516770"


@app.route('/',  methods=['GET', 'POST'])
def index():
    res = ""
    if request.method == 'POST':
        print(request.form['button'])

        
        try:
            res = pipeline()
            if res["status"] == 200:
                message = Markup(res["text"])
                return render_template('home.html', message=message)
                
        except Exception as e:
            print("backend error: ", str(e))
    return render_template('home.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['name']
#     age = request.form['age']
#     return f'Hello {name}, you are {age} years old.'

if __name__ == '__main__':
    app.run(debug=True)

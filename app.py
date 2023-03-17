from flask import Flask, render_template, request, Markup
import http.client

app = Flask(__name__)

conn = http.client.HTTPSConnection("experimental.willow.vectara.io")
api_key = "zqt_luPhYvx4vwvktQg1xkgrbpeCbqv1LGak1QfrNQ"
customer_id = "2531516770"


@app.route('/',  methods=['GET', 'POST'])
def index():
<<<<<<< HEAD
    res = ""
    if request.method == 'POST':
        print(request.form['button'])

        
        try:
            res = "here"
        except Exception as e:
            print("backend error: ", str(e))
        message = Markup(res)
        return render_template('home.html', message=message)
=======
>>>>>>> 5dcf41d9275ff33d347773bd36600b0927f43b25
    return render_template('home.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['name']
#     age = request.form['age']
#     return f'Hello {name}, you are {age} years old.'

if __name__ == '__main__':
    app.run(debug=True)

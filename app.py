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
                cases_appoinments = [['','24 ساعة','طوارئ مستشفى الملك سعود الجامعي','https://goo.gl/maps/fYco4iFqLbRrEeTi9'],
                    [['د.عبدالله', ' الاحد 19/3/2023  9:30 صباحا ', 'مجمع إرادة( الأمل) للصحة النفسية بالرياض', 'https://goo.gl/maps/pn36qXeioMzLEoK4A'], ['د.منال', ' الاثنين 20/3/2023  3 عصرا ', 'مجمع إرادة( الأمل) للصحة النفسية بالرياض', 'https://goo.gl/maps/pn36qXeioMzLEoK4A']]
                ]
                if res['id'] == 1:
                    return render_template('home.html', message=message, res=res)
                elif res['id'] == 2:
                    return render_template('home.html', message=message, res=cases_appoinments[0])
                elif res['id'] == 3:
                    return render_template('home.html', message=message, res=cases_appoinments[1])
                else:
                    return render_template('home.html', message=message, res=res)

                # return render_template('home.html', message=message, results=results)
                
        except Exception as e:
            print("backend error: ", str(e))
    return render_template('home.html', res=res)

# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form['name']
#     age = request.form['age']
#     return f'Hello {name}, you are {age} years old.'

if __name__ == '__main__':
    app.run(debug=True)
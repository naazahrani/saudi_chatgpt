import http.client
import json
from flask import Flask

app = Flask(__name__)
conn = http.client.HTTPSConnection("experimental.willow.vectara.io")

api_key = "zqt_luPhYvx4vwvktQg1xkgrbpeCbqv1LGak1QfrNQ"
customer_id = "2531516770"

def chatgpt(prompt, api_key, customer_id):
  payload = json.dumps({
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": prompt 
    }
    ]
  })
  headers = {
    'Content-Type': 'application/json',
    'customer-id': customer_id,
    'x-api-key': api_key
  }
  conn.request("POST", "/v1/chat/completions", payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))

  ans = json.loads(data)
  return ans["choices"][0]["message"]["content"]


while True:
  prompt = input()
  print(chatgpt(prompt, api_key, customer_id))



# @app.route('/', methods=['POST'])
# def index():
#   prompt = 'hi'
#   return json.loads(chatgpt(prompt, api_key, customer_id))
# app.run()
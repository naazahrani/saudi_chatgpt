import http.client
import json
from utils import classify_intent_extract_entities_parser
from audio import record_audio

conn = http.client.HTTPSConnection("experimental.willow.vectara.io")
customer_id = "2702570306"
api_key = "zqt_oRXzQgfyo2zWb80GcaNoaLrbSU58480yIJSBrg"

def classify_intent_extract_entities(message):
  payload = json.dumps({
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": f"Classify the intent of the following user's message and extract the entities:\
        '{message}'\
          Intent: [Write answer here]\
          Entities: [Write answer/s here]\
            If something is unknown or unclear write None in the answer" 
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


def chatgpt(prompt):
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


record_audio(save_audio=True)
# print(classify_intent_extract_entities(" i want to book an appointment"))
# classify_intent_extract_entities_parser(classify_intent_extract_entities(" i want to book an appointment"))
import http.client
import requests
import json
from utils import classify_intent_extract_entities_parser
from audio import record_audio, generate_audio
import arabic_reshaper
from bidi.algorithm import get_display

conn = http.client.HTTPSConnection("experimental.willow.vectara.io")
api_key = "zqt_luPhYvx4vwvktQg1xkgrbpeCbqv1LGak1QfrNQ"
customer_id = "2531516770"

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

def whisper_api(filename):
  url = "https://experimental.willow.vectara.io/v1/audio/transcriptions"

  print(filename)
  payload={'model': 'whisper-1'}
  files=[
    ('file',(f'{filename}.wav',open(f'static/audios/{filename}.wav','rb'),'application/octet-stream'))
  ]
  headers = {
    'customer-id': customer_id,
    'x-api-key': api_key
  }

  response = requests.request("POST", url, headers=headers, data=payload, files=files)

  return response.text




# return a response upon call start

def pipeline():
  latest_audio='latest_audio'
  record_audio(audio_name="latest_audio", save_audio=True)
  print("to whisper")
  text = whisper_api(latest_audio)
  print("to chatgpt")
  text = chatgpt(text)
  # text = arabic_reshaper.reshape(text)
  # text = get_display(text) 
  res = generate_audio(text, latest_audio)
  return res
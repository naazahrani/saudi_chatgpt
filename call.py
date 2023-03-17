import os
from twilio.rest import Client
from twilio.twiml.voice_response import Play, VoiceResponse
import flask

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC486de4f3c535411677aca4e48da60677'
auth_token = '1b46fef5ff38a86110854940bbf931eb'



from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
app = Flask(__name__)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()
    resp.play(url="file:///home/abdulaziz/Development/saudi_chatgpt/tts_output.wav")
    return str(resp)

if __name__ == "__main__":
    app.run()


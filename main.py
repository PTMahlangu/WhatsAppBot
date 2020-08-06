# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import aiml
import os

# Create the kernel and learn AIML files
kernel = aiml.Kernel()

for filename in os.listdir("brain"):
	if filename.endswith(".aiml"):
		kernel.learn("brain/" + filename)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'welcome to the whatsappbot'

@app.route("/sms", methods=['POST'])
def sms_reply():

    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')
    reply = kernel.respond(msg)

    # Create reply
    resp = MessagingResponse()

    if reply:
        resp.message(reply)
    else:
        resp.message("Currently no match found for input: *" + msg + "* ,Make sure the word is spelled correctly.")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

print("Hello I am here")
@app.route("/")

def hello():
    return{
        "Result": "Successful First Route!"
    }

@app.route("/webhook", methods = ['POST'])
def webhook_fun():
    ##msg = request.form.get('body')
    message = request.form["message"]
    resp = MessagingResponse()
    resp.message("You said: {}".format(message))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True) 
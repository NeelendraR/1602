# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
app = twilio(__name__)
@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a receipt SMS."""
    # Start our response
    resp = MessagingResponse()
# Add a message
    resp.message("Thank you for your response! We are confirming your message.")
return str(resp)
if __name__ == "__main__":
    app.run(debug=True)

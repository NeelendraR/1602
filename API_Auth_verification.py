
#Auth ID = MAODUZYTQ0Y2FMYJBLOW
#Auth token : ODgyYmQxYTQ2N2FkNDFiZTNhZWY4MDAwYWY4NzY0

import requests

auth_token =  'MAODUZYTQ0Y2FMYJBLOW'

# Download the Python helper library from twilio.com/docs/python/install
from abc.rest import Client

# Your Account Sid and Auth Token from abc.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = Client(account_sid, auth_token)

numbers = client.available_phone_numbers("US") \
                .local \
                .list(area_code="510")

# Purchase the phone number
number = client.incoming_phone_numbers \
               .create(phone_number=numbers[0].phone_number)

print(number.sid)

# Your Account Sid and Auth Token from abc.com/user/account
client = Client(account_sid, auth_token)

country = client.pricing \
                .phone_numbers \
                .countries("US") \
                .fetch()

for p in country.phone_number_prices:
    print("{} {}".format(p['type'], p['current_price']))


message = client.messages.create(
                              from_='+15017122661',
                              body='body',
                              to='+15558675310'
                          )

print(message.sid)

client = Client(account_sid, auth_token)

country = client.pricing \
                .messaging \
                .countries("EE") \
                .fetch()



C:\Users\ranjan3\Desktop\Automation_learning\TestCase\API_Auth_verification.py
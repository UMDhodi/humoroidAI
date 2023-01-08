from twilio.rest import Client

print("Type your message")
msz = input("")

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid ='ACc306752871b6b08e7a01f003f601f876'
auth_token  ='f41f153b4018ee52dfe4d9bc34636612'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body= msz,
         from_= '+18475651650',
         to= '+919528499374'
     )

print(message.sid)

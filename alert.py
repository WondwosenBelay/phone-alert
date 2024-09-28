from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'
recipient_phone_number = 'recipient_phone_number'

# Create Twilio client
client = Client(account_sid, auth_token)

# Send SMS
message = client.messages.create(
    body="Alert: This is a phone alert signal!",
    from_=twilio_phone_number,
    to=recipient_phone_number
)

print(f"Alert sent! Message SID: {message.sid}")

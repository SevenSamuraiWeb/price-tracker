from twilio.rest import Client
import toml

def send_sms(message, to_number=None):
    secrets = toml.load("secrets.toml")
    client = Client(secrets["twilio_sid"], secrets["twilio_token"])
    to_number = to_number or secrets["user_phone"]
    client.messages.create(
        body=message,
        from_=secrets["twilio_number"],
        to=to_number
    )

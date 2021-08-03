import os
import string
import random
from flask_mail import Message


# Generate random string
def random_str_generator(size=15, chars=string.ascii_letters + string.digits):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))


# Send an email
def send_message(message, mail):

    msg = Message(
        subject=message.get("subject"),
        sender=message.get("email"),
        recipients=[os.environ["DUMMY_MAIL_USERNAME"]],
        body=message.get("message")
    )
    mail.send(msg)



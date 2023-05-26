# utils.py

from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_password_reset_email(user, reset_link):
    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=user.email,
        subject='Password Reset',
        plain_text_content=f'Click the following link to reset your password: {reset_link}',
    )
    try:
        sendgrid_client = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        sendgrid_client.send(message)
    except Exception as e:
        # Handle any errors that occur during sending the email
        print(str(e))

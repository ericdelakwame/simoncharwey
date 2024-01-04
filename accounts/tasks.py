from celery import shared_task
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from django.conf import settings

from django.contrib.auth import get_user_model
sendgrid_key = settings.SENDGRID_API_KEY
User = get_user_model()


@shared_task
def welcome_user(user_id):
    user = User.objects.get(id=user_id)
    receipient = user.email
    mail_subject = 'Welcome. I am Simon Charwey'
    body = 'Dear {}, \n\n Your registration was successful. Please sign in with your credentials and discover another world of design. Thank You'.format(
        user.first_name)
    message = Mail(
        from_email='creativecharwey@gmail.com', to_emails=receipient,
        subject=mail_subject,
        html_content=body,

    )
    message.dynamic_template_data = {

        'first_name': '{}'.format(user.first_name),
    }
    message.template_id = 'd-2c030ee2524846238e992e1329d19df0'
    try:
        sg = SendGridAPIClient(api_key=sendgrid_key)
        sg.send(message)
    except Exception as e:
        print(e)



from django.core.mail import EmailMessage


class Util:
    @staticmethod
    def send_email(data):
        
        email = EmailMessage(subject=data['subject'], body=data['message'], to=data['to'])
        email.send()
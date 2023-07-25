from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError

def say_hello(request):
    try:
        mail_admins('subject', 'message', html_message='message')
    except BadHeaderError as b:
        print(b)

    return render(request, 'hello.html', {'name': 'Mosh'})

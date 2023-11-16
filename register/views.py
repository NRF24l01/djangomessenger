from django.http import HttpResponse
from django.shortcuts import render
import smtplib
from email.mime.text import MIMEText
import jinja2


def render_mail(auth_link, name):
    environment = jinja2.Environment()
    with open("register/templates/mail_request.html", "r", encoding="UTF-8") as f:
        template = environment.from_string(f.read())
        return template.render(name=name, link=auth_link)


def send_email_message(receiver_mail, title, name, auth_link):
    port = 465
    password = 'ZbiBdss8bDgU60xjhxfm'
    sender_mail = 'sendmail.messenger@mail.ru'
    smtp_server = 'smtp.mail.ru'
    text = render_mail(name=name, auth_link=auth_link)
    print("Jinja work sucsses")

    try:
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(sender_mail, password)
            msg = MIMEText(f'{text}', 'html')
            msg['Subject'] = title
            msg['From'] = sender_mail
            msg['To'] = receiver_mail
            server.sendmail(sender_mail, receiver_mail, msg.as_string())
        return True
    except Exception as e:
        print(e)
        return False


# Create your views here.
def register_sistem(request):
    print(request)
    name = request.GET.get("name", None)
    email = request.GET.get("email", None)
    pasw = request.GET.get("pass", None)

    if send_email_message(email, "Потверждение регистрации", name, ""):
        return HttpResponse(
            f"<h2>Отправлено письмо с потверждением верификации. Перейдите поссылке в письме. Ваша почта {email}</h2>")
    else:
        return HttpResponse(
            f"<h2>Не удалось отправить письмо. Ваша почта {email}</h2>")


def hello_world(request):
    return render(request, 'register.html')

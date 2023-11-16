import re
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
    password = 'edNYS7awi6Us2wDH13aB'
    sender_mail = 'sendmail.messenger@mail.ru'
    smtp_server = 'smtp.mail.ru'
    text = "hohoho"  # render_mail(name=name, auth_link=auth_link)
    print("Jinja work sucsses")

    try:
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(sender_mail, password)
            msg = MIMEText(f'{text}', 'html')
            msg['Subject'] = title
            msg['To'] = receiver_mail
            server.sendmail(sender_mail, receiver_mail, msg.as_string())
            print("sucses")
        return True
    except Exception as e:
        print(e)
        return False

def is_valid_email(email):
    # Регулярное выражение для проверки формата адреса
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Проверка формата адреса
    if re.match(pattern, email):
        return True
    else:
        return False

from django.http import HttpResponse
from django.shortcuts import render, redirect
from threading import Thread
from register.models import Users
from register.other_things import is_valid_email, send_email_message


# Create your views here.
def register_sistem(request):
    # print(request)
    name = request.GET.get("name", None)
    email = request.GET.get("email", None)
    pasw = request.GET.get("pass", None)
    pasw1 = request.GET.get("pass1", None)
    agree = request.GET.get("agree", False)
    if not agree:
        return redirect("/register/?err=Вы не приняли правила сервиса")

    if not is_valid_email(email):
        return redirect("/register/?err=Неверная почта")

    if not pasw == pasw1:
        return redirect("/register/?err=Пароли не совпадают")

    if len(Users.objects.filter(email=email)) > 0:
        return redirect("/register/?err=-1")
    else:
        user = Users(email=email, username=name, pasw=pasw, name=name, reg_link="", state="reg")
        user.save()
        email_sender = Thread(target=send_email_message, args=(email, "Потверждение регистрации в сodingmessengers", name, ""))
        email_sender.start()
        return HttpResponse(
            f"<h2>Вроде вам должно отправиться письмо на почту)</h2>")


def render_register(request):
    print(request.session.get("id", None))
    if request.session.get("id", None):
        return redirect("/messenger/chat")
    err = request.GET.get("err", None)
    return render(request, 'register.html', {"err": err})

def render_login(request):
    print(request.session.get("id", None))
    if request.session.get("id", None):
        return redirect("/messenger/chat")
    err = request.GET.get("err", None)
    return render(request, 'login.html', {"err": err})

def login_user(request):
    username = request.GET.get("lg", None)
    pasw = request.GET.get("pass", None)

    if len(Users.objects.filter(email=username, pasw=pasw)) > 0:
        id = Users.objects.get(email=username, pasw=pasw).id
        request.session["user"] = username
        request.session["id"] = id
        request.session["pass"] = pasw
        return redirect("/messenger/chat")
    elif len(Users.objects.filter(username=username, pasw=pasw)) > 0:
        id = Users.objects.get(username=username, pasw=pasw).id
        request.session["id"] = id
        request.session["user"] = username
        request.session["pass"] = pasw
        return redirect("/messenger/chat")
    else:
        return redirect("/register/login/?err=Пользователь не обнаружен")

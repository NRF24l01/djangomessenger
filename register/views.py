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
    pasw = request.GET.get("pas1", None)
    if not is_valid_email(email):
        return redirect("/register/?err=Неверная почта")

    if not pasw = (email):
        return redirect("/register/?err=Неверная почта")

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
    err = request.GET.get("err", None)
    return render(request, 'register.html', {"err": err})

def render_login(request):
    err = request.GET.get("err", None)
    return render(request, 'login.html', {"err": err})

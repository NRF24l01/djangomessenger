from django.shortcuts import render
from django.http import HttpResponse
from json import dumps
from register.models import Users

def get_contack_info(request):
    print(request)
    id = request.GET.get("id", None)
    print(id)
    if not id:
        return HttpResponse("err, no id", 401)
    try:
        record = Users.objects.get(id=id)
        ret = {"email": record.email, "username": record.username, "name": record.name}
        return HttpResponse(dumps(ret))
    except Exception as e:
        return HttpResponse("caput, "+str(e), 401)

from django.shortcuts import render, redirect

# Create your views here.
def chatrender(request, chat_number):
    print(chat_number)
    return render(request, 'messenger.html')

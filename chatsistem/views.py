from django.shortcuts import render, redirect

# Create your views here.
def chatrender(request):
    return render(request, 'messenger.html')

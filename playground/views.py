from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# request -> response
# request handler
# action

def say_hello(request):
    # pull data from database
    return render(request, 'hello.html', {'name': 'Sok'})


def room(request):
    return HttpResponse('Hello World!')

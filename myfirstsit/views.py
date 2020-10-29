from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello This is my First Django Woooo.....")

def about(request):
    return HttpResponse("My name is Ismail.")


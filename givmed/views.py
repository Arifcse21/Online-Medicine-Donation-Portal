from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'givmed/index.html')


def register(request):
    return render(request, 'givmed/registration.html')




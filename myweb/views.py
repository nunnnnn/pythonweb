from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.
def index(req):
        return render(req,'myweb/index.html')

def united(req):
    return render(req,'myweb/index.html')


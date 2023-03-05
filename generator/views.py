from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'generator\home.html' )
#    return HttpResponse('Hello there friend!')

def about(request):
    return render(request, 'generator\\about.html')

def password(request):    
    charactors = list('abcdefghijklmnopqrstuvwxyz')
    length=10
    thepassword=''
    if request.GET.get('uppercase'):
        charactors.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        charactors.extend(list('1234567890'))
    if request.GET.get('special'):
        charactors.extend(list('!@#$%^&*()'))
    length=int(request.GET.get('length',12))
    for x in range(length):
        thepassword += random.choice(charactors)
    return render(request, 'generator\password.html', {'password':thepassword} )
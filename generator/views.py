from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator\home.html')


def about(request):
    return render(request, 'generator\About.html')






def password(request):
    c=list('abcdefghijklmnopqrstuvwxyz')
    l=int(request.GET.get('length',12))
    r=''
    if request.GET.get('uppercase'):
        c.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        c.extend(list('!@#$%^&*_+='))
    if request.GET.get('numbers'):
        c.extend(list('1234567890'))

    for i in range(l):
        r+=random.choice(c)
    return render(request, 'generator\password.html', {'password':r})

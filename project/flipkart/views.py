from django.shortcuts import render

from django.http import HttpResponse

def landing(req):
    data = {
        'name'='Vinika',
        'college'='RITS',}
    return render(req,'landing.html',data)
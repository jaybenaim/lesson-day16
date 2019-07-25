from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from datetime import datetime 

def root(request): 
    return HttpResponseRedirect('home') 

def home_page(request): 
    response = render(request, 'index.html') 
    return HttpResponse(response)

def todo_list(request): 

    current_time = datetime.now() 
    context = {
        'current_time': current_time, 
        'name': 'Jay', 
        'profile_pic_url': 'https://catass.com/cat', 
        'todo_list': ['feed cat', 'call gf']
    }
    response = render(request, 'todo_list.html', context)
    return HttpResponse(response) 
# not created by DJANGO

from django.http import HttpResponse
from django.shortcuts import render

# making function for different view i.e what data they will be showing
# it by default takes an request and return an httpresponse
def index(request):
    #with open('C:\\Users\\rosha\\OneDrive\\Desktop\\interview-experience\\django\\textutils\\textutils\\textutils\\fun.txt') as f:
    #    return HttpResponse("<br/>".join(f.readlines()))
    #return HttpResponse("this is homepage")
    params = {'name': "Roshan", 'place': "Delhi"}
    return render(request, 'index.html', params)

def about(request):
    return HttpResponse("About page <a href = '/'> Home Page </a> <a href = '/spaceRemove'>Space Remove </a>")

def charCount(request):
    return HttpResponse("Char count")

def spaceRemove(request):
    # getting the text whatever is sent through form using this below method
    print(request.GET.get('text', 'default'))
    return HttpResponse("Space Remove")

def firstCaps(request):
    return HttpResponse("First letter Capital")
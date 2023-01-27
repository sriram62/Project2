from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    return render(request,'input.html')
def add(request):
    x=int(request.POST["t1"])
    y=int(request.POST["t2"])
    z=x+y
    return HttpResponse("the sum is:"+str[z])

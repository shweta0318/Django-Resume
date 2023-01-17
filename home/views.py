from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
  #  return HttpResponse("<h1>App1:-Hello World Django </h1>")
    return render(request,"home.html")

def contact_me(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
  #  return HttpResponse("<h1>App1:-Hello World Django </h1>")
    return render(request,"contact_me.html")
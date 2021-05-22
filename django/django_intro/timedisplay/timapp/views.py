from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

   
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "time2":strftime("%A, %d %b %Y %H:%M:%S %p", gmtime())
    }
    return render(request,'index.html', context)

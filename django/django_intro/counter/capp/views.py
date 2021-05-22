from typing import Counter
from django.shortcuts import redirect, render, HttpResponse

def index(request):
    if 'counter' in request.session:
        request.session['counter'] +=1
    else:
            request.session['counter']=0
    
    return render(request,"index.html") 


def destroy(request):
    request.session.clear()
    return redirect('/') 

def add2(request):
     request.session['counter'] +=1
     return redirect("/")  


def addnumber(request):
    request.session['counter']+=int(request.POST['addn'])-1
    return redirect('/')

#### to del a specific key
# def destroy(request):
#     try:
#         del request.session['counter']
#     except KeyError:
#         print("Invalide access")    
#     return redirect('/')
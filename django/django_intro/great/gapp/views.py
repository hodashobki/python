from django.shortcuts import render, redirect ,HttpResponse
import random 


def index(request):
    if "numbers" not in request.session:
        request.session ["numbers"]=random.randint(1, 100)
        print( request.session ["numbers"])
    
    return render(request,"index.html")


def guess(request):
    if request.method=="POST":
        request.session['user']=int(request.POST['number'])
        if request.session['user'] ==request.session["numbers"]:
            
        
            return redirect("/")

        elif  request.session['user'] > request.session["numbers"]:
        
            return redirect("/")

        elif request.session['user']< request.session["numbers"]:
            
            return redirect("/")

def back(request):
     return redirect("/")


def reset(request):
    request.session.clear()
    return redirect("/")





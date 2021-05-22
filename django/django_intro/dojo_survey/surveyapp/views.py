from django.shortcuts import redirect, render, HttpResponse

def index(request):
    return render(request,"index.html")

def survey(request):
    request.session["name"] = request.POST["user-name"]
    request.session["location"] = request.POST["location"]
    request.session["language"] = request.POST["language"]
    request.session["pyth"] = request.POST["pyth"]
    request.session["comment"] = request.POST["comment"]
    
   

   
    return redirect("/success")


def success(request):

    return render(request,"info.html")


    
    
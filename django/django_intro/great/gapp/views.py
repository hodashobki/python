from django.shortcuts import render, redirect ,HttpResponse
import random 


def index(request):
    if "numbers" not in request.session:
        request.session ["numbers"]=random.randint(1, 100)
    
    return render(request,"index.html")


def guess(request):
    if int(request.POST['number'])==request.session["numbers"]:
        return render(request,"index1.html")

    elif  int(request.POST['number']) > request.session["numbers"]:
        return render(request,"index2.html")

    elif int(request.POST['number']) < request.session["numbers"]:
        return render(request,"index3.html")

def back(request):
     return redirect("/")




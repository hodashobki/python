from django.shortcuts import render,redirect,HttpResponse
from time import gmtime, strftime
import random 

def index(request):
    if 'your' not in request.session:
        request.session['your']=0
        request.session["activity"]=[]
    return render(request,"index.html")

def colgold(request):
    time=strftime("%Y-%m-%d %H:%M %p", gmtime())
    if request.method=='POST':
        
        if request.POST["gold"]=='farm':
            x=random.randint(1, 100)
            active=f"Earned {x} from farm at {time}"

        elif  request.POST["gold"]=='cave':
            x=random.randint(5, 10)
            active=f"Earned {x} from Cave at {time}"

        elif  request.POST["gold"]=='house':
            x=random.randint(2, 5)
            active=f"Earned {x} from House at {time}" 

        elif  request.POST["gold"]=='casino':
            x=random.randint(-20, 50)
            if x>0:
                active=f"Earned {x} from casino at {time}"
            else:
                active=f"Lost {x} from casino... ouch... at {time}"       
    
        request.session['your']+=x 
        request.session["activity"].append(active)      
    
    return redirect('/')            
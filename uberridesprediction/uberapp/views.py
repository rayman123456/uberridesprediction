from django.shortcuts import render,redirect
import os
import pickle
from . models import RidesPrediction

# Create your views here.

def index(request):
    obj=RidesPrediction.objects.all()
    return render(request, "index.html", {'obj':obj})

def test(request):
    ppw = int(request.POST['ppw'])
    pn = int(request.POST['pn'])
    mi =  int(request.POST['mi'])
    appm= int(request.POST['appm'])
    path=os.path.dirname(__file__) #root path of our application
    model=pickle.load(open(os.path.join(path,'taxi.pkl'), 'rb'))
    res=str(model.predict([[ppw,pn,mi,appm]])[0].round(2))
    rp=RidesPrediction(ppw=ppw,pn=pn,mi=mi,appm=appm,res=res) #orm
    rp.save()
    return redirect('index')

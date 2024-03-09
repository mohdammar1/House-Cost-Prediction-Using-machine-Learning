from django.shortcuts import render
from machinelearning.machinelearning import Predict

def run(a,b,c,d):
    return Predict.predict_price(a,b,c,d)
   
        
def home(request):
    if request.method=="POST":
        loc=request.POST.get('locations')
        area=request.POST.get('sqft')
        bath=request.POST.get('bath')
        bhk=request.POST.get('bhk')
        ans=run(loc,int(area),int(bath), int(bhk))
        ans=round(ans,2)
        ans=abs(ans)
        post=["Price: ",ans,"Lakhs"]
        return render(request,"gui.html",{"post":post})
    else:
        return render(request,"gui.html")
    



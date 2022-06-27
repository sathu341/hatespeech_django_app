from django.shortcuts import render,redirect
from .models import User_tbl

# Create your views here.
def index(request):
    return render(request,'index.html')
def userreg(req):
    if req.method=="POST":
        name=req.POST.get('name')
        email=req.POST.get('email')
        password=req.POST.get('password')
        mobile=req.POST.get('mobile')
        obj=User_tbl.objects.filter(email=email,password=password)
        if obj:
            return render(req,'register.html',{'msg':"email and password already existings"}) 
        else:      

            obj=User_tbl.objects.create(name=name,email=email,password=password,mobile=mobile)
            if obj:
                obj.save()

                return render(req,'login.html',{'msg':"Successfully Register"})   
            else:
                return render(req,'register.html',{'msg':" Not Successfully Register"})   

    return render(req,'register.html')    
def login(req):
    if req.method=="POST":
        email=req.POST.get('email')
        password=req.POST.get('password')
        obj=User_tbl.objects.filter(email=email,password=password)
        if obj:
            req.session['email']=email
            req.session['password']=password
            return render(req,'home.html',{'data':obj}) 

    return render(req,'login.html')       
def home(req):
    email=req.session['email']
    password=req.session['password']
    obj=User_tbl.objects.filter(email=email,password=password)
    if obj:
        return render(req,'home.html',{'data':obj})       
    else:
        return render(req,'index.html')    
    
def logout(req):
    req.session['email']=" "
    req.session['password']=" "

    return render(req,'index.html') 
def predic(req):
    if req.method=="POST":

        import pickle

        filename = 'F:\Djangoworks\hatespeech/finalized_model.sav'
        text=req.POST.get("prd")
        # load the model from disk
        loaded_model = pickle.load(open(filename, 'rb'))
       
        
        rs2=loaded_model.predict([text])
        print("Prediction ",rs2)
        if rs2==1:
            prd="Hate Speech"
            print("Hate speech")
        if rs2==0:
            prd=" Not Hate Speech"
            print("Not Hate Speech")   
        
 


        email=req.session['email']
        password=req.session['password']
        obj=User_tbl.objects.filter(email=email,password=password)
        if obj:
            return render(req,'home.html',{'data':obj,'prd':prd})       
        else:
            return render(req,'index.html')    

    

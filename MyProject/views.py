from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from User.models import User,Apartments, Villas,House,Office,Building,Townhouse,Shop,Garage,CommonProperties,ContactUs,PropertyAgents,ContactSeller,Addproperty,ClientReview
from django.urls import reverse
from django.core.mail import send_mail
import random
from datetime import datetime


def home(request):
    obj=CommonProperties.objects.get(id=1)
    l=[]
    Aprt=Apartments.objects.get(id=obj.A_id)
    l.append(Aprt)

    vill=Villas.objects.get(id=obj.V_id)
    l.append(vill)

    hom=House.objects.get(id=obj.H_id)
    l.append(hom)

    ofi=Office.objects.get(id=obj.O_id)
    l.append(ofi)

    buil=Building.objects.get(id=obj.B_id)
    l.append(buil)

    town=Townhouse.objects.get(id=obj.T_id)
    l.append(town)

    shop=Shop.objects.get(id=obj.S_id)
    l.append(shop)

    garag=Garage.objects.get(id=obj.G_id)
    l.append(garag)

    agents=PropertyAgents.objects.all()[0:4]
    clients=ClientReview.objects.all()
    return render(request,'Home.html',{'obj':l,'agents':agents,'clients':clients})

def about(request):

    return render(request,'About.html',locals())

def privacypolicy(request):
    return render(request,'PrivacyPolicy.html',locals())


def termsncondition(request):
    return render(request,'TermsAndCondition.html',locals())


def agents(request):
    agents=PropertyAgents.objects.all()
    return render(request,'AllAgents.html',locals())

def agentsdetail(request,pk):
    obj=PropertyAgents.objects.get(id=pk)
    return render(request,'AgentsDetail.html',locals())


def contactus(request):
    if request.method=='GET':
        return render(request,'ContactUs.html',locals())
    
    else:
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        ContactUs.objects.create(firstname=fname,lastname=lname,email=email,mobile=mobile,subject=subject,message=message)

        msg='We have received your request and will get in touch with you soon...!'
        return render(request,'ContactUs.html',locals())

    

def sigin(request):
    if request.method=='GET':
        return render(request,'Signin.html',locals())
    
    else:
        email=request.POST.get('email')
        password=request.POST.get('pass')

        obj=User.objects.filter(email=email)

        if not obj:
            exists=1
            return render(request,'Signin.html',locals())
        
        dbpassword=obj[0].password

        if password!=dbpassword:
            conpass=1
            forpass=1
            return render(request,'Signin.html',locals())
        global otp
        otp=str(random.randint(100000,999999))

        global Time
        Time=datetime.now().minute*60
        
        send_mail('Testting',otp,'mohammadyameen002@gmail.com',['mohammadyamin801@gmail.com',],fail_silently=False,)
        
        return HttpResponseRedirect('varify')
            
def forgotpass(request):
    if request.method=="GET":
        return render(request,'Forgotpass.html',locals())
    
    else:
        global otp
        otp=str(random.randint(100000,999999))
        email=request.POST.get('email')
        send_mail('Verify Your Email',otp,'mohammadyameen002@gmail.com',[email,],fail_silently=False,)

        return render(request,'PassVerify.html',locals())
def forpassvarify(request):
        fotp=request.POST.get('otp')
        if fotp!=otp:
            fotp=1
            fresend=1
            return render(request,'PassVerify.html',{'otp':fotp,'resend':fresend})
        else:
            return render(request,'Newpass.html',locals())
def changepass(request):
    email=request.POST.get('email')
    password=request.POST.get('pass')
    re_password=request.POST.get('re_pass')
    if password!=re_password:
        conpass=1
        return render(request,'Newpass.html',locals())
    
    else:
        obj=User.objects.get(email=email)
        obj.password=password
        obj.save()

        return render(request,'Signin.html',locals())



def signup(request):
    if request.method=='GET':
        return render(request,'Signup.html',locals())
        
    
    else:
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        re_password=request.POST.get('re_pass')
        db_email=User.objects.filter(email=email)

        if  db_email:
            exists=1
            return render(request,'Signup.html',locals())
        
        if password!=re_password:
            conpass=1
            return render(request,'Signup.html',locals())
        
        else:
            User(username=name,email=email,password=password).save()
            return HttpResponseRedirect('/')

def verify(request):
    if request.method=='GET':
        return render(request,'verify.html',locals())
    
    else:
        cotp=request.POST.get('otp')

        if cotp!=otp:
            return render(request,'verify.html',{'otp':1,'resend':1})
        
        ctime=datetime.now().minute*60

        if  ctime-Time>100:
            return render(request,'verify.html',{'resend':1,'time':1})
        
        else:
          return HttpResponseRedirect('home')

def resendotp(request):
    global otp
    otp=str(random.randint(100000,999999))
    send_mail('Testting',otp,'mohammadyameen002@gmail.com',['mohammadyamin801@gmail.com',],fail_silently=False,)
    return render(request,'verify.html',locals())



def apartment(request):
    obj=Apartments.objects.all()[0:9]
    return render(request,'Apartments.html',locals())

def apartmentsell(request):
    obj=Apartments.objects.filter(typeof='sell')[0:9]
    return render(request,'Apartments.html',locals())
        

def apartmentrent(request):
    obj=Apartments.objects.filter(typeof='rent')[0:9]
    return render(request,'Apartments.html',locals())

def apartmentdetail(request,pk):
    obj=Apartments.objects.get(id=pk)
    return render(request,'Detail.html',locals())

def villa(request):
    obj=Villas.objects.all()[0:9]
    return render(request,'Villas.html',locals())

def villadetail(request,pk):
    obj=Villas.objects.get(id=pk)
    print(obj.bed)
    return render(request,'Detail.html',locals())


def house(request):
    obj=House.objects.all()[0:9]
    return render(request,'House.html',locals())

def housesell(request):
    obj=House.objects.filter(typeof='sell')
    return render(request,'House.html',locals())

def houserent(request):
    obj=House.objects.filter(typeof='rent')
    return render(request,'House.html',locals())

def housedetail(request,pk):
    obj=House.objects.get(id=pk)
    return render(request,'Detail.html',locals())


def office(request):
    obj=Office.objects.all()[0:9]
    return render(request,'Office.html',locals())

def officesell(request):
    obj=Office.objects.filter(typeof='sell')[0:9]
    return render(request,'Office.html',locals())

def officerent(request):
    obj=Office.objects.filter(typeof='rent')[0:9]
    return render(request,'Office.html',locals())

def officedetail(request,pk):
    print(pk)
    obj=Office.objects.get(id=pk)
    return render(request,'Detail.html',locals())

def building(request):
    obj=Building.objects.all()[0:9]
    return render(request,'Building.html',locals())


def buildingdetail(request,pk):
    obj=Building.objects.get(id=pk)
    return render(request,'Detail.html',locals())



def townhouse(request):
    obj=Townhouse.objects.all()[0:9]
    return render(request,'Townhouse.html',locals())

def townhousesell(request):
    obj=Townhouse.objects.filter(typeof='sell')
    return render(request,'Townhouse.html',locals())

def townhouserent(request):
    obj=Townhouse.objects.filter(typeof='rent')
    return render(request,'Townhouse.html',locals())


def townhousedetail(request,pk):
    obj=Townhouse.objects.get(id=pk)
    return render(request,'Detail.html',locals())



def shop(request):
    obj=Shop.objects.all()[0:9]
    return render(request,'Shop.html',locals())


def shopsell(request):
    obj=Shop.objects.filter(typeof='sell')[0:9]
    return render(request,'Shop.html',locals())

def shoprent(request):
    obj=Shop.objects.filter(typeof='rent')[0:9]
    return render(request,'Shop.html',locals())


def shopdetail(request,pk):
    obj=Shop.objects.get(id=pk)
    return render(request,'Detail.html',locals())



def garage(request):
    obj=Garage.objects.all()[0:9]
    return render(request,'Garage.html',locals())

def garagesell(request):
    obj=Garage.objects.filter(typeof='sell')[0:9]
    return render(request,'Garage.html',locals())

def garagerent(request):
    obj=Garage.objects.filter(typeof='rent')[0:9]
    return render(request,'Garage.html',locals())


def garagedetail(request,pk):
    obj=Garage.objects.get(id=pk)
    return render(request,'Detail.html',locals())



def search(request):
    tab=request.GET.get('tab')
    p_type=request.GET.get('ptype')
    location=request.GET.get('location')
    city=request.GET.get('city')
    price=int(request.GET.get('price'))
    print(tab,p_type,location,city,price)

    if  p_type=='Appartment' :
        print("Hello")
        obj=Apartments.objects.filter(typeof=tab,location=location,city=city,price__lte=price)[0:9]
        if obj:
            return render(request,'Apartments.html',locals())
        else:
            not_found=1
            return render(request,'Home.html',locals())
    
    if  p_type=='Villas' :
        obj=Villas.objects.filter(typeof=tab,location=location,city=city,price__lte=price)[0:9]
        if obj:
            return render(request,'Villas.html',locals())
        else:
            not_found=1
            return render(request,'Home.html',locals())
    
    if  p_type=='Home' :
        obj=House.objects.filter(typeof=tab,location=location,city=city,price__lte=price)[0:9]
        if obj:
            return render(request,'House.html',locals())
        else:
            not_found=1
            return render(request,'Home.html',locals())
    
    if  p_type=='Office' :
        obj=Office.objects.filter(typeof=tab,location=location,city=city,price__lte=price)[0:9]
        if obj:
            return render(request,'Office.html',locals())
        else:
            not_found=1
            return render(request,'Home.html',locals())
    
    if  p_type=='Building' :
        obj=Building.objects.filter(typeof=tab,location=location,city=city,price__lte=price)[0:9]
        if obj:
            return render(request,'building.html',locals())
        else:
            not_found=1
            return render(request,'Home.html',locals())
    
    if  p_type=='Townhouse' :
        obj=Townhouse.objects.filter(typeof=tab,location=location,city=city,price__lte=price)[0:9]
        if obj:
            return render(request,'Townhouse.html',locals())
        else:
            not_found=1
            return render(request,'Home.html',locals())
    
    if  p_type=='Shop' :
        obj=Shop.objects.filter(typeof=tab,location=location,city=city,price__lte=price)[0:9]
        if obj:
            return render(request,'Shop.html',locals())
        else:
            not_found=1
            return render(request,'Home.html',locals())
    
    if p_type=='Garage':
        print("Hello")
        obj=Garage.objects.filter(typeof=tab,location=location,city=city,price__lte=price)[0:9]
        if obj:
            return render(request,'Garage.html',locals())
        else:
            not_found=1
            return render(request,'Home.html',locals())
    else:
        not_found=1
        return render(request,'Home.html',locals())


   
def contactseller(request):
    if request.method=='GET':
        return render(request,'ContactSeller.html',locals())

    else:

        reason=request.POST.get('reason')
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        ContactSeller.objects.create(reason=reason,name=name,email=email,mobile=mobile)
        return render(request,'ContactSeller.html',locals())


def addproperty(request):
    if request.method=="GET":
        return render(request,'AddProperty.html',locals())
    
    else:
        youare=request.POST.get('youare')
        typeof=request.POST.get('typeof')
        ptype=request.POST.get('ptype')
        bed=request.POST.get('bed')
        bath=request.POST.get('bath')
        status=request.POST.get('saletype')
        facing=request.POST.get('facing')
        price=request.POST.get('price')
        approved=request.POST.get('approved')
        tokenamount=request.POST.get('tokenamount')
        area=request.POST.get('area')
        rate=request.POST.get('rate')
        roadwidth=request.POST.get('roadwidth')
        locality=request.POST.get('locality')
        city=request.POST.get('city')
        landmark=request.POST.get('landmark')
        contactdetail=request.POST.get('contactdetail')
        altcontact=request.POST.get('altcontact')
        image1=request.POST.get('image1')
        image2=request.POST.get('image2')
        image3=request.POST.get('image3')


        
        Addproperty.objects.create(typeof=typeof,bed=bed,bath=bath,price=price,location=locality,city=city,area=area,image1=image1,image2=image2,image3=image3,Bhk=bed,approved=approved,landmark=landmark,status=status,youare=youare,facing=facing,tokenamount=tokenamount,rate=rate,roadwidth=roadwidth,contactdetail=contactdetail,altcontact=altcontact)
        return render(request,'AddProperty.html',locals())
       






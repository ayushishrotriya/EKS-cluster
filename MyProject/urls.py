
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from MyProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('',sigin,name="signin"),
    path('signup',signup,name="signup"),
    path('forgotpass',forgotpass,name="forgotpass"),
    path('changepass',changepass,name="changepass"),
    path('forpassvarify',forpassvarify,name="forpassvarify"),
    path('varify',verify,name='verify'),
    path('resendotp',resendotp,name='resendotp'),
    path('home',home,name="home"),
    path('apartment',apartment,name="apartment"),
    path('apartmentsell',apartmentsell,name="apartmentsell"),
    path('apartmentrent',apartmentrent,name="apartmentrent"),
    path('apartmentdetail/<int:pk>',apartmentdetail,name="apartmentdetail"),
    path('villa',villa,name="villa"),
    path('villadetail/<int:pk>',villadetail,name="villadetail"),
    path('house',house,name="house"),
    path('housesell',housesell,name="housesell"),
    path('houserent',houserent,name="houserent"),
    path('housedetail/<int:pk>',housedetail,name="housedetail"),
    path('office',office,name="office"),
    path('officesell',officesell,name="officesell"),
    path('officerent',officerent,name="officerent"),
    path('officedetail/<int:pk>',officedetail,name="officedetail"),
    path('building',building,name="building"),
    path('buildingdetail/<int:pk>',buildingdetail,name="buildingdetail"),
    path('townhouse',townhouse,name="townhouse"),
    path('townhousesell',townhousesell,name="townhousesell"),
    path('townhouserent',townhouserent,name="townhouserent"),
    path('townhousedetail/<int:pk>',townhousedetail,name="townhousedetail"),
    path('shop',shop,name="shop"),
    path('shopsell',shopsell,name="shopsell"),
    path('shoprent',shoprent,name="shoprent"),
    path('shopdetail/<int:pk>',shopdetail,name="shopdetail"),
    path('garage',garage,name="garage"),
    path('garagesell',garagesell,name="garagesell"),
    path('garagerent',garagerent,name="garagerent"),
    path('garagedetail/<int:pk>',garagedetail,name="garagedetail"),
    path('search',search,name="search"),
    path('about',about,name="about"),
    path('contactus',contactus,name="contactus"),
    path('agents',agents,name="agents"),
    path('agentsdetail/<int:pk>',agentsdetail,name="agentsdetail"),
    path('contactseller',contactseller,name="contactseller"),
    path('addproperty',addproperty,name='addproperty'),
    path('privacypolicy',privacypolicy,name="privacypolicy"),
    path('termsncondition',termsncondition,name="termsncondition"),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

print(static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))

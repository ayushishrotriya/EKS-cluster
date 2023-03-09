from django.contrib import admin
from .models import User,Apartments,Villas,House,Office,Building,Townhouse,Shop,Garage,CommonProperties,PropertyAgents,Addproperty,ClientReview,ContactSeller
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display =('id','username','email','password')

admin.site.register(User, UserAdmin)

class ApartmentsAdmin(admin.ModelAdmin):
    list_display =('id','typeof','image','price','title','location','area','bed','bath')

admin.site.register(Apartments, ApartmentsAdmin)

class VillasAdmin(admin.ModelAdmin):
    list_display =('id','image','price','title','location','area','bed')

admin.site.register(Villas, VillasAdmin)

class HouseAdmin(admin.ModelAdmin):
    list_display =('id','typeof','image','price','title','location','area','bed','bath')

admin.site.register(House, HouseAdmin)

class OfficeAdmin(admin.ModelAdmin):
    list_display =('id','typeof','image','price','title','location','area',)

admin.site.register(Office, OfficeAdmin)


class BuildingAdmin(admin.ModelAdmin):
    list_display =('id','image','price','title','location','area','floor')

admin.site.register(Building, BuildingAdmin)


class TownhouseAdmin(admin.ModelAdmin):
    list_display =('id','typeof','image','price','title','location','area','bed','bath')

admin.site.register(Townhouse, TownhouseAdmin)

class ShopAdmin(admin.ModelAdmin):
    list_display =('id','typeof','image','price','title','location','area',)

admin.site.register(Shop, ShopAdmin)


class GarageAdmin(admin.ModelAdmin):
    list_display =('id','typeof','image','price','title','location','area',)

admin.site.register(Garage, GarageAdmin)


class CommonPropertiesAdmin(admin.ModelAdmin):
    list_display =('id','V','A','O','H','T','B','G','S')

admin.site.register(CommonProperties, CommonPropertiesAdmin)



class PropertyAgentsAdmin(admin.ModelAdmin):
    list_display =('id','image','fburl','twiturl','instaurl','fullname','contact','address','email','deals','firm','exp')

admin.site.register(PropertyAgents, PropertyAgentsAdmin)



class AddpropertyAdmin(admin.ModelAdmin):
    list_display =('id','ptype','typeof','price','location','city','area','bed','bath','image1','image2','image3','Bhk','approved','landmark','status','rate','tokenamount','additionalroom','cornerprop','youare','saletype','facing','roadwidth','locality','contactdetail','altcontact')

admin.site.register(Addproperty, AddpropertyAdmin)


class ClientReviewAdmin(admin.ModelAdmin):
    list_display =('id','image','name','profession','review')

admin.site.register(ClientReview, ClientReviewAdmin)


class ContactSellerAdmin(admin.ModelAdmin):
    list_display =('id','reason','name','email','mobile')

admin.site.register(ContactSeller, ContactSellerAdmin)


from email import message
from email.policy import default
from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)


class Apartments(models.Model):
    name=models.CharField(max_length=50,default='Apartment')
    typeof=models.CharField(max_length=50)
    image=models.FileField(upload_to='images/Apartment', max_length=100)
    price=models.IntegerField(default=6)
    title=models.CharField(max_length=50,default="Apartment")
    location=models.CharField(max_length=50)
    city=models.CharField(max_length=50,default='Jaipur')
    area=models.CharField(max_length=50)
    bed=models.IntegerField()
    bath=models.IntegerField()
    image1=models.FileField(upload_to='images/Apartment', max_length=200,default='images/v8.jpg')
    image2=models.FileField(upload_to='images/Apartment', max_length=200,default='images/v8.jpg')
    image3=models.FileField(upload_to='images/Apartment', max_length=200,default='images/v8.jpg')
    Bhk=models.IntegerField(default=2)
    approved=models.CharField(max_length=50,default='Yes')
    landmark=models.CharField(max_length=50,default='Near Tonk Road')
    floors=models.IntegerField(default=3)
    status=models.CharField(max_length=50,default='Fresh')
    rate=models.CharField(max_length=50,default='54216')
    tokenamount=models.CharField(max_length=50,default='500000')
    additionalroom=models.CharField(max_length=50,default='Room')
    cornerprop=models.CharField(max_length=5,default='NO')
    detail=models.CharField(max_length=50,default='apartmentdetail')
    


class Villas(models.Model):
    typeof=models.CharField(max_length=50,default='sell')
    name=models.CharField(max_length=50,default='Villa')
    image=models.FileField(upload_to='images/villas', max_length=100)
    price=models.IntegerField(default=6)    
    title=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    city=models.CharField(max_length=50,default='Jaipur')
    area=models.CharField(max_length=50)
    bed=models.IntegerField()
    Bhk=models.IntegerField(default=2)
    bed=models.IntegerField(default=5)
    bath=models.IntegerField(default=6)
    approved=models.CharField(max_length=50,default='Yes')
    area=models.CharField(max_length=50,default='2245')
    rate=models.CharField(max_length=50,default='54216')
    tokenamount=models.CharField(max_length=50,default='500000')
    additionalroom=models.CharField(max_length=50,default='Fram House')
    landmark=models.CharField(max_length=50,default='Near Tonk Road')
    status=models.CharField(max_length=50,default='Fresh')
    cornerprop=models.CharField(max_length=5,default='Yes')
    detail=models.CharField(max_length=50,default='villadetail')
    image1=models.FileField(upload_to='images/villas', max_length=200,default='images/v8.jpg')
    image2=models.FileField(upload_to='images/villas', max_length=200,default='images/v8.jpg')
    image3=models.FileField(upload_to='images/villas', max_length=200,default='images/v8.jpg')
    Bhk=models.IntegerField(default=2)
    

class House(models.Model):
    name=models.CharField(max_length=50,default='Home')
    typeof=models.CharField(max_length=50)
    image=models.FileField(upload_to='images/House', max_length=100)
    price=models.IntegerField(default=6)
    title=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    city=models.CharField(max_length=50,default='Jaipur')
    area=models.CharField(max_length=50)
    bed=models.IntegerField()
    bath=models.IntegerField()
    detail=models.CharField(max_length=50,default='housedetail')
    image1=models.FileField(upload_to='images/House', max_length=200,default='images/v8.jpg')
    image2=models.FileField(upload_to='images/House', max_length=200,default='images/v8.jpg')
    image3=models.FileField(upload_to='images/House', max_length=200,default='images/v8.jpg')
    rate=models.CharField(max_length=50,default='54216')
    tokenamount=models.CharField(max_length=50,default='500000')
    additionalroom=models.CharField(max_length=50,default='Room')
    cornerprop=models.CharField(max_length=5,default='NO')
    Bhk=models.IntegerField(default=2)
    landmark=models.CharField(max_length=50,default='Near Tonk Road')
    approved=models.CharField(max_length=50,default='Yes')
   

class Office(models.Model):
    name=models.CharField(max_length=50,default='Office')
    typeof=models.CharField(max_length=50)
    image=models.FileField(upload_to='images/Office', max_length=100)
    price=models.IntegerField(default=6)
    title=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    city=models.CharField(max_length=50,default='Jaipur')
    area=models.CharField(max_length=50)
    detail=models.CharField(max_length=50,default='officedetail')
    image1=models.FileField(upload_to='images/Office', max_length=200,default='images/v8.jpg')
    image2=models.FileField(upload_to='images/Office', max_length=200,default='images/v8.jpg')
    image3=models.FileField(upload_to='images/Office', max_length=200,default='images/v8.jpg')
    Bhk=models.IntegerField(default=2)
    approved=models.CharField(max_length=50,default='Yes')
    bath=models.IntegerField(default=2)
    landmark=models.CharField(max_length=50,default='Near Tonk Road')
    rate=models.CharField(max_length=50,default='54216')
    tokenamount=models.CharField(max_length=50,default='500000')
    additionalroom=models.CharField(max_length=50,default='Room')
    cornerprop=models.CharField(max_length=5,default='NO')
   







class Building(models.Model):
    name=models.CharField(max_length=50,default='Building')
    image=models.FileField(upload_to='images/Building', max_length=100)
    price=models.IntegerField(default=6)
    title=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    city=models.CharField(max_length=50,default='Jaipur')
    area=models.CharField(max_length=50)
    floor=models.IntegerField()
    detail=models.CharField(max_length=50,default='buildingdetail')
    image1=models.FileField(upload_to='images/Building', max_length=200,default='images/v8.jpg')
    image2=models.FileField(upload_to='images/Building', max_length=200,default='images/v8.jpg')
    image3=models.FileField(upload_to='images/Building', max_length=200,default='images/v8.jpg')
    Bhk=models.IntegerField(default=2)
    approved=models.CharField(max_length=50,default='Yes')
    landmark=models.CharField(max_length=50,default='Near Tonk Road')
    rate=models.CharField(max_length=50,default='54216')
    tokenamount=models.CharField(max_length=50,default='500000')
    additionalroom=models.CharField(max_length=50,default='Room')
    cornerprop=models.CharField(max_length=5,default='NO')
    typeof=models.CharField(max_length=50,default='sell')
   



class Townhouse(models.Model):
    name=models.CharField(max_length=50,default='Townhouse')
    typeof=models.CharField(max_length=50)
    image=models.FileField(upload_to='images/Townhouse', max_length=100)
    price=models.IntegerField(default=6)
    title=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    city=models.CharField(max_length=50,default='Jaipur')
    area=models.CharField(max_length=50)
    bed=models.IntegerField()
    bath=models.IntegerField()
    detail=models.CharField(max_length=50,default='townhousedetail')
    image1=models.FileField(upload_to='images/Townhouse', max_length=200,default='images/v8.jpg')
    image2=models.FileField(upload_to='images/Townhouse', max_length=200,default='images/v8.jpg')
    image3=models.FileField(upload_to='images/Townhouse', max_length=200,default='images/v8.jpg')
    rate=models.CharField(max_length=50,default='54216')
    tokenamount=models.CharField(max_length=50,default='500000')
    additionalroom=models.CharField(max_length=50,default='Room')
    cornerprop=models.CharField(max_length=5,default='NO')
    Bhk=models.IntegerField(default=2)
    landmark=models.CharField(max_length=50,default='Near Tonk Road')
    approved=models.CharField(max_length=50,default='Yes')
   

class Shop(models.Model):
    name=models.CharField(max_length=50,default='Shop')
    typeof=models.CharField(max_length=50)
    image=models.FileField(upload_to='images/Shop', max_length=100)
    price=models.IntegerField(default=6)
    title=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    city=models.CharField(max_length=50,default='Jaipur')
    area=models.CharField(max_length=50)
    detail=models.CharField(max_length=50,default='shopdetail')
    image1=models.FileField(upload_to='images/Shop', max_length=200,default='images/v8.jpg')
    image2=models.FileField(upload_to='images/Shop', max_length=200,default='images/v8.jpg')
    image3=models.FileField(upload_to='images/Shop', max_length=200,default='images/v8.jpg')
    Bhk=models.IntegerField(default=2)
    approved=models.CharField(max_length=50,default='Yes')
    bath=models.IntegerField(default=2)
    landmark=models.CharField(max_length=50,default='Near Tonk Road')
    rate=models.CharField(max_length=50,default='54216')
    tokenamount=models.CharField(max_length=50,default='500000')
    additionalroom=models.CharField(max_length=50,default='Room')
    cornerprop=models.CharField(max_length=5,default='NO')
   

class Garage(models.Model):
    name=models.CharField(max_length=50,default='Garage')
    typeof=models.CharField(max_length=50)
    image=models.FileField(upload_to='images/Garage', max_length=100)
    price=models.IntegerField(default=6)
    title=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    city=models.CharField(max_length=50,default='Jaipur')
    area=models.CharField(max_length=50)
    detail=models.CharField(max_length=50,default='garagedetail')
    image1=models.FileField(upload_to='images/Garage', max_length=200,default='images/v8.jpg')
    image2=models.FileField(upload_to='images/Garage', max_length=200,default='images/v8.jpg')
    image3=models.FileField(upload_to='images/Garage', max_length=200,default='images/v8.jpg')
    Bhk=models.IntegerField(default=2)
    approved=models.CharField(max_length=50,default='Yes')
    bath=models.IntegerField(default=2)
    landmark=models.CharField(max_length=50,default='Near Tonk Road')
    rate=models.CharField(max_length=50,default='54216')
    tokenamount=models.CharField(max_length=50,default='500000')
    additionalroom=models.CharField(max_length=50,default='Room')
    cornerprop=models.CharField(max_length=5,default='NO')
   


class CommonProperties(models.Model):
    V=models.OneToOneField(Villas, on_delete=models.CASCADE)
    A=models.OneToOneField(Apartments, on_delete=models.CASCADE)
    O=models.OneToOneField(Office, on_delete=models.CASCADE)
    H=models.OneToOneField(House, on_delete=models.CASCADE)
    T=models.OneToOneField(Townhouse, on_delete=models.CASCADE)
    B=models.OneToOneField(Building, on_delete=models.CASCADE)
    G=models.OneToOneField(Garage, on_delete=models.CASCADE)
    S=models.OneToOneField(Shop, on_delete=models.CASCADE)



class ContactUs(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    mobile=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.TextField()



class PropertyAgents(models.Model):
    image=models.FileField(upload_to='images/Agents', max_length=100)
    fburl=models.CharField(max_length=50)
    twiturl=models.CharField(max_length=50)
    instaurl=models.CharField(max_length=50)
    fullname=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    deals=models.IntegerField(default=5)
    firm=models.CharField(max_length=50,default='Aashiyana Property')
    exp=models.CharField(max_length=50,default='12')

    



class ContactSeller(models.Model):
    reason=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    mobile=models.CharField(max_length=50)




class Addproperty(models.Model):
    ptype=models.CharField(max_length=50)
    typeof=models.CharField(max_length=50)
    price=models.IntegerField(default=6)
    location=models.CharField(max_length=50)
    city=models.CharField(max_length=50,default='Jaipur')
    area=models.CharField(max_length=50)
    bed=models.IntegerField()
    bath=models.IntegerField()
    image1=models.FileField(upload_to='images/AddProperties', max_length=200,default='images/v8.jpg')
    image2=models.FileField(upload_to='images/AddProperties', max_length=200,default='images/v8.jpg')
    image3=models.FileField(upload_to='images/AddProperties', max_length=200,default='images/v8.jpg')
    Bhk=models.IntegerField(default=2)
    approved=models.CharField(max_length=50,default='Yes')
    landmark=models.CharField(max_length=50,default='Near Tonk Road')
    status=models.CharField(max_length=50,default='Fresh')
    rate=models.CharField(max_length=50,default='54216')
    tokenamount=models.CharField(max_length=50,default='500000')
    additionalroom=models.CharField(max_length=50,default='Room')
    cornerprop=models.CharField(max_length=5,default='NO')
    youare=models.CharField(max_length=50,default="Agent")
    saletype=models.CharField(max_length=50,default='Fresh')
    facing=models.CharField(max_length=50,default="East")
    roadwidth=models.IntegerField(default=20)
    locality=models.CharField(max_length=50,default="Kumbha Marg")
    contactdetail=models.CharField(max_length=50,default='7698679876')
    altcontact=models.CharField(max_length=50,default='8778986745')


class ClientReview(models.Model):
    image=models.FileField(upload_to='imgaes/Clients', max_length=100)
    name=models.CharField( max_length=50)
    profession=models.CharField(max_length=50)
    review=models.CharField(max_length=50)

    def __str__(self):
        return self.review

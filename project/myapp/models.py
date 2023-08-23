from django.db import models
from django.contrib.auth.models import User
# Create your models here.

'''
class Vendor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(null=True)
    def __str__(self):
        return self.user.username

class ProductCategory(models.Model):
    title =models.CharField(max_length=200)
    detail=models.TextField(null=True)
    def __str__(self):
      return self.title

class Product (models.Model):
   name = models.CharField(max_length=200)
   vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
   category = models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True)
   detail=models.TextField(null=True)
   price = models.FloatField(null=False)
   def __str__(self):
      return self.name
   
class Costumer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.PositiveBigIntegerField()
    def __str__(self):
        return self.user.username

class CostumerAdress(models.Model):
    Costumer=models.ForeignKey(Costumer,on_delete=models.CASCADE)
    address=models.TextField()
    default_address=models.BooleanField(default=False)
    def __str__(self):
        return self.address

class Order(models.Model):
    costumer=models.ForeignKey(Costumer,on_delete=models.CASCADE)
    order_time=models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return '%s' %(self.order_time)

class OrderItem(models.Model):
    costumer=models.ForeignKey(Costumer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.product.title
    
class ProductRating(models.Model):
    customer=models.ForeignKey(Costumer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    rating=models.IntegerField()
    reviews=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.reviews
'''
#________________________________________________
class Color(models.Model):
    Color=models.TextField()
    def __str__(self):
        return self.Color

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)  


class Image(models.Model):
    Image=models.ImageField(upload_to=upload_to,null=False,blank=False)

class Album(models.Model):
   album =models.ManyToManyField(Image)

class Device(models.Model):
    name=models.TextField(max_length=100)
    price=models.FloatField(null=False)
    MATERIAL_CHOICES = (
        ('Metal', 'Metal'),
        ('Plastic', 'Plastic'),
        ('Glass', 'Glass'),
        ('Other', 'Other'),
        ('Aluminum','aluminum'),
    )
    material = models.CharField(max_length=10, choices=MATERIAL_CHOICES,default='other')
    release_date=models.DateField()
    album =models.OneToOneField(Album,on_delete=models.CASCADE,blank=True,null=True)
    cover_image=models.ImageField(upload_to=upload_to,blank=True,null=True)
    detail=models.TextField(max_length=100,blank=True,null=True)
    colors=models.ManyToManyField(Color,blank=True)
    STATE=(
        ('new', 'New'),
        ('old', 'Old'),
        )
    state=models.CharField(max_length=10,choices=STATE,default='new',blank=True,null=True)
    nb=models.IntegerField(null=False)
    discount=models.BooleanField(default=False)
    discount_perc=models.IntegerField(default=0)
    popularity=models.IntegerField(default=0)
    rtnb=models.IntegerField(default=0)
    rating=models.IntegerField(default=0)
    tags=models.TextField(null=True)
    date=models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
    def tag_list(self):
      if self.tags:
         taglist = self.tags.split(',')
         return taglist
      return []

class Laptop(Device):
   battery=models.IntegerField()
   CATEGORY=(
       ('Ultrabook','Ultrabook'),
       ('NetBook','Netbook'),
       ('Classic','Classic'),
       ('Notebook','Notebook'),
       ('1 in 2 laptop','1 in 2 laptop'),
       ('Gamer','Gamer'),
       ('Elitebook','Elitebook'),
       ('Probook','Probook'),
    )
   category=models.CharField(max_length=20, choices=CATEGORY,default='Apple')
   BRAND=(
        ('Dell', 'Dell'),
        ('Lenovo', 'Lenovo'),
        ('Apple', 'Apple'),
        ('Acer', 'Acer'),
        ('Hp', 'Hp'),
        ('Microsoft', 'Microsoft'),
        ('Toshiba', 'Toshiba'),
        ('D-tech', 'D-tech'),   
    )
   brand=models.CharField(max_length=10,choices=BRAND,default='Dell')
   os=models.TextField(max_length=100,blank=True)
   PRO=(
       ('Intel Core i3','Intel Core i3'),
       ('Intel Core i5','Intel Core i5'),
       ('Intel Core i7','Intel Core i3'),
       ('Intel Core i9','Intel Core i9'),
       ('AMD Ryzen 3','AMD Ryzen 3'),
       ('AMD Ryzen 5','AMD Ryzen 5'),
       ('AMD Ryzen 7','AMD Ryzen 7'),
       ('AMD Ryzen 9','AMD Ryzen 9'),
       ('M1','M1'),
       ('M2','M2'),
       ('Celeron','Celeron'),
       )
   processor_type=models.CharField(max_length=20,choices=PRO,default='Intel Core i3')
   Processor=models.TextField()
   SCREEN=(
       (11, '11 inches'),
       (12, '12 inches'),
       (13, '13 inches'),
       (14, '14 inches'),
       (15, '15 inches'),
       (16, '16 inches'),
       (17, '17 inches'),
       (18, '18 inches'),
    )
   screen_size=models.IntegerField(choices=SCREEN,default=15)
   screen_type=models.CharField(max_length=30,blank=True)
   graphic_card=models.TextField(max_length=50,blank=True)
   GC=(
       ('intern','Intern'),
       ('extern','Extern'),
    )
   graphic_card_type=models.CharField(max_length=10,choices=GC,default='intern')
   Weight=models.FloatField(blank=True)
   cache_mem=models.IntegerField(null=True,blank=True)
   ram = models.IntegerField(choices=((0, '0 GB'), (2, '2 GB'), (4, '4 GB'), (16, '16 GB'), (32, '32 GB'), (64, '64 GB')))
   DISK=(
       (0,'0 GB'),
       (64,'64 GB'),
       (128,'128 GB'), 
       (256,'256 GB'),
       (512,'512 GB'),       
       (1028,'1028 GB'),
       (2048,'2048 GB'),
    )
   hard_disk=models.IntegerField(choices=DISK,default=0,blank=True)
   DT=(
       ('SSD','ssd'),
       ('HDD','hdd'),
    )
   hard_disk_type=models.CharField(max_length=10,choices=DT,default='SSD')
   wifi=models.BooleanField(default=True)
   bluetooth=models.BooleanField(default=True)
   Webcam=models.BooleanField(default=True)

class Tablet(Device):
   battery=models.IntegerField()
   BRAND=(
      ('Samsung','Samsung'),  
      ('Iris','Iris'),
      ('Apple','Apple'),
      ('C-idea','C-idea'),
      ('Hwawei','Hwawei'),
      ('Condor','Condor'),
      ('Lenovo','Lenovo'),
      ('Black View','Black_view'),
      ('D-tech','D-tech'),     
    )
   brand=models.TextField(max_length=20,choices=BRAND,default='other')
   SYSTEM=(
       ('Android','Android'),
       ('IOS','IOS'),
    )
   System=models.TextField(max_length=10,choices=SYSTEM)
   camera=models.FloatField()
   front_cam=models.FloatField()
   Processor=models.TextField()
   SCREEN=(
       (5, '5 inches'),
       (6, '6 inches'),
       (7, '7 inches'),
       (8, '8 inches'),
       (9, '9 inches'),
       (10, '10 inches'),
       (11, '11 inches'),
       (12, '12 inches'),
    )
   screen_size=models.IntegerField(choices=SCREEN,default=15)
   screen_type=models.CharField(max_length=30)
   Weight=models.FloatField()
   RAM=(
       (0,'0 GB'),
       (1,'1 GB'),
       (2,'2 GB'),
       (4,'4 GB'),
       (16,'16 GB'),
    )
   Ram=models.IntegerField(choices=RAM,default=0)
   DISK=(
       (0,'0 GB'),
       (4,'4 GB'),
       (16,'16 GB'),
       (32,'32 GB'),
       (64,'64 GB'), 
    )
   hard_disk=models.IntegerField(choices=DISK,default=0)
   usb=models.BooleanField(default=False)
   sim_card=models.BooleanField(default=False)
   wifi=models.BooleanField(default=False)
   bluetooth=models.BooleanField(default=False)
   hdmi=models.BooleanField(default=False)
   mem_card=models.BooleanField(default=False)
   gps=models.BooleanField(default=False)
   radio=models.BooleanField(default=True)
   RS=(
       (2,'2G'),
       (3,'3G'),
       (4,'4G'),
       (5,'5G'),
    )
   Reseau=models.IntegerField(choices=RS,default='4G')

class SmartPhone(Device):
   battery=models.IntegerField()
   BRAND=(
      ('Samsung','Samsung'),  
      ('Iris','Iris'),
      ('Apple','Apple'),
      ('Xiaomi','Xiaomi'),
      ('Hwawei','Hwawei'),
      ('Infinix','Infinix'),
      ('Realme','Realme'),
      ('Nokia','Nokia'),  
      ('Oppo','Oppo'),
      ('Ace','Ace'),
      ('Google','Google'),
      ('Microsoft','Microsoft'),
      ('Starlight','Starlight'),   
    )
   brand=models.TextField(max_length=10,choices=BRAND,default='Ace')
   SYSTEM=(
       ('Android 1.0','android 1.0'),
       ('Android 1.1','android 1.1'),
       ('Android 1.5','android 1.5'),
       ('Android 1.6','android 1.6'),
       ('Android 2.0','android 2.0'),
       ('Android 2.3','android 2.3'),
       ('Android 3.0','android 3.0'),
       ('Android 4.0','android 4.0'),
       ('Android 4.1','android 4.1'),
       ('Android 4.4','android 4.4'),
       ('Android 5.0','android 5.0'),
       ('Android 6.0','android 6.0'),
       ('Android 7.O','android 7.0'),
       ('Android 8.0','android 8.0'),
       ('Android 9.0','android 9.0'),
       ('Android 10','android 10'),
       ('Android 11','android 11'),
       ('Android 12','android 12'),
       ('Android 13','android 13'),
       ('Android 14','android 14'),
       ('IOS 1','IOS 1'),
       ('IOS 2','IOS 2'),
       ('IOS 3','IOS 3'),
       ('IOS 4','IOS 4'),
       ('IOS 5','IOS 5'),
       ('IOS 6','IOS 6'),
       ('IOS 7','IOS 7'),
       ('IOS 8','IOS 8'),
       ('IOS 9','IOS 9'),
       ('IOS 10','IOS 10'),
       ('IOS 11','IOS 11'),
       ('IOS 12','IOS 12'),
       ('IOS 13','IOS 13'),
       ('IOS 14','IOS 14'),
       ('IOS 15','IOS 15'),

    )
   System=models.TextField(choices=SYSTEM)
   camera=models.FloatField()
   camera_info=models.TextField()
   front_cam=models.FloatField()
   front_cam_info=models.TextField()
   Processor=models.TextField()
   SCREEN=(
       (4, '4 inches'),
       (5, '5 inches'),
       (6, '6 inches'),
       (7, '7 inches'),
       (8, '8 inches'),
    )
   screen_size=models.IntegerField(choices=SCREEN,default=15)
   screen_type=models.CharField(max_length=30)
   Weight=models.FloatField()
   RAM=(
       (0,'0 GB'),
       (1,'1 GB'),
       (2,'2 GB'),
       (4,'4 GB'),
       (16,'16 GB'),
    )
   Ram=models.IntegerField(choices=RAM,default=0)
   DISK=(
       (0,'0 GB'),
       (1,'1 GB'),
       (2,'2 GB'),
       (4,'4 GB'),
       (16,'16 GB'),
       (32,'32 GB'),
       (64,'64 GB'), 
       (128,'128 GB'),
       (256,'256 GB'),
    )
   hard_disk=models.IntegerField(choices=DISK,default=0)
   Chipset=models.TextField()
   gpu=models.TextField()
   SCT=(
      ('Normal sim','Normal Sim'),
      ('Micro sim','Micro Sim'),
      ('Nano sim','Nano Sim'),
    )
   double_sim=models.BooleanField(default=False)
   sim_card_type=models.TextField(max_length=10,choices=SCT,default='Nano Sim')
   wifi=models.BooleanField(default=False)
   bluetooth=models.BooleanField(default=False)
   hdmi=models.BooleanField(default=False)
   mem_card=models.BooleanField(default=False)
   gps=models.BooleanField(default=False)
   radio=models.BooleanField(default=True)
   RS=(
       (2,'2G'),
       (3,'3G'),
       (4,'4G'),
       (5,'5G'),
    )
   Reseau=models.IntegerField(choices=RS,default=4)  
   wireless_charging=models.BooleanField(default=False)

class SmartWatch(Device):
   BRAND=(
      ('Samsung', 'Samsung'),
      ('Hoco', 'Hoco'),
      ('Sony', 'Sony'),
      ('Apple', 'Apple'),
      ('Xiaomi', 'Xiaomi'),
      ('Hwawei', 'Hwawei'),
      ('Haylo', 'Haylo'),
      ('G-tab', 'G-tab'),
      ('Haino teko', 'Haino teko'),
      ('KIESLECT', 'KIESLECT'),
      ('Google', 'Google'),
    )
   brand=models.TextField(max_length=10,choices=BRAND,default='other')
   SYSTEM=(
       ('Android','Android'),
       ('IOS','IOS'),
       ('Android , IOS','Android , IOS'),
    )
   System_compatible=models.TextField(max_length=20,choices=SYSTEM)
   water_resistance=models.BooleanField(default=False)
   Weight=models.IntegerField()
   gps=models.BooleanField(default=False)
   mem_card=models.BooleanField(default=False)
   ram=models.FloatField()
   stockage=models.FloatField()
   battery=models.IntegerField()
   wirless_charging=models.BooleanField(default=False)
   sms=models.BooleanField(default=False)
   email=models.BooleanField(default=False)
   calls=models.BooleanField(default=False)
   radio=models.BooleanField(default=False)
   wifi=models.BooleanField(default=False)
   bluetooth=models.BooleanField(default=False)
   
class SoundDevice(Device):
    BRAND = (
    ('Samsung', 'Samsung'),
    ('Hoco', 'Hoco'),
    ('Haino teko', 'Haino teko'),
    ('AWEI', 'AWEI'),
    ('Anker', 'Anker'),
    ('Beats', 'Beats'),
    ('Bose', 'Bose'),
    ('Sony', 'Sony'),
    ('Celebrat', 'Celebrat'),
    ('Apple', 'Apple'),
    ('Xiaomi', 'Xiaomi'),
    ('Hwawei', 'Hwawei'),
    ('YINDU', 'YINDU'),
    ('JBL', 'JBL'),
    ('Lenovo', 'Lenovo'),
    ('LG', 'LG'),
)
    brand=models.TextField(max_length=10,choices=BRAND,default='other')
    CATEGORY=(
        ('Headset','Headset'),
        ('Earphone','Earphone'),
        ('Speaker','Speaker'),
        ('Earpiece','Earpiece'),
        ('Microphone','Microphone'),

    )
    category=models.TextField(max_length=10,choices=CATEGORY,default='Speaker')
    bluetooth=models.BooleanField(default=False)
    wired=models.BooleanField(default=False)

class FlashDisk(Device):
    capacity=models.IntegerField()

class PowerBank(Device):
    capacity=models.IntegerField()
    NB=(
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
    )
    Nb=models.IntegerField(choices=NB,default=1)
    AM=(
        (1,'1A'),
        (1.5,'1.5 A'),
        (2,'2 A'),
        (2.5,'2.5 A'),
        (3,'3 A'),
         
    )
    Amperage=models.FloatField(choices=AM,default='1 A')

class DesiredDevice(models.Model):
    device=models.ForeignKey(Device,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    nb=models.IntegerField()

class Basket(models.Model):
   devices=models.ManyToManyField(DesiredDevice)
   price=models.IntegerField(default=0)

class Order(models.Model):
    basket=models.ForeignKey(Basket,on_delete=models.CASCADE,)
    name=models.TextField(max_length=50)
    email=models.EmailField(null=False)
    address=models.TextField(max_length=100)
   #phone=PhoneNumberField()
    treated=models.BooleanField(default=False)
    order_datetime=models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    email=models.EmailField()
    message=models.TextField(max_length=100)

from rest_framework import serializers
from .import models
from django.contrib.auth.models import User






'''
class UserSerializer(serializers.ModelSerializer):
   class Meta : 
       model = User
       fields='__all__'
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        user=UserSerializer
        fields = ['id','user','address']
    def __init__(self,*args,**kwargs):
     super(VendorSerializer,self).__init__(*args,**kwargs)


class ProductCategorySerializer(serializers.Serializer):
   class Meta:
    models=models.ProductCategory
    fields='__all__'


class ProductSerializer(serializers.Serializer):
   product_rating=serializers.PrimaryKeyRelatedField( read_only=True)
   class Meta:
     models=models.Product
     category=ProductCategorySerializer
     fields=['id','category','vendor','title','detail','price','product_rating']
     def __init__(self,*args,**kwargs):
       super(ProductSerializer,self).__init__(*args,**kwargs)       
       self.Meta.depth =1




class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields='__all__'


class OrderSerialiser(serializers.ModelSerializer):
   class Meta :
      model = models.Order
      
      fields='__all__'
      
class CustomerSerializer(serializers.ModelSerializer):
   class Meta : 
        model = models.Costumer
        fields='__all__'    
   def __init__(self,*args,**kwargs):
       super(CustomerSerializer,self).__init__(*args,**kwargs)       
       self.Meta.depth =1



class OrderSerializer(serializers.ModelSerializer):
   class Meta :
      model = models.Order
      costumer=CustomerSerializer
      fields='__all__'

class CostumerAdressSerializer(serializers.ModelSerializer):
   class Meta :
      model = models.CostumerAdress
      costumer=CustomerSerializer
      fields='__all__'
      def __init__(self,*args,**kwargs):
         super(CostumerAdressSerializer,self).__init__(*args,**kwargs)
         self.Meta.depth=1



class ProductRatingSerializer(serializers.ModelSerializer):
  
   class Meta :
      model = models.ProductRating
      costumer=CustomerSerializer
      product=ProductSerializer
      fields='__all__'
   
'''

class ColorSerializer(serializers.ModelSerializer):
   class Meta : 
       model = models.Color
       fields='__all__'

class ImageSerializer(serializers.ModelSerializer):
   class Meta : 
       model = models.Image
       fields='__all__'

class AlbumSerializer(serializers.ModelSerializer):
   class Meta : 
       album = ImageSerializer(many=True)
       model = models.Album
       fields='__all__'













class DeviceSerializer(serializers.ModelSerializer):
    tags=serializers.CharField(write_only=True)
    class Meta:
        datetime = serializers.ReadOnlyField() 
        tags = serializers.ReadOnlyField() 
        rating=serializers.ReadOnlyField() 
        tags=serializers.CharField(write_only=True)
        model = models.Device
        colors = serializers.PrimaryKeyRelatedField(queryset=models.Color.objects.all(), many=True)
        album = serializers.PrimaryKeyRelatedField(queryset=models.Album.objects.all(), required=False)
        fields=['id','name','price','material','release_date','album','cover_image','detail','colors','state','nb','discount','discount_perc','popularity','rating','date','tags','tag_list']
    def create(self, validated_data):
        color_choices = validated_data.pop('colors', [])
        album_choice = validated_data.pop('album', None)
        
        device = models.Device.objects.create(**validated_data)
        
        if album_choice:
            device.album = album_choice
        
        device.colors.set(color_choices)
        
        return device
     
    def update(self, instance, validated_data):
        color_choices = validated_data.pop('colors', instance.colors.all())
        album_choice = validated_data.pop('album', None)
        for attr, value in validated_data.items():
            if value is not None:
             setattr(instance, attr, value)
        
        if album_choice:
            instance.album = album_choice
        
        instance.colors.set(color_choices)
        instance.save()
        
        return instance
'''
class LaptopSerializer(DeviceSerializer):
   class Meta : 
       model = models.Laptop
       fields='__all__'

class DeviceSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()  # You need to define AlbumSerializer if not already defined
    class Meta:
        model = models.Device
        fields = '__all__'

'''

class LaptopSerializer(DeviceSerializer):
    class Meta(DeviceSerializer.Meta):
        model = models.Laptop
        fields= DeviceSerializer.Meta.fields+['battery','category','brand','os','processor_type','Processor','screen_size','screen_type','graphic_card','Weight','cache_mem','ram','hard_disk','hard_disk_type','wifi','bluetooth','Webcam']        
    def create(self, validated_data):
        color_choices = validated_data.pop('colors', [])
        album_choice = validated_data.pop('album', None)
        
        device = models.Laptop.objects.create(**validated_data)
        
        if album_choice:
            device.album = album_choice
        
        device.colors.set(color_choices)
        
        return device
     
    def update(self, instance, validated_data):
        color_choices = validated_data.pop('colors', instance.colors.all())
        album_choice = validated_data.pop('album', None)
        for attr, value in validated_data.items():
            if value is not None:
             setattr(instance, attr, value)
        
        if album_choice:
            instance.album = album_choice
        
        instance.colors.set(color_choices)
        instance.save()
        
        return instance
'''
class LaptopSerializer(DeviceSerializer):
    class Meta:
        colors=ColorSerializer
        model = models.Laptop
        fields = '__all__'
   
    def create(self, validated_data):
        colors_data = validated_data.pop('colors', [])
        album_data = validated_data.pop('album', None)

        laptop = models.Laptop.objects.create(**validated_data)

        for color_data in colors_data:
            # Create each color associated with the laptop
            laptop.colors.create(**color_data)

        if album_data:
            # Create the album associated with the laptop
            laptop.album.create(**album_data)

        return laptop
 '''  
class TabletSerializer(DeviceSerializer):
   class Meta : 
       model = models.Tablet
       fields=DeviceSerializer.Meta.fields +['battery','brand','System','camera','front_cam','Processor','screen_size','screen_type','Weight','cache_mem','Ram','hard_disk','usb','wifi','bluetooth','hdmi','mem_card','gps','radio','Reseau']    
   def create(self, validated_data):
        color_choices = validated_data.pop('colors', [])
        album_choice = validated_data.pop('album', None)
        
        device = models.Tablet.objects.create(**validated_data)
        
        if album_choice:
            device.album = album_choice
        
        device.colors.set(color_choices)
        
        return device
     
   def update(self, instance, validated_data):
        color_choices = validated_data.pop('colors', instance.colors.all())
        album_choice = validated_data.pop('album', None)
        for attr, value in validated_data.items():
            if value is not None:
             setattr(instance, attr, value)
        
        if album_choice:
            instance.album = album_choice
        
        instance.colors.set(color_choices)
        instance.save()
        
        return instance

class SmartPhoneSerializer(DeviceSerializer):
   class Meta : 
       model = models.SmartPhone
       fields=DeviceSerializer.Meta.fields +['battery','brand','System','camera','camera_info','front_cam','front_cam_info','Processor','screen_size','screen_type','Weight','Ram','Chipset','gpu','double_sim','sim_card_type','wifi','bluetooth','hdmi','mem_card','gps','radio','Reseau','wireless_charging'] 
   def create(self, validated_data):
        color_choices = validated_data.pop('colors', [])
        album_choice = validated_data.pop('album', None)
        
        device = models.SmartPhone.objects.create(**validated_data)
        
        if album_choice:
            device.album = album_choice
        
        device.colors.set(color_choices)
        
        return device
     
   def update(self, instance, validated_data):
        color_choices = validated_data.pop('colors', instance.colors.all())
        album_choice = validated_data.pop('album', None)
        for attr, value in validated_data.items():
            if value is not None:
             setattr(instance, attr, value)
        
        if album_choice:
            instance.album = album_choice
        
        instance.colors.set(color_choices)
        instance.save()
        
        return instance

class SmartWatchSerializer(DeviceSerializer):
   class Meta (DeviceSerializer.Meta):
       model = models.SmartWatch
       fields= DeviceSerializer.Meta.fields +['brand','System_compatible','water_resistance','Weight','gps','mem_card','ram','stockage','battery','wirless_charging','sms','email','calls','radio','wifi','bluetooth']

   def create(self, validated_data):
        color_choices = validated_data.pop('colors', [])
        album_choice = validated_data.pop('album', None)
        
        device = models.SmartWatch.objects.create(**validated_data)
        
        if album_choice:
            device.album = album_choice
        
        device.colors.set(color_choices)
        
        return device
     
   def update(self, instance, validated_data):
        color_choices = validated_data.pop('colors', instance.colors.all())
        album_choice = validated_data.pop('album', None)
        for attr, value in validated_data.items():
            if value is not None:
             setattr(instance, attr, value)
        
        if album_choice:
            instance.album = album_choice
        
        instance.colors.set(color_choices)
        instance.save()
        
        return instance

class SoundDeviceSerializer(DeviceSerializer):
   class Meta : 
       model = models.SoundDevice
       fields=DeviceSerializer.Meta.fields+['brand','category','bluetooth','wired']

   def create(self, validated_data):
        color_choices = validated_data.pop('colors', [])
        album_choice = validated_data.pop('album', None)
        
        device = models.SoundDevice.objects.create(**validated_data)
        
        if album_choice:
            device.album = album_choice
        
        device.colors.set(color_choices)
        
        return device
     
   def update(self, instance, validated_data):
        color_choices = validated_data.pop('colors', instance.colors.all())
        album_choice = validated_data.pop('album', None)
        for attr, value in validated_data.items():
            if value is not None:
             setattr(instance, attr, value)
        
        if album_choice:
            instance.album = album_choice
        
        instance.colors.set(color_choices)
        instance.save()
        
        return instance

class PowerBankSerializer(DeviceSerializer):
   class Meta : 
       model = models.PowerBank
       fields=DeviceSerializer.Meta.fields + ['capacity','Nb','Amperage']

   def create(self, validated_data):
        color_choices = validated_data.pop('colors', [])
        album_choice = validated_data.pop('album', None)
        
        device = models.PowerBank.objects.create(**validated_data)
        
        if album_choice:
            device.album = album_choice
        
        device.colors.set(color_choices)
        
        return device
     
   def update(self, instance, validated_data):
        color_choices = validated_data.pop('colors', instance.colors.all())
        album_choice = validated_data.pop('album', None)
        for attr, value in validated_data.items():
            if value is not None:
             setattr(instance, attr, value)
        
        if album_choice:
            instance.album = album_choice
        
        instance.colors.set(color_choices)
        instance.save()
        
        return instance

class FlashDiskSerializer(DeviceSerializer):
   class Meta : 
       model = models.FlashDisk
       fields=DeviceSerializer.Meta.fields + ['capacity']

   def create(self, validated_data):
        color_choices = validated_data.pop('colors', [])
        album_choice = validated_data.pop('album', None)
        
        device = models.FlashDisk.objects.create(**validated_data)
        
        if album_choice:
            device.album = album_choice
        
        device.colors.set(color_choices)
        
        return device
     
   def update(self, instance, validated_data):
        color_choices = validated_data.pop('colors', instance.colors.all())
        album_choice = validated_data.pop('album', None)
        for attr, value in validated_data.items():
            if value is not None:
             setattr(instance, attr, value)
        
        if album_choice:
            instance.album = album_choice
        
        instance.colors.set(color_choices)
        instance.save()
        
        return instance

class DesiredDeviceSerializer(serializers.ModelSerializer):
   class Meta : 
       model = models.DesiredDevice
       fields='__all__'
 
class BasketSerializer(serializers.ModelSerializer):
   class Meta : 
       model = models.Basket
       fields='__all__'
   
class OrderSerializer(serializers.ModelSerializer):
   class Meta : 
       model = models.Order
       fields='__all__'

class FeedbackSerializer(serializers.ModelSerializer):
   class Meta : 
       model = models.Feedback
       fields='__all__'


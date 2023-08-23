from django.shortcuts import render
from rest_framework import viewsets,permissions
from . import models
from . import serializers
from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
'''

class VendorViewSet(viewsets.ModelViewSet):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializer
    permission_classes=[permissions.IsAuthenticated]

class CostumerViewSet(viewsets.ModelViewSet):
    queryset=models.Costumer.objects.all()
    serializer_class=serializers.CustomerSerializer
    permission_classes=[permissions.IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset=models.Order.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.OrderSerializer
        return serializers.OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializer
    permission_classes=[permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductSerializer
    permission_classes=[permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=models.ProductCategory.objects.all()
    serializer_class=serializers.ProductCategorySerializer
    permission_classes=[permissions.IsAuthenticated]


class CostumerAddressViewSet(viewsets.ModelViewSet):
    queryset=models.CostumerAdress.objects.all()
    serializer_class=serializers.CostumerAdressSerializer
    permission_classes=[permissions.IsAuthenticated]
 
class ProductRatingViewSet(viewsets.ModelViewSet):
    queryset=models.ProductRating.objects.all()
    serializer_class=serializers.ProductRatingSerializer
    permission_classes=[permissions.IsAuthenticated]
'''



class ColorViewSet(viewsets.ModelViewSet):
    queryset=models.Color.objects.all()
    serializer_class=serializers.ColorSerializer
    permission_classes=[permissions.IsAuthenticated]

class ImageViewSet(viewsets.ModelViewSet):
    queryset=models.Image.objects.all()
    serializer_class=serializers.ImageSerializer
    permission_classes=[permissions.IsAuthenticated]

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class AlbumViewSet(viewsets.ModelViewSet):
    queryset=models.Album.objects.all()
    serializer_class=serializers.AlbumSerializer
    permission_classes=[permissions.IsAuthenticated]

class LaptopViewSet(viewsets.ModelViewSet):
    queryset=models.Laptop.objects.all()
    serializer_class=serializers.LaptopSerializer
    permission_classes=[permissions.IsAuthenticated]
    search_fields = ['name']
    filterset_fields=['name']
    #filter_backends = [DjangoFilterBackend, filters.SearchFilter]  # Add SearchFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]

class TabletViewSet(viewsets.ModelViewSet):
    queryset=models.Tablet.objects.all()
    serializer_class=serializers.TabletSerializer
    permission_classes=[permissions.IsAuthenticated]

class SmartWatchViewSet(viewsets.ModelViewSet):
    queryset=models.SmartWatch.objects.all()
    serializer_class=serializers.SmartWatchSerializer
    permission_classes=[permissions.IsAuthenticated]

class SmartPhoneViewSet(viewsets.ModelViewSet):
    queryset=models.SmartPhone.objects.all()
    serializer_class=serializers.SmartPhoneSerializer
    permission_classes=[permissions.IsAuthenticated]

class SoundDeviceViewSet(viewsets.ModelViewSet):
    queryset=models.SoundDevice.objects.all()
    serializer_class=serializers.SoundDeviceSerializer
    permission_classes=[permissions.IsAuthenticated]

class PowerBankViewSet(viewsets.ModelViewSet):
    queryset=models.PowerBank.objects.all()
    serializer_class=serializers.PowerBankSerializer
    permission_classes=[permissions.IsAuthenticated]

class FlashDiskViewSet(viewsets.ModelViewSet):
    queryset=models.FlashDisk.objects.all()
    serializer_class=serializers.FlashDiskSerializer
    permission_classes=[permissions.IsAuthenticated]

class DesiredDeviceViewSet(viewsets.ModelViewSet):
    queryset=models.DesiredDevice.objects.all()
    serializer_class=serializers.DesiredDeviceSerializer
    permission_classes=[permissions.IsAuthenticated]

class BasketViewSet(viewsets.ModelViewSet):
    queryset=models.Basket.objects.all()
    serializer_class=serializers.BasketSerializer
    permission_classes=[permissions.IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset=models.Order.objects.all()
    serializer_class=serializers.OrderSerializer
    permission_classes=[permissions.IsAuthenticated]

    
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset=models.Feedback.objects.all()
    serializer_class=serializers.FeedbackSerializer
    permission_classes=[permissions.IsAuthenticated]

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer
    search_fields = '__all__'
    filter_fields='__all__'
    permission_classes=[permissions.IsAuthenticated]
@api_view(['GET'])
def device_discount_search_view(request):
    devices = models.Device.objects.filter(discount=True).order_by('-discount_perc','-price')
    
    serializer = serializers.DeviceSerializer(devices, many=True)
    return Response({'devices': serializer.data})

@api_view(['GET'])
def device_popularity_search_view(request):
    devices = models.Device.objects.all().order_by('-popularity')
    
    if len(devices) >= 10:
        devices = devices[:10]  # Limit to the top 9 devices
    else:
        device=models.Device.objects.all().order_by('-popularity')
        
    serializer = serializers.DeviceSerializer(devices, many=True)
    return Response({'devices': serializer.data})

@api_view(['GET', 'POST'])
def laptop_general_search_view(request):
    keyword = request.data.get('keyword')
    
    devices = models.Laptop.objects.all()  # Initialize the variable
    
    if keyword:
        devices = devices.filter(
            Q(name__icontains=keyword)|
            Q(detail__icontains=keyword)|
            Q(material__icontains=keyword)|
            Q(state__icontains=keyword)|
            Q(category__icontains=keyword)|
            Q(os__icontains=keyword)|
            Q(processor_type__icontains=keyword)|
            Q(Processor__icontains=keyword)|
            Q(graphic_card__icontains=keyword)|
            Q(graphic_card_type__icontains=keyword)|
            Q(hard_disk__icontains=keyword)|
            Q(hard_sisk_type__icontains=keyword)|
            Q(brand__icontains=keyword)|
            Q(tags__icontains=keyword)


        )
    serializer = serializers.LaptopSerializer(devices, many=True)
    
    return Response({'devices': serializer.data})

@api_view(['GET', 'POST'])
def tablet_general_search_view(request):
    keyword = request.data.get('keyword')
    
    devices = models.Tablet.objects.all()  # Initialize the variable
    
    if keyword:
        devices = devices.filter(
            Q(name__icontains=keyword)|
            Q(material__icontains=keyword)|

            Q(detail__icontains=keyword)|
            Q(state__icontains=keyword)|
            Q(brand__icontains=keyword)|
            Q(System__icontains=keyword)|
            Q(Processor__icontains=keyword)|
            Q(screen_type__icontains=keyword)|
            Q(tags__icontains=keyword)|
            Q(graphic_card__icontains=keyword)
        )
    serializer = serializers.TabletSerializer(devices, many=True)
    
    return Response({'devices': serializer.data})

@api_view(['GET', 'POST'])
def smartphone_general_search_view(request):
    keyword = request.data.get('keyword')
    
    devices = models.SmartPhone.objects.all()  # Initialize the variable
    
    if keyword:
        devices = devices.filter(
            Q(name__icontains=keyword)|
            Q(detail__icontains=keyword)|
            Q(material__icontains=keyword)|
            Q(state__icontains=keyword)|
            Q(brand__icontains=keyword)|
            Q(System__icontains=keyword)|
            Q(camera_info__icontains=keyword)|
            Q(screen_type__icontains=keyword)|
            Q(gpu__icontains=keyword)|
            Q(tags__icontains=keyword)|
            Q(sim_card_type__icontains=keyword)|
            Q(Chipset__icontains=keyword)
        )
    serializer = serializers.SmartPhoneSerializer(devices, many=True)

@api_view(['GET', 'POST'])
def smartwatch_general_search_view(request):

    keyword = request.data.get('keyword')
    
    devices = models.SmartWatch.objects.all()  # Initialize the variable
    
    if keyword:
        devices = devices.filter(
            Q(name__icontains=keyword)|
            Q(detail__icontains=keyword)|
            Q(material__icontains=keyword)|
            Q(state__icontains=keyword)|
            Q(tags__icontains=keyword)| 
            Q(brand__icontains=keyword)|
            Q(System_compatible__icontains=keyword)
        )
    serializer = serializers.SmartWatchSerializer(devices, many=True)

@api_view(['GET', 'POST'])
def sounddevice_general_search_view(request):
    keyword = request.data.get('keyword')
    
    devices = models.SoundDevice.objects.all()  # Initialize the variable
    
    if keyword:
        devices = devices.filter(
            Q(name__icontains=keyword)|
            Q(detail__icontains=keyword)|
            Q(tags__icontains=keyword)|
            Q(state__icontains=keyword)|
            Q(brand__icontains=keyword)|
            Q(category__icontains=keyword)
        )
    serializer = serializers.SoundDeviceSerializer(devices, many=True)

@api_view(['GET', 'POST'])
def flashdisk_general_search_view(request):
    keyword = request.data.get('keyword')
    
    devices = models.FlashDisk.objects.all()  # Initialize the variable
    
    if keyword:
        devices = devices.filter(
            Q(name__icontains=keyword)|
            Q(material__icontains=keyword)|

            Q(detail__icontains=keyword)|
            Q(tags__icontains=keyword)|
            Q(state__icontains=keyword)

        )
    serializer = serializers.FlashDiskSerializer(devices, many=True)


@api_view(['GET', 'POST'])
def powerbank_general_search_view(request):
    keyword = request.data.get('keyword')
    
    devices = models.PowerBank.objects.all()  # Initialize the variable
    
    if keyword:
        devices = devices.filter(
            Q(name__icontains=keyword)|
            Q(detail__icontains=keyword)|
            Q(material__icontains=keyword)|

            Q(tags__icontains=keyword)|
            Q(state__icontains=keyword)

        )
    serializer = serializers.PowerBankSerializer(devices, many=True)

@api_view(['GET', 'POST'])
def laptop_search_range_view(request):
    devices=models.Laptop.objects.all()
    name=request.data.get('name')
    brand=request.data.get('brand')
    min_price = request.data.get('min_price')
    max_price = request.data.get('max_price')
    state=request.data.get('state')
    category=request.data.get('category')
    processor_type=request.data.get('processor_type')
    smin=request.data.get('smin')
    smax=request.data.get('smax')
    rammin=request.data.get('rammin')
    rammax=request.data.get('rammax')
    diskmin=request.data.get('diskmin')
    diskmax=request.data.get('diskmax')
    weightmin=request.data.get('weightmin')
    weightmax=request.data.get('weightmax')
    if name:
     devices = devices.filter(name__icontains=name)
    if brand:
     
     devices=devices.filter(brand__icontains=brand)
    if state:
     devices=devices.filter(state=state)
    if category:
     devices=devices.filter(category=category)
    if processor_type:
     devices=devices.filter(processor_type=processor_type)

    if min_price is not None and max_price is not None:
        devices = devices.filter(price__range=(min_price, max_price))
    if smin is not None and smax is not None:
        devices = devices.filter(screen_size__range=(smin, smax))
    if rammin is not None and rammax is not None:
        devices = devices.filter(ram__range=(rammin, rammax))
    if diskmin is not None and diskmax is not None:
        devices = devices.filter(hard_disk__range=(diskmin, diskmax))
    if weightmin is not None and weightmax is not None:
        devices = devices.filter(Weight__range=(weightmin, weightmax))
    serializer = serializers.LaptopSerializer(devices, many=True) 

    return Response({'devices': serializer.data})

@api_view(['GET', 'POST'])
def tablet_search_range_view(request):
    devices=models.Tablet.objects.all()
    name=request.data.get('name')
    brand=request.data.get('brand')
    min_price = request.data.get('min_price')
    max_price = request.data.get('max_price')
    state=request.data.get('state')
    system=request.data.get('system')
    smin=request.data.get('smin')
    smax=request.data.get('smax')
    cammin=request.data.get('cammin')
    cammax=request.data.get('cammax')
    fcmin=request.data.get('fcmin')
    fcmax=request.data.get('fcmax')
    rammin=request.data.get('rammin')
    rammax=request.data.get('rammax')
    diskmin=request.data.get('diskmin')
    diskmax=request.data.get('diskmax')
    weightmin=request.data.get('weightmin')
    weightmax=request.data.get('weightmax')
    reseau=request.data.get('reseau')
    if name:
     devices = devices.filter(name__icontains=name)
    if brand:
     devices=devices.filter(brand__icontains=brand)
    if state:
     devices=devices.filter(state=state)
    if system:
     devices=devices.filter(System__icontains=system)
    if reseau:
     devices=devices.filter(reseau=reseau)
    
    if min_price is not None and max_price is not None:
        devices = devices.filter(price__range=(min_price, max_price))
    if smin is not None and smax is not None:
        devices = devices.filter(screen_size__range=(smin, smax))
    if rammin is not None and rammax is not None:
        devices = devices.filter(Ram__range=(rammin, rammax))
    if diskmin is not None and diskmax is not None:
        devices = devices.filter(hard_disk__range=(diskmin, diskmax))
    if cammin is not None and cammax is not None:
        devices = devices.filter(camera__range=(cammin, cammax))
    if fcmin is not None and fcmax is not None:
        devices = devices.filter(front_cam__range=(fcmin, fcmax))
    if weightmin is not None and weightmax is not None:
        devices = devices.filter(Weight__range=(weightmin, weightmax))
    serializer = serializers.TabletSerializer(devices, many=True)


    return Response({'devices': serializer.data})

@api_view(['GET', 'POST'])
def smartwatch_search_range_view(request):
    devices= models.SmartWatch.objects.all()
    name=request.data.get('name')
    brand=request.data.get('brand')
    min_price = request.data.get('min_price')
    max_price = request.data.get('max_price')
    state=request.data.get('state')
    system=request.data.get('system')
    weightmin=request.data.get('weightmin')
    weightmax=request.data.get('weightmax')
    if name :
     devices = devices.filter(name__icontains=name)
    if brand :
     devices=devices.filter(brand__icontains=brand)
    if state :
     devices=devices.filter(state=state)
    if system:
      devices=devices.filter(System_compatible__icontains=system)

    
    if min_price is not None and max_price is not None:
        devices = devices.filter(price__range=(min_price, max_price))
    if weightmin is not None and weightmax is not None:
        devices = devices.filter(Weight__range=(weightmin, weightmax))
    serializer = serializers.SmartWatchSerializer(devices, many=True)

    return Response({'devices': serializer.data})

@api_view(['GET', 'POST'])
def smartphone_search_range_view(request):
    devices=models.SmartPhone.objects.all()
    name=request.data.get('name')
    brand=request.data.get('brand')
    min_price = request.data.get('min_price')
    max_price = request.data.get('max_price')
    state=request.data.get('state')
    system=request.data.get('system')
    gpu=request.data.get('gpu')
    smin=request.data.get('smin')
    smax=request.data.get('smax')
    cammin=request.data.get('cammin')
    cammax=request.data.get('cammax')
    fcmin=request.data.get('fcmin')
    fcmax=request.data.get('fcmax')
    rammin=request.data.get('rammin')
    rammax=request.data.get('rammax')
    diskmin=request.data.get('diskmin')
    diskmax=request.data.get('diskmax')
    weightmin=request.data.get('weightmin')
    weightmax=request.data.get('weightmax')
    reseau=request.data.get('reseau')
    processor=request.data.get('processor')
    double_sim=request.data.get('double_sim')
    if name:
     devices = devices.filter(name__icontains=name)
    if brand:
     devices= devices.filter(brand__icontains=brand)
    if state:
     devices=devices.filter(state=state)
    if system:
     devices=devices.filter(System__icontains=system)
    if gpu :
     devices =devices.filter(gpu__icontains=gpu)
    if processor :
      devices=devices.filter(Processor__icontains=processor)
    if double_sim:
      devices=devices.filter(double_sim__icontains=double_sim)
    if reseau :
      devices=devices.filter(reseau=reseau)
    
    
    if min_price is not None and max_price is not None:
        devices = devices.filter(price__range=(min_price, max_price))
    if smin is not None and smax is not None:
        devices = devices.filter(screen_size__range=(smin, smax))
    if rammin is not None and rammax is not None:
        devices = devices.filter(Ram__range=(rammin, rammax))
    if diskmin is not None and diskmax is not None:
        devices = devices.filter(hard_disk__range=(diskmin, diskmax))
    if cammin is not None and cammax is not None:
        devices = devices.filter(camera__range=(cammin, cammax))
    if fcmin is not None and fcmax is not None:
        devices = devices.filter(front_cam__range=(fcmin, fcmax))
    if weightmin is not None and weightmax is not None:
        devices = devices.filter(Weight__range=(weightmin, weightmax))
    serializer = serializers.SmartPhoneSerializer(devices, many=True)
    return Response({'devices': serializer.data})
    
@api_view(['GET', 'POST'])
def flashdisk_search_range_view(request):
    devices=models.FlashDisk.objects.all()
    name=request.data.get('name')
    min_price = request.data.get('min_price')
    max_price = request.data.get('max_price')
    state=request.data.get('state')
    if name:
     devices = devices.filter(name__icontains=name)
    if state:
     devices=devices.filter(state=state)


    if min_price is not None and max_price is not None:
        devices = devices.filter(price__range=(min_price, max_price))
    serializer = serializers.FlashDiskSerializer(devices, many=True)
    return Response({'devices': serializer.data})

@api_view(['GET', 'POST'])
def sounddevice_search_range_view(request):
    devices=models.SoundDevice.objects.all()
    name=request.data.get('name')
    min_price = request.data.get('min_price')
    max_price = request.data.get('max_price')
    state=request.data.get('state')
    brand=request.data.get('brand')
    category=request.data.get('category')
    if name:
      devices = devices.filter(name__icontains=name)
    if brand:
      devices=devices.filter(brand=brand)
    if category:
      devices=devices.filter(category=category)
    if state:
      devices=devices.filter(state=state)
    if min_price is not None and max_price is not None:
        devices = devices.filter(price__range=(min_price, max_price))
    serializer = serializers.SoundDeviceSerializer(devices, many=True)
    return Response({'devices': serializer.data})

@api_view(['GET', 'POST'])
def powerbank_search_range_view(request):
    devices=models.PowerBank.objects.all()
    name=request.data.get('name')
    min_price = request.data.get('min_price')
    max_price = request.data.get('max_price')
    state=request.data.get('state')
    if name :
      devices = devices.filter(name__icontains=name)
 
    if state :
       devices=devices.filter(state=state)
    

    if min_price is not None and max_price is not None:
        devices = devices.filter(price__range=(min_price, max_price))
    serializer = serializers.PowerBankSerializer(devices, many=True)
    return Response({'devices': serializer.data})
    
    
@api_view(['POST'])
def rating(request, id):
    rating = request.data.get('rating')
    device = models.Device.objects.get(id=id)
    if device.rtnb == 0:
        device.rtnb = 1
        device.rating = rating
    else:
        device.rtnb = device.rtnb + 1
        device.rating = (device.rating * (device.rtnb - 1) + rating) / device.rtnb
    device.save()
    return Response({'message': 'Rating updated successfully'})

@api_view(['POST'])
def confirm_order(request,id):
   order=models.Order.objects.get(id=id)
   if order :
      basket=order.basket
      devices=basket.devices.all()
      for d in devices :
         if d :
             device=d.device
             device.popularity=device.popularity + d.nb
             device.nb=device.nb + d.nb
        
   order.delete
   return Response('confirmed successfully')

                
   
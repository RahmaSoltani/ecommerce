"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
http post http://127.0.0.1:8000/api/token/ username=thinkpad54 password=rahima
 http  http://127.0.0.1:8000/api/vendor/  "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxNzQ0OTA0LCJpYXQiOjE2OTE3NDM5MzksImp0aSI6ImFjNDA2ZGU1Y2Q3ZjQwNmNiNzI5ZTVhNmU5ZTMxNGNjIiwidXNlcl9pZCI6MX0.pIvhxMJeoc4OWxGXScKrkYqLam1w16eYtmZqvcUq5g0"
{
      "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxNzQ0MjM5LCJpYXQiOjE2OTE3NDM5MzksImp0aSI6IjVkMmE2OTY0NTFlNjQ3YmFiN2Q3M2M2ODIxODk3MTkzIiwidXNlcl9pZCI6MX0.fcgZlegAvxVcSMyuCGtIqQgPJ8wfHQ83qLWXuMlwBh4",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MTgzMDMzOSwiaWF0IjoxNjkxNzQzOTM5LCJqdGkiOiJjNWM2ZmZlYTc4ZGY0MzEwYjc5ZmViZjMyMDFmZWIzMyIsInVzZXJfaWQiOjF9.05nhZU3UswmwMBIjlvAhAV6HmtCypDtbO4SNsrC5-HQ"  
}
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('myapp.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
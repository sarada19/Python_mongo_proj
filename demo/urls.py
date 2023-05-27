from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo-app/api-endpoint/',include('demoapp.api.urls')),
    path('demo-app/',include('demoapp.urls')),    
]

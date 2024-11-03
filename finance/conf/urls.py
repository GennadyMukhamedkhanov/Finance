from django.contrib import admin
from django.urls import include
from django.urls import path

from conf.yasg import urlpatterns as yasg_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

urlpatterns += yasg_url

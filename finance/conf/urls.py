from conf.yasg import urlpatterns as yasg_url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]

urlpatterns += yasg_url

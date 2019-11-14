
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from FirstApp import views
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'FirstApp/(\d+)/',views.pet_detail,name='pet_detail'),
]

from django.contrib import admin
from django.conf.urls import url, include
from home import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.home_page, name='home'),
]

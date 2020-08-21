from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.cv_view, name='cv_view'),
]
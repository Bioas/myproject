
from django.urls import path
from .views import contact, custom, download_config, index,home, setting_congig,start,download,recommend
from webs import views
from webs.control import Delete 

urlpatterns = [
    path('',index,name='index'),
    path('input/',views.input,name='input'),
    path('home/',home),
    path('start/',start,name='start'),
    path('download',download,name='dowloand'),
    path('dowload_config',download_config,name='dowload_config'),
    path('contact',contact,name='contact'),
    path('delete',Delete.Delete,name='delete'),
    path('recommend',recommend,name='recommend'),
    path('input_csv/',views.input_csv,name='input_csv'),
    path('custom',custom,name='custom'),
    path('setting_config',setting_congig,name='setting_config'),
    path('upload_csv/',views.upload_csv,name='upload_csv'),
   
]
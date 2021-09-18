
from django.urls import path
from .views import manual, custom, download_config, index,home, setting_congig,start,download,recommend,downloadrecom
from webs import views
from webs.control import Delete 
from webs.control import DeleteCustom
from webs.control import DeleteRecom


urlpatterns = [
    path('',index,name='index'),
    path('input/',views.input,name='input'),
    path('home/',home),
    path('start/',start,name='start'),
    path('download',download,name='dowloand'),
    path('downloadrecom',downloadrecom,name='dowloandrecom'),
    path('dowload_config',download_config,name='dowload_config'),
    path('manual',manual,name='manual'),
    path('delete',Delete.Delete,name='delete'),
    path('deletecustom',DeleteCustom.DeleteCustom,name='deletecustom'),
    path('deleterecom',DeleteRecom.DeleteRecom,name='deleterecom'),
    path('recommend',recommend,name='recommend'),
    path('input_csv/',views.input_csv,name='input_csv'),
    path('custom',custom,name='custom'),
    path('setting_config',setting_congig,name='setting_config'),
    path('upload_csv/',views.upload_csv,name='upload_csv'),
   
]
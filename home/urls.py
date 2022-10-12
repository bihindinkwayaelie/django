import imp 
from xml.dom.minidom import Document
from django.urls import path
from .import views                      
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='welcome'),
    path('about/',views.about, name='about'),
    path('indiba/',views.indiba, name='indiba'),
    path('more/',views.more, name='more'),
    path('register/',views.register, name='register'),
    path('idaussd/', views.idaussd, name='idaussd'),
    path('delete/<int:id>',views.deletedata, name='delete'),
    path('deleteart/<int:id>',views.deleteart, name='deleteart'),
    path('edit/<int:id>',views.edit, name='edit')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

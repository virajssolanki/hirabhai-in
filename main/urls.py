from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('s_upload/<pk>', views.simple_upload, name='upload'),
    path('l_upload/<pk>', views.l_upload, name='l_upload'),
    path('square_with_small_image/<pk>', views.square_with_small_image, name='square_with_small_image'),
    path('vertical/<pk>', views.vertical_image, name='vertical_image'),
    
]
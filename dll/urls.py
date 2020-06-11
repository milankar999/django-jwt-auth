from django.urls import path
from .views import *
from dll import views

urlpatterns = [
    path('get_data/',views.test.as_view(),name='generate-quotation-list'),
    path('get_data2/',views.test2.as_view(),name='generate-quotation-list2'),
    path('get_data3/',retest1,name='generate-quotation-list1'),
    path('get_data4/',retest2,name='generate-quotation-list2'),
]
from django.urls import path
from .views import *
import django.urls import path
import requests import delete
from .views import *
urlpatterns = [

    path('', accounts_list, name='accounts_list'),
    path('Add/', account_create, name='account_create'),
    path('Update/<int:id>', account_update, name='account_update' ),
    path('Delete/<int:id>', account_delete, name='account_delete' ),
    path('Info/<int:id>', account_info, name='account_info')
]

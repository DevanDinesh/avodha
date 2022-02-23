from django.urls import path
from . import views
urlpatterns=[
    path('',views.demo,name='demo'),
    path('shop/<int:shop_id>',views.detail,name='detail')
]
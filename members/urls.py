from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.member_list, name='list'),
    path('create/', views.member_create, name='create'),
    path('provinces/', views.load_provinces, name='load_provinces'),
    path('municipalities/', views.load_municipalities, name='load_municipalities'),
    path('barangays/', views.load_barangays, name='load_barangays'),
]

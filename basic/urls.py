from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('state', views.get_state_data, name='data'),
    path('layout', views.layout, name='layout_test'),
]
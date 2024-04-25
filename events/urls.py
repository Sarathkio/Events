from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('brochure/<int:pk>/', views.brochure_detail, name='brochure_detail'),
]

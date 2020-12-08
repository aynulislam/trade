from django.urls import path
from store import views

urlpatterns = [
    path('', views.StoreDashboardView.as_view(),name='storeDashboardView' ),
]
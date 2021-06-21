from django.urls import path
from . import api_views

urlpatterns = [
    path('items/', api_views.ItemListAPIView.as_view(), name='items-api')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="product-main"),
    path('<int:game_id>', views.game_items, name='game-items')
]
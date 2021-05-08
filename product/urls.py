from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="product-main"),
    path('<int:game_id>', views.game_items, name='game-items'),
    path('<int:game_id>/<str:seller_name>', views.sellers_item, name='sellers-item'),
    path('item/<int:item_id>', views.item_main, name='item-main'),
    path('item/<int:item_id>/order', views.item_order, name='item-order')

]
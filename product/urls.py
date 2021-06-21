from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="product-main"),
    path('<int:game_id>', views.game_items, name='game-items'),

    path('item/<int:item_id>', views.item_main, name='item-main'),
    path('item/<int:item_id>/order', views.item_order, name='item-order'),
    path('purchases', views.purchases, name='purchases'),
    path('sell', views.sell_form, name='sell-form'),
    path('accounts', views.seller_accounts, name='seller-accounts'),
    path('item/<int:item_id>/edit', views.acc_edit, name='acc-edit'),
    path('item/<int:item_id>/delete', views.acc_delete, name='acc-delete'),
    path('add-game', views.add_game, name='add-game'),
    path('<int:game_id>/edit', views.game_edit, name='game-edit'),
    path('<int:game_id>/delete', views.game_delete, name='game-delete'),
    path('<int:game_id>/<str:seller_name>', views.sellers_item, name='sellers-item'),
]

from django.shortcuts import render, redirect
from .models import Game, Item
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def main(request):
    if request.method == 'GET':
        search_string = request.GET.get('search', '')
        games = Game.objects.all().filter(name__contains=search_string)
    else:
        games = Game.objects.all()

    context = {
        'title': 'Main Page',
        'search_text': 'Search by games',
        'games': games
    }
    return render(request, 'product/main.html', context)


def game_items(request, game_id):
    game = Game.objects.filter(id=game_id).first()
    if request.method == 'GET':
        search_string = request.GET.get('search', '')
        items = Item.objects.all().filter(game=game_id, description__contains=search_string, sold=False)
    else:
        items = Item.objects.all().filter(game=game_id)
    context = {
        'title': game.name,
        'search_text': 'Search by description',
        'items': items
    }

    return render(request, 'product/game.html', context)


def sellers_item(request, game_id, seller_name):
    game = Game.objects.filter(id=game_id).first()
    context = {
        'title': game.name,
        'items': Item.objects.all().filter(game=game_id, seller=seller_name, sold=False)
    }
    return render(request, 'product/game.html', context)


def item_main(request, item_id):
    context = {
        'title': 'Item',
        'item': Item.objects.filter(id=item_id).first()
    }
    return render(request, 'product/item_main.html', context)


@login_required
def item_order(request, item_id):
    context = {
        'title': 'Order',
        'item': Item.objects.filter(id=item_id).first()
    }
    if request.method == 'POST':
        payment_code = request.POST.get('payment_code', '')
        if payment_code == '123':
            item = Item.objects.filter(id=item_id).first()
            item.sold = True
            item.owner = request.user
            item.save()
            messages.success(request, 'Your payment has been processed successfully. '
                                      'Please check your purchased list.')
            return redirect('product-main')
        else:
            messages.warning(request, 'Oops! Something went wrong with payment. Please try to check out again.')
            return redirect('product-main')
    else:
        return render(request, 'product/item_order.html', context)


def purchases(request):
    items = Item.objects.all().filter(owner=request.user)
    context = {
        'title': 'My List',
        'items': items
    }
    return render(request, 'product/purchases.html', context)

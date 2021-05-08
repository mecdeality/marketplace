from django.shortcuts import render
from .models import Game, Item
from django.http import HttpResponse


def main(request):
    if request.method == 'POST':
        # return HttpResponse('dadw')
        search_string = request.POST.get('search', '')
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
    if request.method == 'POST':
        search_string = request.POST.get('search', '')
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


def item_order(request, item_id):
    context = {
        'title': 'Order',
        'item': Item.objects.filter(id=item_id).first()
    }
    return render(request, 'product/item_order.html', context)

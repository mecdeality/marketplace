from django.shortcuts import render
from .models import Game, Item
from django.http import HttpResponse


def main(request):
    context = {
        'title': 'Main Page',
        'games': Game.objects.all()
    }
    return render(request, 'product/main.html', context)


def game_items(request, game_id):
    game = Game.objects.filter(id=game_id).first()
    context = {
        'title': game.name,
        'items': Item.objects.all().filter(game=game_id)
    }
    return render(request, 'product/game.html', context)

from django.shortcuts import render, redirect
from .models import Game, Item, Comment
from user.models import UserStatus
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def main(request):
    if request.method == 'GET':
        search_string = request.GET.get('search', '')
        games = Game.objects.all().filter(name__contains=search_string)
    else:
        games = Game.objects.all()

    if request.user.is_authenticated:
        is_seller = UserStatus.objects.filter(user=request.user).first().is_seller
    else:
        is_seller = False
    context = {
        'title': 'Main Page',
        'search_text': 'Search by games',
        'games': games,
        'is_seller': is_seller
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
    user = User.objects.filter(username=seller_name).first()
    seller = UserStatus.objects.filter(user=user).first()
    context = {
        'title': game.name,
        'items': Item.objects.all().filter(game=game_id, seller=seller, sold=False)
    }
    return render(request, 'product/game.html', context)


def item_main(request, item_id):
    item = Item.objects.filter(id=item_id).first()
    # seller = UserStatus.objects.filter(user=request.user).first()
    if request.method == 'POST':
        com = request.POST.get('comment')
        comment = Comment(seller=item.seller, user=request.user, content=com)
        comment.save()

    comments = Comment.objects.filter(seller=item.seller).order_by('-timestamp')
    context = {
        'title': 'Item',
        'item': item,
        'comments': comments
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


@login_required
def sell_form(request):
    if request.method == 'POST':
        desc = request.POST.get('description')
        detailed = request.POST.get('detailed')
        price = request.POST.get('price')
        game = Game.objects.filter(id=request.POST.get('game')).first()
        login = request.POST.get('item_login')
        password = request.POST.get('item_password')
        user = UserStatus.objects.filter(user=request.user).first()
        acc = Item(description=desc, detailed_description=detailed, price=price, game=game, item_login=login,
                   item_password=password, seller=user)
        acc.save()
        messages.success(request, 'Account published successfully!')
        return redirect('product-main')
    context = {
        'title': 'Sell Form',
        'games': Game.objects.all()
    }
    return render(request, 'product/sell_form.html', context)


@login_required
def seller_accounts(request):
    seller = UserStatus.objects.filter(user=request.user).first()
    items = Item.objects.all().filter(seller=seller)
    context = {
        'title': 'My List',
        'items': items
    }
    return render(request, 'product/seller_accounts.html', context)


@login_required
def acc_edit(request, item_id):
    item = Item.objects.filter(id=item_id).first()
    if request.method == 'POST':
        item.description = request.POST.get('description')
        item.detailed_description = request.POST.get('detailed')
        item.price = request.POST.get('price')
        item.game = Game.objects.filter(id=request.POST.get('game')).first()
        item.item_login = request.POST.get('item_login')
        item.item_password = request.POST.get('item_password')
        item.save()
        messages.success(request, 'Account edited successfully!')
        return redirect('item-main', item_id=item_id)
    context = {
        'title': 'Edit item',
        'games': Game.objects.exclude(id=item.game.id),
        'item': item
    }
    return render(request, 'product/acc_edit.html', context)


@login_required
def acc_delete(request, item_id):
    item = Item.objects.filter(id=item_id).first()
    if request.method == 'GET':
        if 'yes' in request.GET:
            item.delete()
            messages.success(request, 'Account successfully deleted!')
            return redirect('seller-accounts')
        elif 'no' in request.GET:
            return redirect('seller-accounts')
    context = {
        'title': 'Delete item',
        'item': item
    }
    return render(request, 'product/acc_delete.html', context)


def add_game(request):
    if request.method == 'POST' and 'add' in request.POST:
        name = request.POST.get('gname')
        pic = request.FILES.get('game_pic')

        g = Game.objects.create(
            name=name,
            picture_url=pic,
        )
        messages.success(request, 'Game added successfully!')
        return redirect('product-main')
    return render(request, 'product/add_game.html')


def game_edit(request, game_id):
    game = Game.objects.filter(id=game_id).first()
    if request.method == 'POST' and 'edit' in request.POST:
        name = request.POST.get('gname')
        pic = request.FILES.get('game_pic')

        game.name = name
        if pic is not None:
            game.picture_url = pic
        game.save()
        messages.success(request, 'Game edited successfully!')
        return redirect('product-main')
    context = {
        'title': 'Game edit',
        'game': game
    }

    return render(request, 'product/edit_game.html', context)


def game_delete(request, game_id):
    game = Game.objects.filter(id=game_id).first()
    if request.method == 'GET':
        if 'yes' in request.GET:
            game.delete()
            messages.success(request, 'Game deleted successfully!')
            return redirect('product-main')
        elif 'no' in request.GET:
            return redirect('product-main')
    context = {
        'title': 'Game deletion',
        'game': game
    }
    return render(request, 'product/delete_game.html', context)

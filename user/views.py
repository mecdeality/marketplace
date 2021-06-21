from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from .models import UserStatus
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('user-login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/registration.html', {'form': form})


@login_required
def sellerRequest(request):
    if request.method == 'POST':
        status = UserStatus.objects.filter(user=request.user).first()
        status.send_request = True
        status.save()
        messages.success(request, 'Your request has been successfully sent to the administrations!')
        return redirect('product-main')
    return render(request, 'user/send_request.html')


@login_required
def checkRequest(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id', '')
        user = UserStatus.objects.filter(user=user_id).first()
        if 'accept' in request.POST:
            user.is_seller = True
            user.send_request = False
        elif 'deny' in request.POST:
            user.send_request = False
        user.save()

    context = {
        'users': UserStatus.objects.filter(send_request=True),
    }

    return render(request, 'user/check_request.html', context)

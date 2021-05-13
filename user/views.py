from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


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



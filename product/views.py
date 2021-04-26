from django.shortcuts import render


def main(request):
    return render(request, 'product/main.html', {'title': 'Main Page'})

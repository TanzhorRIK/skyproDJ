from django.shortcuts import render
from catalog.models import Product

CARDS = Product.objects.all()


def index(request):
    return render(request, 'main/index.html', {'cards': CARDS})


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(name, phone, message)

    return render(request, 'main/contacts.html')


def card(request):
    return render(request, 'main/card.html', {'cards': CARDS})

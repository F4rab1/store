from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
    query_set = Product.objects.all()[5:10]

    return render(request, 'hello.html', {'name': 'Farabi', 'products': list(query_set)})

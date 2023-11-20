from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Value, F, Func, Count
from django.db.models.functions import Concat
from django.db import transaction
from store.models import Customer, Product, Collection, Address
from tags.models import TaggedItem


def say_hello(request):
    Collection.objects.filter(pk=11).update(featured_product=1)

    return render(request, 'hello.html', {'name': 'Farabi'})
 
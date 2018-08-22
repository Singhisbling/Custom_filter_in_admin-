from django.shortcuts import render
from.models import *
from django.http import HttpResponseRedirect
from django.conf.urls import url

# Create your views here.
# def search(request):
#     item = request.GET.get('q')
#     print(item)
#     return HttpResponseRedirect('/?q={}/&'.format(item))

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def all_users(reques):
    return HttpResponse('Return all users')
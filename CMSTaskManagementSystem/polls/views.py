from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello lets start a cms project!")
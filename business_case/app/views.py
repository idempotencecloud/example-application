from django.shortcuts import render
#from django.core import serializers

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def idempotenceAuthenticator(request):
    if(not request.user.is_authenticated):
        return JsonResponse({
            'authenticated': False
        })
    #https://en.wikipedia.org/wiki/ISO_8601
    #print(serializers.serialize("json", [request.user]))
    return JsonResponse({
        'legalName': "{} {}".format(request.user.first_name, request.user.last_name),
        'authenticationTimestamp': request.user.last_login,
        'userIdentifer': request.user.pk,
        'authenticated': True
    })
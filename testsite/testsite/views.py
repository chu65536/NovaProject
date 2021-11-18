from django.http import HttpResponse
from .request import amocrm_request
import os


def req(request):
    name = request.GET['name']
    phone = request.GET['phone']
    email = request.GET['email']

    amocrm_request(name, phone, email)

    return HttpResponse('requesting...')


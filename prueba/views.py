from django.shortcuts import render, redirect, render_to_response
import conekta
from django.http import HttpResponse

from prueba.models import Sale
def prueba(request):
    sale = Sale()
    token_id = "tok_test_visa_4242"
    return HttpResponse(sale.charge(300, token_id))
# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json


def fizzbuzz(request, number):
    word = ''
    if not number % 3:
        word += 'Fizz'
    if not number % 5:
        word += 'Buzz'
    response = json.dumps({'answer': word or str(number)})
    return HttpResponse(response, content_type='application/json')

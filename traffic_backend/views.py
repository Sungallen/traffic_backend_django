import json 
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token

# Create your views here.
@ensure_csrf_cookie
def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set', 'cookie': get_token(request)})
    response['X-CSRFToken'] = get_token(request)
    print(response)
    return response

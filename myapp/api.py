from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
"""from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie"""
from . import models

def index(request):
    return render(request, 'index.html')
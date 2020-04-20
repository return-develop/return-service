from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import json, hashlib, time
from django.conf import settings

@ensure_csrf_cookie
def user_login(request):
    return render(request, 'user_login.html')
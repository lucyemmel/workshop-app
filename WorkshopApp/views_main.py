from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def hello_world(request):
    return render(request, 'overview.html')

import re
import sqlite3

from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from WorkshopApp.models import Plant


@require_http_methods(['GET', 'POST'])
def sqli(request):
    own_url = '/sqli/fixed'
    if request.method == 'GET':
        context = {'own_url': own_url}
        return render(request, "sqli.html", context=context)
    else:
        plant_name = request.POST.get('plant', 'Tulip')
        with sqlite3.connect('db.sqlite3') as conn:
            query = "SELECT * FROM WorkshopApp_Plant WHERE name= ?;"
            plants = conn.execute(query, (plant_name,)).fetchall()

            # convert to Django model type
            plants = list(map(lambda db_plant: Plant(name=db_plant[1], age=db_plant[2]), plants))

        # simple django solution
        # plants = Plant.objects.filter(name=plant_name)
        context = {'own_url': own_url, 'plants': plants}
        if not plants:
            messages.info(request, 'No plants found for this name.')
        return render(request, "sqli.html", context=context)


@require_http_methods(['GET', 'POST'])
def xss(request):
    own_url = '/xss/fixed'
    if request.method == 'GET':
        context = {'own_url': own_url}
        return render(request, "xss.html", context=context)
    else:
        message = request.POST.get('message', 'No message given')
        if not re.match(r'^([a-z]|[A-Z]|[0-9]|[?!., ])*$', message):
            message = 'Invalid message format'
        context = {'message': message, 'own_url': own_url}
        return render(request, "xss.html", context=context)


@require_http_methods(['GET', 'POST'])
def request_forgery(request):
    if request.method == 'POST':
        donation = request.POST.get('donation', -1)
        if not donation.isdigit() or int(donation) <= 0:
            messages.warning(request, 'Invalid donation!')
        else:
            messages.info(request, 'Thank you for the donation!')

    return render(request, 'forgery.html')

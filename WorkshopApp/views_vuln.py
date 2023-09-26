import sqlite3

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from WorkshopApp.models import Plant
from django.contrib import messages


@require_http_methods(['GET', 'POST'])
def sqli(request):
    own_url = '/sqli'
    if request.method == 'GET':
        context = {'own_url': own_url}
        return render(request, "sqli.html", context=context)
    else:
        plant_name = request.POST.get('plant', 'Tulip')
        with sqlite3.connect('db.sqlite3') as conn:
            query = f"SELECT * FROM WorkshopApp_Plant WHERE name='{plant_name}';"
            plants = conn.execute(query).fetchall()

            # convert to Django model type
            plants = list(map(lambda db_plant: Plant(name=db_plant[1], age=db_plant[2]), plants))

        context = {'own_url': own_url, 'plants': plants}
        if not plants:
            messages.info(request,'No plants found for this name.')
        return render(request, "sqli.html", context=context)


@require_http_methods(['GET', 'POST'])
def xss(request):
    own_url = '/xss'
    if request.method == 'GET':
        context = {'own_url': own_url}
        return render(request, "xss.html", context=context)
    else:
        message = request.POST.get('message', 'No message given')
        context = {'message': message, 'own_url': own_url}
        return render(request, "xss.html", context=context)



@require_http_methods(['GET', 'POST'])
def request_forgery(request):
    if request.method == 'POST':
        messages.info(request, 'Thank you for the donation!')
    return render(request, 'forgery.html')

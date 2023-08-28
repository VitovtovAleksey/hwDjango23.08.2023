from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import datetime, timedelta


def index(request):
    # любая логика

    return HttpResponse("""
    <h1> Hello from django ! </h1>
    <h2> Test Response </h2>
    """)


def day(request):
    current_datetime = datetime.now()
    return HttpResponse("<h1>Текущий день недели:</h1>"
                        f"<h2> {current_datetime.strftime('%A')}</h2>")


def date(request):
    current_datetime = datetime.now()
    return HttpResponse("<h1>Текущая дата:</h1>"
                        f"<h2> {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}</h2>")


def holiday(request):
    holiday_date = datetime(datetime.now().year, 1, 1) + timedelta(days=255)
    return HttpResponse("<h1>День программиста:</h1>"
                        f"<h2> {holiday_date.strftime('%Y-%m-%d')}</h2>")


def table(request):
    table = ''
    for x in range(1, 11):
        for y in range(1, 11):
            table += f"{x} x {y} = {x * y}<br>"
        table += "<br><br>"

    return HttpResponse("<h1> Таблица умножения ! </h1>"
                        f"{table}")

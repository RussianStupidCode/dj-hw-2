from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = request.GET.get('page', 1)
    with open(settings.BUS_STATION_CSV, newline='', encoding="utf-8") as csvfile:
        reader = [line for line in csv.DictReader(csvfile)]

    paginator = Paginator(reader, 10)

    context = {
         'bus_stations': paginator.get_page(page_number),
         'page': paginator.page(page_number),
    }
    return render(request, 'stations/index.html', context)

from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import todo, todomonth, todoweek
import time

# def index(request):
# return render(request, 'tasks/index.json')


def index(request):
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Субботу', 'Воскресенье'
            ]
    months = [
        'января', 'февраля', 'марта', 'апреля', 'майя', 'июнь', 'июля', 'августа', 'сентября',
        'октября', 'ноября', 'декабря'
    ]
    # среда, 21 октября 2020 г.

    context = {
        "NowDate": days[time.localtime().tm_wday] +
        time.strftime(
            ", %d, "+months[time.localtime().tm_mon-1]+" %Y г.", time.localtime())

    }
    return render(request, 'tasks/index.html', context)


def d3printer(request):
    return render(request, 'tasks/3dprinter.html')


def main_info(request):
    return render(request, 'tasks/main_info.html')


def Segway(request):
    return render(request, 'tasks/Segway.html')


def tablet(request):
    return render(request, 'tasks/tablet.html')


def VRAR(request):
    return render(request, 'tasks/VRAR.html')


def Smartphone(request):
    return render(request, 'tasks/Smartphone.html')

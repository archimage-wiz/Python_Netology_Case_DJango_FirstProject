from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, reverse
from datetime import datetime as dt
from os import listdir


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = dt.now().strftime("%d.%m.%Y %H:%M")
    msg = {'Current time': current_time}
    return JsonResponse(msg)


def workdir_view(request):
    template_name = 'app/dirs.html'
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    dirs = listdir('.')
    return render(request, template_name, context={'dirs': dirs})

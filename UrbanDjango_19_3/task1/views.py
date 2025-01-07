from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import UserRegister
from .models import Buyer, Game


def index(request):
    context = {
        'title': 'Главная страница',
        'index': reverse('index')
    }
    return render(request, 'first_task/index.html', context=context)


def page1(request):
    games = Game.objects.all()
    contex = {
        'title': 'Магазин',
        'index': reverse('index'),
        'games': games
    }
    return render(request, 'first_task/page1.html', context=contex)


def page2(request):
    context = {
        'text': 'Здесь будет информация о заказах',
        'title': 'Заказы',
        'index': reverse('index')
    }
    return render(request, 'first_task/page2.html', context=context)


def sign_up_by_django(request):
    users = []
    users1 = Buyer.objects.all().values()
    n_users = len(users1)
    for i in range(n_users):
        users.append(users1[i]['name'])
    info = {}

    if request.method == 'POST':
        user_have = False
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            is_user = username in users
            if password == repeat_password:
                if age >= 18:
                    if not is_user:
                        user_have = True
                    else:
                        info['error'] = 'Пользователь уже существует'
                else:
                    info['error'] = 'Вы должны быть старше 18'
            else:
                info['error'] = 'Пароли не совпадают'

            if user_have:
                message = f'Приветствуем, {username}!'
                Buyer.objects.create(name=username, balance=0, age=age)
                return HttpResponse(message)
            else:
                info['error'] = message = info['error']
        else:
            info['error'] = 'Форма не валидна'
            message = info['error']
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'first_task/registration_page.html', info)


def sign_up_by_html(request):
    users = []
    users1 = Buyer.objects.all().values()
    n_users = len(users1)
    for i in range(n_users):
        users.append(users1[i]['name'])
    info = {}

    if request.method == 'POST':
        user_have = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        is_user = username in users
        if password == repeat_password:
            if age >= 18:
                if is_user == False:
                    user_have = True
                else:
                    info['error'] = 'Пользователь уже существует'
            else:
                info['error'] = 'Вы должны быть старше 18'
        else:
            info['error'] = 'Пароли не совпадают'

        if user_have:
            message = (f'Приветствуем, {username}!')
            Buyer.objects.create(name=username, balance=0, age=age)
        else:
            message = info['error']
        return HttpResponse(message)
    return render(request, 'first_task/registration_page.html', info)

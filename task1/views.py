from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import *
# Create your views here.
def platform_view(request):
    return render(request, 'first_task/platform.html')


def games_view(request):
    # Получаем все объекты из базы данных
    games = Game.objects.all()

    context = {
        'games': games,
        'page_title': 'Список игр'
    }
    return render(request, 'first_task/games.html', context)


def cart_view(request):
    cart = request.session.get('cart', {})

    # Переносим игры в список
    items = [
        {'id': 'item1', 'name': 'Atomic heart', 'price': '$10'},
        {'id': 'item2', 'name': 'CyberPunk 2000', 'price': '$20'},
        {'id': 'item3', 'name': 'PayDay2', 'price': '$30'}
    ]

    cart_items = []
    total_price = 0

    for item in items:
        if item['id'] in cart:
            cart_items.append({
                'id': item['id'],
                'name': item['name'],
                'qty': cart[item['id']]
            })
            total_price += int(item['price'][1:]) * cart[item['id']]

    context = {
        'cart_items': cart_items,
        'items': items,
        'total_price': total_price
    }

    return render(request, 'first_task/cart.html', context)


def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})

    cart[item_id] = cart.get(item_id, 0) + 1

    request.session['cart'] = cart

    return redirect('games')


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']


            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'first_task/registration_page.html', info)
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'first_task/registration_page.html', info)

            existing_user = Buyer.objects.filter(Q(name=username)).exists()
            if existing_user:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'first_task/registration_page.html', info)
            else:
                # Создаем нового пользователя
                Buyer.objects.create(name=username, balance=100, age=age)

                return render(request, 'first_task/registration_success.html', {'username': username})
        else:
            form = UserRegister()
    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'first_task/registration_page.html', info)



from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['user1', 'user2', 'user3']
info = {}
def check(username, password, repeat_password, age):
    if password != repeat_password:
        info['error'] = "Пароли не совпадают"
    elif int(age) < 18:
        info['error'] = "Вы должны быть старше 18"
    elif username in users:
        info['error'] = "Пользователь уже существует"
    else:
        info['error'] = ''

# Create your views here.
def sign_up_by_django(request):

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            check(username, password, repeat_password, age)
            if not info['error']:
                users.append(username)
                return HttpResponse(f"Приветствуем, {username}!")
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', context = info)

def sign_up_by_html(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        check(username, password, repeat_password, age)
        if not info['error']:
            users.append(username)
            return HttpResponse(f"Приветствуем, {username}!")

    return render(request, 'registration_page.html', context = info)
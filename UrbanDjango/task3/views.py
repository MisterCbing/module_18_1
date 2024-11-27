from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def catalog(request):
    life = {'pos1': 'Крепкий алкоголь', 'pos2': 'Винишко', 'pos3': 'ПИВО'}
    return render(request, 'catalog.html', context=life)

def help(request):
    return render(request, 'help.html')
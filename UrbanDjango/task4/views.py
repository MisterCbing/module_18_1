from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def catalog(request):
    life = {'medicine': [['Крепкий алкоголь','Налить со льдом'], ['Винишко','Охладить и налить'],
                         ['ПИВО','Налить срочно!']]}
    return render(request, 'catalog.html', context=life)

def help(request):
    return render(request, 'help.html')
from django.shortcuts import render

context = {
    'name' : 'Nima',
    'last_name' : 'Bazargan',
    'address': 'Tehran, Iran',
    'phone': '(+98)9101539050',
    'email': 'nima.kazemzadeh.bazargan@gmail.com'
}

def index_view(request):
    return render(request, 'index.html', context)

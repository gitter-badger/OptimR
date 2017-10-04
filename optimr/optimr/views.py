from django.shortcuts import render


def home(request):
    context = {'variable': 'hello'}
    return render(request, 'optimr/home.html', context)
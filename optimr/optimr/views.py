from django

def home(request):
    context = {'variable': 'hello'}
    return render
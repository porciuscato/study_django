from django.shortcuts import render

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'index.html', context)

def create(request):
    context = {
        
    }
    return render(request, 'create.html', context)
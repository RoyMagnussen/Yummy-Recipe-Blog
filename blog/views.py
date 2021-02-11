from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/')
def home(request):
    context = {
        'title': 'Home',
    }

    return render(request, 'blog/home.html', context)

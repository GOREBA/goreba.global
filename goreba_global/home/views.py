from django.http import HttpResponse
from django.shortcuts import render
from home.models import Setting


# Create your views here.
def index(request):
    setting = Setting.objects.get()

    page = "home"
    context = {
        'setting': setting,
        'page': page
    }
    return render(request, 'home/index.html', context)

from django.shortcuts import render
from .models  import *
from django.http  import *
from .forms import *

# Create your views here.

def myuser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user-form/')
    else:
        form = UserForm()
    return render(request, 'user.html', {'form': form})

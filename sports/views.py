from django.shortcuts import render
from sports.models import Sport
from django.contrib.auth.decorators import login_required # @login_required()
from sports import forms
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.

# Function to display all Sports to the user
def sports_detail(request):
    get_sports_data = Sport.objects.all()
    context = {
        'sports_data' : get_sports_data,
    }
    return render(request,'sports/sports_detail.html', context)

# Function to display detailed particular sports information
def sports_info(request, sport_id):
    get_sports_info = Sport.objects.get(pk=sport_id)
    print(get_sports_info)
    context = {
        'sports_info' : get_sports_info,
    }
    return render(request,'sports/sports_info.html', context)

# Function to creating New Sport(Sports Form)
def sports_form(request):
    load_sports_form = forms.SportForm()

    if request.method == 'POST':
        load_sports_form = forms.SportForm(request.POST, request.FILES)
        print(load_sports_form)
        if load_sports_form.is_valid():
            load_sports_form.save(commit=True)
            return redirect('sports_detail')
    sport_data = {
        'sports_form' : load_sports_form,
    }
    return render(request,'sports/sports_form.html', context = sport_data)


from django.shortcuts import render
from sports.models import Sport
from django.contrib.auth.decorators import user_passes_test, login_required
from sports import forms
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
# decorator function to restrict the page for the admin only
def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_admin:
            messages.info(request, "Only admin is allowed to do that action.")
            return redirect('sports_detail')  # Replace with the URL you want to redirect to
        return view_func(request, *args, **kwargs)
    return wrapper


# Function to display all Sports to the user
def sports_detail(request):
    get_sports_data = Sport.objects.all()
    context = {
        'sports_data' : get_sports_data,
    }
    return render(request,'sports/sports_detail.html', context)

# Function to display detailed particular sports information
def sports_info(request, sport_id):
    if request.user.is_anonymous:
        messages.add_message(request, messages.INFO, 'You must be logged first in to access the page')
        return redirect('sports_detail')
    else:  
        get_sports_info = Sport.objects.get(pk=sport_id)
        context = {
            'sports_info' : get_sports_info,
        }
    return render(request,'sports/sports_info.html', context)

# Function to creating New Sport for admin only(Sports Form)
@admin_required
def sports_form(request):
    load_sports_form = forms.SportForm()

    if request.method == 'POST':
        load_sports_form = forms.SportForm(request.POST, request.FILES)
        
        if load_sports_form.is_valid():
            load_sports_form.save(commit=True)
            sport = Sport.objects.last()
            new_sport_name = sport.sport_name
            messages.success(request, f"New Sport '{new_sport_name}' is Added Successfully")
            return redirect('sports_detail')
        
    sport_data = {
        'sports_form' : load_sports_form,
    }
    return render(request,'sports/sports_form.html', context = sport_data)

# Function to delete Sport for admin only
@admin_required
def delete_sport(request, sport_id):
    sport_to_delete = Sport.objects.get(pk=sport_id)
    sport_name = sport_to_delete.sport_name
    sport_to_delete.delete()
    messages.info(request, f"The Sport '{sport_name}' is Deleted Successfully")
    return redirect('sports_detail')

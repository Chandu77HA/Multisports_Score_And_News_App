from django.shortcuts import render
from sports.models import Sport
from sports import forms
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

# decorator function to restrict the page for the adminuser only
def superuser_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "You need to be logged in as an admin to access that page.")
            return redirect('login')  # Replace with the login URL
        elif not request.user.is_superuser:
            messages.info(request, "Only admin is allowed to do that action.")
            return redirect('sports_detail')  # Replace with the URL you want to redirect to
        return view_func(request, *args, **kwargs)
    return wrapper

# Function to display all Sports to the user
def sports_detail(request):
    get_sports_data = Sport.objects.all().order_by('id')
    context = {
        'sports_data' : get_sports_data,
    }
    return render(request,'sports/sports_detail.html', context)

# Function to display detailed particular sports information
def sports_info(request, sport_id):
    if request.user.is_anonymous:
        messages.add_message(request, messages.INFO, 'You must be logged in first to access that page.')
        return redirect('login')
    else:  
        get_sports_info = Sport.objects.get(pk=sport_id)
        context = {
            'sports_info' : get_sports_info,
        }
    return render(request,'sports/sports_info.html', context)

# Function to creating New Sport for admin only(Sports Form)
@superuser_required
def sports_form(request):
    load_sports_form = forms.SportForm()

    if request.method == 'POST':
        load_sports_form = forms.SportForm(request.POST, request.FILES)
        
        if load_sports_form.is_valid():
            load_sports_form.save(commit=True)
            sport = Sport.objects.last()
            sport.sport_name = sport.sport_name.upper()
            sport.save()
            messages.success(request, f"New Sport {sport.sport_name} is Added Successfully")
            return redirect('sports_detail')
        
    sport_data = {
        'sports_form' : load_sports_form,
    }
    return render(request,'sports/sports_form.html', context = sport_data)

# Function to delete Sport for admin only
@superuser_required
def delete_sport(request, sport_id):
    sport_to_delete = Sport.objects.get(pk=sport_id)
    sport_name = sport_to_delete.sport_name
    sport_to_delete.delete()
    messages.info(request, f"The Sport {sport_name} is Deleted Successfully")
    return redirect('sports_detail')

# Function to edit Sport for admin only
@superuser_required
def edit_sport(request, sport_id):
    sport_info = Sport.objects.get(pk=sport_id)
    sport_name = sport_info.sport_name
    get_sport_form = forms.SportForm(instance=sport_info)
    
    if request.method == 'POST':
        get_sport_form = forms.SportForm(request.POST, request.FILES, instance=sport_info)

        if get_sport_form.is_valid():
            get_sport_form.save(commit=True)
            messages.success(request, f"The Sport {sport_name} is Successfully Updated..!")
            return sports_info(request, sport_id)
        
    sports_data = {'title' : 'Edit Sport',
                   'edit_from' : get_sport_form,}
    return render(request, 'sports/edit_sport.html', context = sports_data)


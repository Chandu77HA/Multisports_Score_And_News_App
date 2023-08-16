from django.shortcuts import render
from home.models import ContactList, ContactUs, About, Slider
from authentication.models import User

# Create your views here.

# Function for Home page
def home(request):
    slider_data = Slider.objects.all().order_by('-id')
    user = User.objects.all()
    context = {
        'slider' : slider_data,
        'user' : user,
    }
    return render(request, 'home/home.html', context)

# Function for Contact Us page
def contact_us(request):
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_email = request.POST.get('email')
        get_subject = request.POST.get('subject')
        get_message = request.POST.get('message')

        contact_us_data = ContactUs(name = get_name, email = get_email, subject = get_subject, message = get_message)
        contact_us_data.save()

    contact_list_data = ContactList.objects.all()[0]
    context = {
        'contact' : contact_list_data,
    }
    return render(request, 'home/contact_us.html', context)

# Function for About Us page
def about_us(request):
    about_data = About.objects.all()[0]
    context = {
        'about' : about_data
    }
    return render(request, 'home/about_us.html', context)



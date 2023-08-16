from django import forms
from sports.models import Sport, SportFormat

class SportFormatForm(forms.ModelForm):
    class Meata():
        model = SportFormat
        fields = "__all__"

class SportForm(forms.ModelForm):

    #forrmat_type = forms.CharField(label="Sport Format", widget = forms.Select(attrs={'class': 'form-control'}))
    sport_name = forms.CharField(label="Sports Name", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter the sport name'}))
    description = forms.CharField(label="Description", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter the sport Description', 'style':'height:80px',}))
    playing_area = forms.CharField(label="Playing Area", widget = forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Enter the playing area'}))
    equipments_required = forms.CharField(label="Equipments Required", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter the equipments required for the sport','style':'height:80px'}))
    history = forms.CharField(label="History", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter the history of the sport', 'style':'height:80px'}))
    rules = forms.CharField(label="Rules", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter the rules for the sport', 'style':'height:80px'}))
    #image = forms.ImageField(label="Image", widget = forms.ImageField(attrs={'class': 'form-control'}))
    #number_of_players = forms.CharField(label="Number of players", widget = forms.TextInput(attrs={'class': 'form-control'}))
    #category = forms.CharField(label="Category", widget = forms.TextInput(attrs={'class': 'form-control'}))
    governing_body = forms.CharField(label="Governing Body", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter the governing body for the sport'}))

    class Meta():
        model = Sport
        fields = "__all__"


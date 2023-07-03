from django import forms
from .models import Person, Car, Rent
from django.core.validators import RegexValidator
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import ClearableFileInput
class FormContact(forms.Form):
    full_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'style' : 'color : blue'}))
    email = forms.EmailField(max_length=50, required=False)
    phone = forms.CharField(validators=[RegexValidator(r'^\d+$')], required=False)
    city = forms.ChoiceField(choices=[
        ("tlv", "תל אביב"),
        ("jerusalem", "ירושלים"),
        ("haifa", "חיפה"),
    ], required=False)
    terms = forms.BooleanField(required=True)
    choose_a_car = forms.ModelChoiceField(queryset=(Car.objects.all()), required=False)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': "datetime-local"}), required=False)
    testing123 = forms.CharField(widget=forms.Textarea(attrs={"style": "color : red", "rows" : 3}), max_length=250, required=False)
    img = forms.FileField()




class CarForm(forms.ModelForm):
    plate_id = forms.CharField(required=True, validators=[RegexValidator(r"^\d{7,9}$", message= "7-9 digits number")])
    cost = forms.FloatField(required=True, min_value=0, max_value=9999)
    manufacturer = forms.CharField(max_length=40, required=True)
    model = forms.CharField(max_length=40, required=True)
    year = forms.IntegerField(min_value=1800, max_value=date.today().year)
    km = forms.IntegerField(min_value=0, max_value=999999)
    gearbox = forms.ChoiceField(choices=[
        ("Automatic", "Automatic"),
        ('Manual', 'Manual'),
        ('Tiptronic', 'Tiptronic'),
    ])
    
    
    class Meta:
        model = Car
        fields = '__all__'
        
        

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=40, required=True)
    age = forms.IntegerField(max_value=120, min_value=0, required=True)    


    class Meta:
        model = Person
        fields = ['username', 'password1', 'password2','email', 'first_name', 'last_name', 'age', 'person_id', 'phone_number', 'city', 'age']
        exclude = ['password',]

    labels = {
        'sdaads' : 'username',

    }
class LoginForm(forms.Form):
    username = forms.CharField(max_length=155)
    password = forms.CharField(max_length=155, widget=forms.PasswordInput)
    

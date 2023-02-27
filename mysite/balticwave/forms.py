from .models import Profile, Product
from django import forms
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']

class UserProductCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'description', 'type', 'product_thumbnail', 'status' ]
        widgets = {'product_seller': forms.HiddenInput(), 'insDate': DateInput()}
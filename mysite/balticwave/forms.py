from .models import Profile, Product, ProductReview, Service
from django import forms
from django.contrib.auth.models import User

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('content', 'product', 'reviewer',)
        widgets = {'product': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}
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
        fields = ['product_name', 'price', 'short_description', 'description', 'category', 'type', 'product_thumbnail', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'city', 'status']
        widgets = {'product_seller': forms.HiddenInput(), 'insDate': DateInput()}

class UserServiceCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('service_name', 'description', 'category', 'type', 'service_thumbnail')
        widgets = {'service_seller': forms.HiddenInput(), 'insDate': DateInput()}





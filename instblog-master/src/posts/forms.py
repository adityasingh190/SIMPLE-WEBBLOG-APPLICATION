from django import forms
from django.contrib.auth.models import User
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
		"title",
		"content",
		"image",
		
		]

class UserForm(forms.ModelForm): #blueprint of user form
	password = forms.CharField(widget=forms.PasswordInput) #password is not in admin user by default hence we have to declare it..widget=forms.PasswordInput = this to to make *** when inputting password
	class Meta: #information about class
		model = User # user model from admin
		fields = ['username','email','password']
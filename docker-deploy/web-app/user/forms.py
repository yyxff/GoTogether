from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=4, label='User name', error_messages={
        'required' : 'Please enter user name.',
        'max_length' : 'No more than 20 characters.',
        'min_length' : 'No less than 4 characters.',
    })
    # email = forms.EmailField(error_messages={
    #     'required' : 'Please enter your email.',
    #     'invalid' : 'Please enter a valid email address.'
    # })
    pwd1 = forms.CharField(max_length=20, min_length=6, label='Password', error_messages={
        'required' : 'Please enter password.',
        'max_length' : 'No more than 20 characters.',
        'min_length' : 'No less than 6 characters.',
    })
    pwd2 = forms.CharField(max_length=20, min_length=6, label='Confirm Password', error_messages={
        'required': 'Please enter password once again to confirm.',
        'max_length': 'No more than 20 characters.',
        'min_length': 'No less than 6 characters.',
    })

    def clean_username(self):
        username = self.cleaned_data.get('username')
        exist = User.objects.filter(username=username).exists()
        if exist:
            raise forms.ValidationError('Account has already been registered.')
        else:
            return username

    def clean_pwd2(self):
        pwd1 = self.cleaned_data.get('pwd1')
        pwd2 = self.cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError('The two passwords are different.')
        else:
            return pwd2

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=4, label='User name', error_messages={
        'required' : 'Please enter user name.'})
    pwd = forms.CharField(max_length=20, min_length=6, label='Password')
    remember = forms.BooleanField(required=False)
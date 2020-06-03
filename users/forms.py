from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32, widget=forms.TextInput(
        attrs={
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password'
        }
    ))


class RegisterForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=32, widget=forms.TextInput(
        attrs={
            'placeholder': 'example@f1recloud.com'
        }
    ))
    username = forms.CharField(label='Username', max_length=32, widget=forms.TextInput(
        attrs={
            'placeholder': 'Username'
        }
    ))

    password1 = forms.CharField(label='Password', max_length=32, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password'
        }
    ))
    password2 = forms.CharField(label='Re-enter Password', max_length=32, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password'
        }
    ))

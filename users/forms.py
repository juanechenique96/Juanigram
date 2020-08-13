# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    username = forms.CharField(label=False,
                                min_length=4,
                                max_length=50, 
                                widget = forms.TextInput(
                                    attrs={
                                        'placeholder':'Username',
                                        'class': 'form-control mb-2',
                                        'required': True
                                        }
                                    )
                                )

    password = forms.CharField(label=False,
                                max_length=70, 
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder':'Password',
                                        'class': 'form-control mb-2',
                                        'required': True
                                        }
                                    )
                                )
    password_confirmation = forms.CharField(label=False,
                                                max_length=70, 
                                                widget=forms.PasswordInput(
                                                    attrs={
                                                        'placeholder':'Password confirmation',
                                                        'class': 'form-control mb-3',
                                                        'required': True
                                                        }
                                    )
                                )

    first_name = forms.CharField(label=False, 
                                    min_length=3, 
                                    max_length=50,
                                    widget=forms.TextInput(
                                        attrs={
                                            'placeholder':'First name',
                                            'class': 'form-control mb-2',
                                            'required': True
                                        }
                                    )
                                )
    last_name = forms.CharField(label=False, 
                                    min_length=3, 
                                    max_length=50,
                                    widget=forms.TextInput(
                                        attrs={
                                            'placeholder':'Last name',
                                            'class': 'form-control mb-3',
                                            'required': True
                                        }
                                    )
                                )

    email = forms.CharField(label=False,
                                min_length=6, 
                                max_length=70, 
                                widget=forms.EmailInput(
                                    attrs={
                                            'placeholder':'Email',
                                            'class': 'form-control mb-2',
                                            'required': True
                                        }
                                    )
                                )

    def clean_username(self):
        """ Username must be unique. """
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is alreasy in use.')
        return username

    def clean(self):
        """ Verification password confirmaton match. """
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password do not match')
        return data

    def save(self):
        """ Create a user and profile. """
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField(required=False)
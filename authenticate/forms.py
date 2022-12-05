from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# Create new form, based on UserCreationForm to add
# additional fields to default


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User  # designates that we're using the User model
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    # Have to customize mandatory fields differently:
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

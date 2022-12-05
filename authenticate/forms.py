from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# Create new form, based on UserCreationForm to add
# additional fields to default


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(
        max_length=100, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(
        max_length=100, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User  # designates that we're using the User model
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    # Have to customize mandatory fields differently:
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Customize helper text for password fields (can't get newline to work)
        helper_text = """<ul class='text text-muted'>
            <li>Your password can\'t be too similar to your other personal information.</li>
            <li>Your password must contain at least 8 characters.</li>
            <li>Your password can\'t be a commonly used password.</li>
            <li>Your password can\'t be entirely numeric.</li>
            </ul>
            """

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        # Add in some HTML and Bootstrap formatting
        self.fields['username'].help_text = "<span class='text text-muted'><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>"

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].help_text = '{}'.format(helper_text)

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat Password'
        self.fields['password2'].help_text = "<span class='text text-muted'><small>Enter the same password as before, for verification.</small></span>"

from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError


class UserCreationForm(BaseUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.pop('autofocus', None)
        self.fields['first_name'].widget.attrs['autofocus'] = 'true'

        # To add extra stuff to rendered element 👇
        # self.fields['email'].widget.attrs['style'] = 'color: red;'

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2',)


class UserUpdateForm(forms.ModelForm):
    avatar = forms.ImageField(label='Avatar', required=False, error_messages={
                                    'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = get_user_model()
        fields = ('avatar', 'email', 'username', 'first_name', 'last_name',)


class ConfirmPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ConfirmPasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        # Reference: https://docs.djangoproject.com/en/4.1/ref/forms/validation/
        password = self.cleaned_data['password']

        if check_password(password, self.request.user.password):
            return self.cleaned_data
        else:
            # self.add_error('password', 'Password is incorrect!')
            raise ValidationError('Password is incorrect!')

    class Meta:
        model = get_user_model()
        fields = ('password',)

from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput

from .models import CustomUser


class RegisterCustomUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'phone', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'email': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'phone': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'first_name': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'type': 'text', 'class': 'form-control'}),
                   }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.password = self.cleaned_data['password1']
        if commit:
            user.save()
        return user

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords mismatch")
        return password2

from django import forms

from main.models import LibUser


class LibUserForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'validationCustom01', 'placeholder': 'Mark',
                                                              'class':"form-control"}),
                             required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'validationCustom01', 'placeholder': 'sample@gmail.com',
                                                              'class': "form-control"}),
                                required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'id': 'validationCustom01', 'placeholder': '+998997777777',
                                                              'class': "form-control"}),
                                required=True)

    class Meta:
        model = LibUser
        fields = '__all__'
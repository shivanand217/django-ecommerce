from django import forms
# builtin django forms are here

from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "id": "form_full_name", 
                                        "placeholder": "FullName"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "id": "form_email", 
                                        "placeholder": "Email"})
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "id": "form_content",
                                        "placeholder": "Content"})
    )
    contact = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class":"form-control", "id":"form_contact",
                                        "placeholder":"Contact"})
    )

    # forms fields validations
    def clean_email(self):
        # fetch the original field data
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control", "id":"login_username",
                                        "placeholder": "Username"}),max_length=50,strip=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form-control", "id":"login_password",
                                            "placeholder": "Password"})
    )

class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control", "id":"login_username",
                                        "placeholder": "Username"}),max_length=50,strip=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form-control", "id":"register_password",
                                            "placeholder":"Password"})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form-control", "id":"register_confirm_password",
                                            "placeholder":"Confirm Password"})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"class":"form-control", "id":"register_email",
                                        "placeholder":"Email"}),max_length=50,strip=True
    )
    contact = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class":"form-control", "id":"register_contact",
                                        "placeholder":"Contact"})
    )

    # fields validations
    def clean_username(self):
        username = self.cleaned_data.get("username")
        query_set = User.objects.filter(username=username)
        if query_set.exists():
            raise forms.ValidationError("Username is taken.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        query_set = User.objects.filter(email=email)
        if query_set.exists():
            raise forms.ValidationError("Email is taken.")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password != password2:
            raise forms.ValidationError("Passwords should must match.")
        return data
    
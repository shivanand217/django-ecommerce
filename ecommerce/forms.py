from django import forms

# builtin django forms are here

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
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control", "id":"register_firstname",
                                        "placeholder":"FirstName"}),max_length=50,strip=True
    )
    lastname = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control", "id":"register_lastname",
                                        "placeholder":"LastName"}),max_length=50,strip=True
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
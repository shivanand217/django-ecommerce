
from django import forms

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

    # forms fields validations

    def clean_email(self):
        # fetch the original field data
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email
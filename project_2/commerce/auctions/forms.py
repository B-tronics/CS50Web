from django import forms

class CreateListingForm(forms.Form):
    title = forms.CharField(label="Add title", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control",
        "aria-describedby": "titleHelp",
        "placeholder": "Title"
    }))
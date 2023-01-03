from django import forms


class CreateListingForm(forms.Form):
    title = forms.CharField(label="Add title", max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control",
        "aria-describedby": "titleHelp",
        "placeholder": "Title"
    }))
    description = forms.CharField(label="Add description", widget=forms.Textarea(attrs={
        "class": "form-control",
        "aria-describedby": "descriptionHelp",
        "placeholder": "Descripton",
        "rows": "10",
    }))
    starting_bid = forms.IntegerField(label="Add starting bid", widget=forms.NumberInput(attrs={
        "class": "form-control",
        "aria-describedby": "startingBidHelp",
        "placeholder": "0"
    }))

    picture = forms.URLField(label="Add a pictue (Optional)", required=False, widget=forms.URLInput(attrs={
        "class": "form-control",
        "aria-describedby": "pictureHelp",
    }))

class BiddingForm(forms.Form):
    bid = forms.IntegerField(label="", widget=forms.NumberInput(attrs={
        "class": "form-control",
        "aria-describedby": "startingBidHelp",
        "placeholder": "0"
    }))
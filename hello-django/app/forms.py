from django import forms


class AgeForm(forms.Form):
    end = forms.IntegerField(label="Current Year")
    birthday = forms.IntegerField(label="Birth Year")


class OrderForm(forms.Form):
    burgers = forms.IntegerField(label="Number of Burgers")
    fries = forms.IntegerField(label="Number of Fries")
    drinks = forms.IntegerField(label="Number of Drinks")

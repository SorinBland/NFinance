from django import forms


class Calculator(forms.Form):
    age = forms.DecimalField()
    age_retirement = forms.DecimalField()
    monthly_save = forms.FloatField()
    saved_now = forms.FloatField()
    income_spent = forms.FloatField()


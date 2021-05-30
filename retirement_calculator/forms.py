from django import forms


class Calculator(forms.Form):
    age = forms.DecimalField(min_value=15, max_value=80)
    age_retirement = forms.DecimalField(min_value=18, max_value=80)
    monthly_save = forms.FloatField()
    saved_now = forms.FloatField()
    income_spent = forms.FloatField()


from django.shortcuts import render

# Create your views here.
from retirement_calculator import forms


def retirement_calculator(request):
    form = forms.Calculator(request.POST)
    life_expectation = 80
    if request.method == 'POST':
        if form.is_valid():
            age = int(form['age'].value())
            age_retirement = int(form['age_retirement'].value())
            monthly_save = int(form['monthly_save'].value())
            saved_now = int(form['saved_now'].value())
            income_spent = int(form['income_spent'].value())

            until_retirement = age_retirement - age
            years_in_retirement = life_expectation - age_retirement
            year_save = monthly_save * 12

            inflation_ajusted = year_save * 3 / 100 + year_save
            inflation_ajusted_monthly_save = monthly_save * 2 / 100 + monthly_save
            inflation_ajusted_income_spent = income_spent * 2 / 100 + income_spent
            saved_until_retirement = (inflation_ajusted_monthly_save * 12) * until_retirement + saved_now

            count = 0
            while count < until_retirement - 1:
                count += 1
                inflation_ajusted_income_spent += inflation_ajusted_income_spent * 2 / 100
                inflation_ajusted_monthly_save += inflation_ajusted_monthly_save * 2 / 100
                inflation_ajusted += inflation_ajusted * 3 / 100

            difference = saved_until_retirement - inflation_ajusted
            context = {'until_retirement': until_retirement, "years_in_retirement": years_in_retirement,
                       "inflation_ajusted": inflation_ajusted,
                       "inflation_ajusted_monthly_save": f"{inflation_ajusted_monthly_save:.2f}",
                       "inflation_ajusted_income_spent": f"{inflation_ajusted_income_spent:.2f}",
                       "saved_until_retirement": f"{saved_until_retirement:.2f}",
                       "year_save": year_save,
                       "difference": f"{difference:.2f}"}
            return render(request, "calculator_results.html", context)
        return render(request, "calculator.html", {"form": form})
    return render(request, "calculator.html", {"form": form})

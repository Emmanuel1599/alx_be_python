monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))


montthly_savings = monthly_income - monthly_expenses


projected_annual_savings = montthly_savings * 12 + (montthly_savings * 12 * 0.05)


print(f"Your monthly savings are ${montthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}.")
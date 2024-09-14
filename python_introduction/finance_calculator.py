# This script will calculate the user’s monthly savings based on inputted monthly income and expenses. 
# It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

monthly_income = float(input('Enter your monthly income: '))
monthly_expenses = float(input('Enter your total monthly expenses: '))

monthly_savings = monthly_income - monthly_expenses

annual_interest_rate = 0.05

# formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

print(f'Your monthly savings are ${monthly_savings}.')
print(f'Projected savings after one year, with interest, is: %{projected_savings}.')

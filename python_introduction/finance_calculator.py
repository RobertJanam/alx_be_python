"""Program that calculates and provide feedback on a user’s monthly savings 
and potential future savings without applying conditional statements."""

monthly_income = float(input("Enter your monthly income: "))

monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

simple_annual_interest_rate = 0.05

projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * simple_annual_interest_rate)

print(f"Projected savings after one year, with interest, is: {projected_annual_savings}")
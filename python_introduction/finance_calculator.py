Monthly_income = int(input("Enter your monthly income: "))
Monthly_expense = int(input("Enter your total monthly expenses: "))
Monthly_Savings = Monthly_income - Monthly_expense
print("Your montly savings are", Monthly_Savings)
Projected_Savings = (Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05))
print("Projected savings after one year, with interest, is:", Projected_Savings)

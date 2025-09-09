income = int(input("Enter your monthly income: "))
expense = int(input("Enter your total monthly expenses: "))
Monthly_Savings = income - expense
print("Your montly savings are", Monthly_Savings)
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 0.05 * 12)
print("Projected savings after one year, with interest, is:", Projected_Savings)

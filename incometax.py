# Collects user's yearly income as an input
income = int(input("Input this year's income: "))

# Sets initial tax to 0
tax = 0

# Calculates and reassigns tax depending on income range
if income < 10000:
    tax = 8
elif 10001 <= income <= 26000:
    tax = 12
else:
    tax = 24

# Calculates income after tax
taxed_income = income * (tax / 100)

# Prints what percentage of tax is assigned to given income
print(f"The tax on this income is {tax}%")

# Prints income after tax
print(f"Income after tax: ${taxed_income}")

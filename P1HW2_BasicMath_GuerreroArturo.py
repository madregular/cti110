# Description
# 06/05/2022
# CTI-110 P1HW2 - Basic Math
# Arturo Guerrero
#
# Ask the user to enter the name of the expense and thhe monthly amount
expense_name = input("Enter name of expense:")
expense_amnt = int(input("Enter monthly charge(Without Tax):"))

# Calculate the monthly tax multiplying expense amount by 6%
tax = 0.06 * expense_amnt

# Calculate amount paid monthly by adding the tax to the monthly amount
monthly_charge = tax + expense_amnt

# Calculate amount paid for the entire year by multiplying monthly amount by 12
annual_charge = monthly_charge * 12

# Print results: Bill name and amount before tax, followed by the monthly tax by itself, the monthly charge
# including tax, and the annual amount.
print("Bill:", expense_name, "-------- Before Tax: $", expense_amnt)
print("Monthly Tax:    $%5.2f" %(tax))
print("Monthly Charge: $%5.2f" %(monthly_charge))
print("Annual Charge:  $%5.2f" %(annual_charge))
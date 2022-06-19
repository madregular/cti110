# A program to calculate the total amount of a meal purchased from a restaurant
# 19 June 2022
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Arturo Guerrero
#

# Ask user to enter the charge for food
meal_cost = float(input('Enter Food Cost: $'))

# Ask user to enter the Tip for server
meal_tip = float(input('\nEnter Tip Percentage(in decimal): '))

# Ask user to enter the Tax amount
meal_tax = float(input('Enter Tax Percentage(in decimal): '))

# Calculate tip, tax, and total cost
calculated_tip = meal_cost * meal_tip
calculated_tax = meal_cost * meal_tax
total_cost = meal_cost + calculated_tax + calculated_tip

# Display the following:
# *Calculated tip
# *Calculated tax
# *Display total cost of meal
print('\nCalculated Tip:: ', f'${calculated_tip:.2f}')
print('Calculated Tax: ', f'${calculated_tax:.2f}\n')
print('Total cost including tip and tax: ', f'$ {total_cost:.2f}')

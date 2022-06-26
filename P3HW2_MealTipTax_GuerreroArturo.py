# CTI-110
# P3HW2 - MealTipTax
# Arturo Guerrero
# 06/26/2022
#

#   Asks the user to enter the charge for the meal
meal_cost = float(input("Please enter cost of meal: "))

#   Ask user to enter the tip percentage they would like to consider (15% or 18% or 20%)
tip_amounts = ["15", "18", "20"]

#   ask user to enter tip amount
meal_tip = input("Enter tip amount of 15, 18, or 20: ")

#   check for accurate percentage entered, if true calculate the tip percentage and tax
if meal_tip in tip_amounts:
    if meal_tip == "15":
        meal_tip = meal_cost * 0.15
    elif meal_tip == "18":
        meal_tip = meal_cost * 0.18
    elif meal_tip == "20":
        meal_tip = meal_cost * 0.2
    # output the total costs of the meal, tax, tip, and total
    # meal_tax = meal_cost multiplied by 6%
    # total is the sum of tip, cost, and tax
    meal_tax = meal_cost * 0.06
    meal_total = float(meal_tip) + float(meal_cost) + meal_tax
    print(f"Meal price: ${meal_cost:.2f}")
    print(f"Tax: ${meal_tax:.2f}")
    print(f"Tip: ${meal_tip:.2f}")
    print(f"Total: ${meal_total:.2f}")

# if the tip amount given is not allowed, output an error
else:
    print("Error: Incorrect tip percentage")

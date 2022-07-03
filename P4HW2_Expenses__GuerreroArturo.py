# CTI-110
# P4HW2 - Expenses
# Arturo Guerrero
# 07/03/2022
#

# list created to hold the expenses
expense_list = []

# Prompt user to enter amount in account in which money will be withdrawn from.
starting_amnt = float(input("Enter starting amount in account $"))

# Prompt user to enter amount of first expense
expense_list.append(float(input("\nEnter expense 1: ")))

# Ask user if he/she would like to enter another expense
another_expense = input("Do you want to enter another expense? (y/n) ")
while another_expense == 'y':
    expense_count = len(expense_list) + 1
    expense_list.append(float(input(f"\nEnter expense {expense_count}: ")))
    another_expense = input("Do you want to enter another expense? (y/n) ")

# if the user chooses not to add an expense, continue to output
else:
    # calculate/subtract the final amount
    final_cost = starting_amnt - sum(expense_list)

    # print the amount before and after the expenses, and the number of expenses
    print(f"\nAmount in account before expenses subtracted ${starting_amnt:.2f}")
    print(f"Number of expenses entered: {len(expense_list)}")
    print(f"Amount in account after expenses subtracted is ${final_cost:.2f}")

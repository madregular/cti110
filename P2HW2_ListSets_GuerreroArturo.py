# CTI-110
# P2HW2 - List and Sets
# Arturo Guerrero
# 19 June 2022
#

# Asks the user to enter a series of 6 numbers.(10 points)
num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
num3 = int(input("Enter num 3: "))
num4 = int(input("Enter num 4: "))
num5 = int(input("Enter num 5: "))
num6 = int(input("Enter num 6: "))

# The program should store the numbers in a list. Give the list created a descriptive name (10 points)
number_list = [num1, num2, num3, num4, num5, num6]

# Display the following: (10 points each)
print("\nCreated list")
print(number_list)

# The lowest number in the list
print("Smallest Number in list: ", min(number_list))

# The highest number in the list
print("Largest Number in list: ", max(number_list))

# The total of the numbers in the list
number_sum = sum(number_list)
print("Sum of numbers in list: ", number_sum)

# The average of the numbers in the list
print("Average of numbers in list: ", number_sum / len(number_list))

# Convert to set
print("\nCreated set")
print(set(number_list))


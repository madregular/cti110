# CTI-110
# P4HW1 - Score List
# Arturo Guerrero
# 07/02/2022
#

# Ask user to enter for number of scores they would like to enter
scores = []
num_scores = int(input("How many scores would you like to enter?: "))

# check if a a proper number of scores if given between 0 - 6
for i in range(num_scores):
    if (num_scores < 0) or (num_scores > 6):
        print("Error: Only numbers from 1-6")
        num_scores = int(input("How many scores would you like to enter?: "))
    else:
    # Create a loop to collect the number of scores the user wants to enter
        while len(scores) < num_scores:
            usr_input = int(input(f"Enter score #{len(scores) + 1}: "))
            # validate if the score is between 0 and 100. If it is not valid, notify the user
            if (usr_input < 0) or (usr_input > 100):
                print("INVALID NUMBER!!!!")
                print("Score should be between 0 and 100")
            else:
                # if valid, add the score to the list
                scores.append(usr_input)


# modify the list, sort the list and pop the lowest number
scores.sort()
scores.pop(0)

# get the average of the list
score_avg = sum(scores) / len(scores)

# calculate the grade based off the average
if score_avg >= 90:
    grade = 'A'
elif score_avg >= 80:
    grade = 'B'
elif score_avg >= 70:
    grade = 'C'
elif score_avg >= 60:
    grade = 'D'
else:
    grade = 'F'

# After collecting all the scores:
# print the Lowest score entered
# Score List after dropping the lowest score
# average of scores in modified list

print("\n\n---------------Results---------------")
print(f"Lowest Score   : {min(scores)}")
print(f"Modified List  : {scores}")
print(f"Scores Average : {score_avg}")
print(f"Grade          : {grade}")
print("-------------------------------------")
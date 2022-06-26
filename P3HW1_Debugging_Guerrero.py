# Complete and debug the provided program, test it, and submit the working program.
# 06/25/2022
# CTI-110 P3HW1 - Debugging
# Arturo Guerrero

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    # TO DO: define the rest of the scores
    B_score = 80
    C_score = 70
    D_score = 60

    # take input from user and store it in score
    score = int(input('Please enter score: '))

    # compare input score to set grade scores. Output the final grade.
    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is: C')
    elif score >= D_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F') # TO DO: finish this


# program start
main()

def feet_to_steps(user_feet):
    steps = user_feet / 2.5
    return int(steps)



if __name__ == '__main__':
    feet_walked = float(input())
    print(f"{feet_to_steps(feet_walked)}")
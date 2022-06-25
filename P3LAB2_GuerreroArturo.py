# Return automobile cost to a user
# Arturo Guerrero
# 6/25/2022
# CTI-110 - P3LAB2

# create dictionary of services and costs
service_dict = {"Oil change": 35,
                "Tire rotation": 19,
                "Car wash": 7,
}

# prompt the user for an input, show output
service_req = input("Enter desired auto service:\n")
print(f"You entered: {service_req}")

# check in the service is in the dictionary, output the cost, if not then provided error
if service_req in service_dict:
    if service_req == "Oil change":
        print(f"Cost of oil change: ${service_dict['Oil change']}")
    elif service_req == "Tire rotation":
        print(f"Cost of tire rotation: ${service_dict['Tire rotation']}")
    elif service_req == "Car wash":
        print(f"Cost of car wash: ${service_dict['Car wash']}")
else:
    print("Error: Requested service is not recognized")
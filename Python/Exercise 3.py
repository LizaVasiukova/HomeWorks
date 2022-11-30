#Task 3.1

"""""
zander = int(input("What is the size of the zander?: "))
if zander < 42:
    print(f"Release fish back to the lake. The zander is {42 - zander} cm below the size limit.")
else:
    print("Good catch! The zander meets the size requirements.")
"""""

# Task 3.2
"""""
cabin = input("Please enter the cabin clas:")
if cabin == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin == "B":
    print("B: windowless cabin above the car deck.")
elif cabin == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
"""

#Task 3.3
"""
gender = input("Type your gender: ")
hem = int(input("Type hemoglobin value (g/l): "))
if gender == "female":
    if hem > 155:
        print("Hemoglobin level is too high.")
    elif hem < 117:
        print("Hemoglobin level is too low.")
    else:
        print("Hemoglobin level is normal.")
elif gender == "male":
    if hem > 167:
        print("Hemoglobin level is too high.")
    elif hem < 134:
        print("Hemoglobin level is too low.")
    else:
        print("Hemoglobin level is normal.")
else:
    print("Incorrect gender.")
    
"""""

#Task 3.4

year = int(input("Enter a year: "))
if year % 4 == 0:
    print("It's a leap year.")
elif year % 400 == 0:
    print("It's a leap year.")
else:
    print("It is not a leap year.")

    password = input("Password: ")
    if password == "sekred":
        print("User account created!")
    while password != "sekred":
        print("They do not match")
        new_pass = input("Repeat password: ")
        if new_pass == "sekred":
            print("User account created!")
            break
    """

    password = input("Password: ")

    while True:
        if password == "sekred":
            print("User account created!")
            break  
        elif password != "sekred":
            print("They do not match")
            new_pass = input("Repeat password: ")
        if new_pass == "sekred":
            print("User account created!")
            break  
        elif new_pass != "sekred":
            print("They do not match")

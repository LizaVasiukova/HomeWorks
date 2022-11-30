import random
"""
#Task 4.1
Write a program that uses a while loop to print out all 
#numbers divisible by three in the range of 1-1000.
i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i = i + 1
"""
#Task 4.2 Write a program that converts inches to centimeters until the user
#inputs a negative value. Then the program ends.
""""""

while True:
    inch = float(input("Enter inches: "))
    if inch < 0:
        print("Please enter a positive number.")
        break
    print(f" {inch} inches is {inch * 2.54} centimeters.")
    
"""
#Task 4.3 Write a program that asks the user to enter numbers
# until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.

"""""
"""

number = input("Enter the number: ")
biggest = float(number)
smallest = biggest

while True:
    number = input("Enter the number: ")

    if number == "":
        break

    number = float(number)
    if number > biggest:
        biggest = number
    elif number < smallest:
        smallest = number

print(f" Biggest number is {biggest} and the smallest is {smallest}")
"""
#Task 4.4

"""""
""""""
number = random.randint(1, 10)

while True:
    answer = input("Guess the number: ")
    answer = int(answer)
    if answer > number:
        print("Too high.")
    elif answer < number:
        print("Too low.")
    else:
        print("Correct!")
        break
        
"""""
"""""
#Task 4.5 Write a program that asks the user for a username and password. 
If either or both are incorrect, the program ask the user to enter the username 
and password again. This continues until the login information is correct or 
wrong credentials have been entered five times. If the information is correct, 
the program prints out Welcome. After five failed attempts the program prints out 
Access denied. The correct username is python and password rules.
"""""
"""""

username = "python"
password = "rules"
times_asked = 0

while True:
    given_username = input("Enter username: ")
    given_password = input("Enter password: ")
    if given_username == username and given_password == password:
        print("Welcome!")
        break
    else:
        print("Username and password are wrong.")
    times_asked += 1
    if times_asked > 4:
        print("Access denied.")
        break
"""""
""""""
# Task4.6
#Implement an algorithm for calculating an approximation for the value of pi (π).
# Let's assume that A is a unit circle. A unit circle has the radius of one and it
# is centered at the origin (0,0). Smallest possible square B is drawn around the
# unit circle so that circle A is completely inside the square. The corners of
# the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1). If a large number of
# random points are scattered inside the square, the fraction of points that fall
# inside the circle A correlates with the fraction of the area of circle A compared
# to the area of square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a simple method
# for calculating an approximation of the value of pi: Let's generate a large number
# of random points, such as one million, inside square B. Let N be the total number
# of random points. Each point inside the square is tested for whether it resides
# inside circle A. Let n be the total number of points that fall inside circle A.
# Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program that asks the user
# how many random points to generate, and then calculates the approximate value of pi
# using the method explained above. At the end, the program prints out the
# approximation of pi to the user. (Notice that it is easy to test if a point falls
# inside circle A by testing if it fulfills the inequation x^2+y^2<1.).
"""""
"""
"""
N = int(input("Enter amount of times to run: "))
n = 0

run_times = 0

while (run_times < N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1.0:
        n += 1

    run_times += 1

pi = 4 * n / N

print(f"Approximation of pi is {pi}")



""""""
"""
""""

number = input("Please type in a number: ")
if number > 100:
    print("The number was greater than one hundred")
    print("Now its value has decreased by one hundred")
    print("Its value is now"+ number)
print(number + " must be my lucky number!")
print("Have a nice day!")

"""
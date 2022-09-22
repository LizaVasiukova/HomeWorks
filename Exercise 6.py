import random
import math

# Task 6.1
"""""
def roll_dice():
    number = random.randint(1, 6)
    return number


while True:
    throw_result = roll_dice()
    print(throw_result)
    if throw_result == 6:
        break
"""""
# Task 6.2
"""""
def roll_dice(number_of_sides):
    number = random.randint(1, number_of_sides)
    return number


number_of_sides = int(input("Provide with the number of the sides: "))

while True:
    throw_result = roll_dice(number_of_sides)
    print(throw_result)
    if throw_result == number_of_sides:
        break
"""""

# Task 6.3

# 1 gallon  = 3.78541l
"""""
def volume(gallons):
    amount = gallons * 3.78541
    return amount


while True:
    gallons = float(input("Volume in gallons: "))
    if gallons < 0:
        break
    print(f"Amount in litres {volume(gallons)}")
"""""

# Task 6.4
"""""
def sum_of_numbers(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

numbers = [1, 2, 3, 4, 5]

print(sum_of_numbers(numbers))
"""""

# Task 6.5

"""""
def even_list(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
print(even_list(numbers))
"""""

# Task 6.6
"""""
def meter_price(diameter, price):
    diameter = diameter / 100
    pizza_area = ((diameter / 2) ** 2) * math.pi
    price_per_m2 = price / pizza_area
    return price_per_m2


price1 = float(input("What is the price of the pizza?: "))
pizza_size1 = float(input("What is the diameter of pizza in cm?: "))
price2 = float(input("What is the price of the second pizza?: "))
pizza_size2 = float(input("What is the diameter of the second pizza in cm?: "))


meter_price_pizza1 = meter_price(pizza_size1, price1)
meter_price_pizza2 = meter_price(pizza_size2, price2)

if meter_price_pizza1 < meter_price_pizza2:
    print(f"First pizza has a better value per meter, which is {round(meter_price_pizza1, 2) }")
else:
    print(f"Second pizza has a better value per meter, which is {round(meter_price_pizza2, 2)}")

"""""

# Task 7.1
"""""
seasons = ("winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter")
month_number = int(input("Enter the number of the month: "))
season = seasons[month_number-1]
print(f"The season is {season}!")

"""""

# Task 7.2
""""

names = set()

while True:
    name = input("Please enter a name: ")
    if name == "":
        break
    if name in names:
        print("Existing name")
    else:
        print("New name")
    names.add(name)

for i in names:
    print(i)

"""


# Task 7.3

airports = {}

while True:
    task = int(input("Would you like to: 1. Enter a new airport\n 2. Fetch the information of an existing airport\n 3. Quit\n Choose a number: "))
    if task == 1:
        new_airport_name = input("Enter new airport name: ")
        new_airport_icao = input("Enter the ICAO of the new airport: ")
        airports[new_airport_icao] = new_airport_name

    elif task == 2:
        icao_code = input("Which ICAO code would you like to fetch?: ")
        print(airports[icao_code])
    elif task == 3:
        break
import random
# 5.1 Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the the sum
# of the numbers. Use a for loop.

""""
n = int(input("How many time would you like to roll a dice?"))
dice_sum = 0
for i in range(n):
    dice = random.randint(1, 6)
    print(str(dice), end=" ")   #check the dice is valid
    dice_sum = dice_sum + dice
print(f"\nThe sum of the dices: {dice_sum}")

# 5.2 Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order. Hint:
# You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
""""""""
numbers = []       #we would like to have a list. Example: [0, 1, 3]
number = "Enter a number"
s = input(number)
while a != "":
    numbers.append(float(s))
    s = input(number)
numbers.sort(reserve=True)
print(numbers[0:5])      #print(numbers[0]) print(numbers[1]) print(numbers[2]) 0:5 prints 0 to 4
"""""
#5.3 Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
#For example, number 13 is a prime number as can only be divided by 1 or 13 so that the result is an integer.
#On the other hand, number 21 for example is not a prime number as it can be also be divided by numbers 3 and 7.

n = int(input("Provide the number: "))
if n > 1:
   for i in range(2, int(math.sqrt(n))+1):
    if


#5.4 Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading
# the names) and stores them into a list structure. Finally, the program prints out the names of the
# cities one by one, one city per line, in the same order they were read as input. Use a for loop for asking
# the names and a for/in loop to iterate through the list.

cities = []
for n in range(5):
    cities.append(input("Enter the name of the city"))
for city in cities:
    print(city)

import random

# Exercise 9.1


class Car:
    def __init__(self, number, max_speed):
        self.number = number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


car1 = Car("ABC-123", 142)

print (f"The car's registration number is {car1.number:s} and it's maximum speed is {car1.max_speed:d} and it's current\n"
       f"speed is {car1.current_speed} and it's travelled distance is {car1.travelled_distance}.")

import random

"""""
# Exercise 9.2

class Car:
    def __init__(self, number, max_speed):
        self.number = number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed):
        new_speed = self.current_speed + speed
        new_speed = min(self.max_speed, new_speed)
        new_speed = max(0, new_speed)
        self.current_speed = new_speed

    def print_speed(self):
        print(f"The current speed is: {self.current_speed}")


car1 = Car("ABC-123", 142)

car1.accelerate(30)
car1.print_speed()
car1.accelerate(70)
car1.print_speed()
car1.accelerate(50)
car1.print_speed()
car1.accelerate(-200)
car1.print_speed()

"""
"""""
# 9.3
class Car:
    def __init__(self, number, max_speed):
        self.number = number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed):
        new_speed = self.current_speed + speed
        new_speed = min(self.max_speed, new_speed)
        new_speed = max(0, new_speed)
        self.current_speed = new_speed

    def print_speed(self):
        print(f"The current speed is: {self.current_speed}")

    def drive(self, hours):
        travelled_way = hours * self.current_speed
        self.travelled_distance += travelled_way

    def print_drive(self):
            print(f"The current travelled distance is: {self.travelled_distance}")

car1 = Car("ABC-123", 142)

car1.accelerate(30)
car1.print_speed()
car1.accelerate(70)
car1.print_speed()
car1.accelerate(50)
car1.print_speed()
car1.accelerate(-200)
car1.print_speed()


car1.drive(1.5)
car1.print_drive()

"""

"""""
# 9.4

class Car:
    def __init__(self, number, max_speed):
        self.number = number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed):
        new_speed = self.current_speed + speed
        new_speed = min(self.max_speed, new_speed)
        new_speed = max(0, new_speed)
        self.current_speed = new_speed

    def print_speed(self):
        print(f"The current speed is: {self.current_speed}")

    def drive(self, hours):
        travelled_way = hours * self.current_speed
        self.travelled_distance += travelled_way

    def print_drive(self):
        print(f"The current travelled distance is: {self.travelled_distance}")


cars = []
for i in range(10):
    speed = random.randint(100, 200)
    registration_number = "ABC-" + str(i)
    car = Car(registration_number, speed)
    cars.append(car)

max_distance = 0

while True:
    for car in cars:
        new_speed = random.randint(-10, 15)
        car.accelerate(new_speed)
        car.drive(1)
        max_distance = max(max_distance, car.travelled_distance)

    if car.travelled_distance >= 10000:
        break

for car in cars:
    print(f"{car.number} {car.travelled_distance}")

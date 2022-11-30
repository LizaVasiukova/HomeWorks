from tabulate import tabulate
import random


# Task 10

"""
class Elevator:
    def __init__(self, top_floor, bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        return self.current_floor

    def floor_down(self):
        self.current_floor -= 1
        return self.current_floor

    def go_to_floor(self, floor):
        while self.current_floor != floor:
            if self.current_floor < floor:
                self.floor_up()
            else:
                self.floor_down()
            print(f"Elevator is on the {self.current_floor} floor.")


class Building:
    def __init__(self, top_floor, bottom_floor, number_of_elevators):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.number_of_elevators = number_of_elevators
        self.elevators = []
        for x in range(number_of_elevators):
            elevator = Elevator(top_floor, bottom_floor)
            self.elevators.append(elevator)

    def run_elevator(self, number_of_elevator, destination_floor):
        elevator = self.elevators[number_of_elevator]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


"""

"""
# Task 10.1
h = Elevator(12, 1)
h.go_to_floor(5)
h.go_to_floor(h.bottom_floor)
print(f"Elevator reached the target and it is on the {h.current_floor} floor.")

# Task 10.2
b = Building(100, 0, 3)
b.run_elevator(2, 89)

# Task 10.3
b.fire_alarm()
"""


class Car:
    def __init__(self, number, max_speed, max_distance):
        self.number = number
        self.max_speed = max_speed
        self.max_distance = max_distance
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
        if self.travelled_distance > self.max_distance:
            self.travelled_distance = self.max_distance

    def print_drive(self):
            print(f"The current travelled distance of car number {self.number} is: {self.travelled_distance}")




class Race:
    def __init__(self, name, distance, cars_list):
        self.name = name
        self.distance = distance
        self.cars_list = cars_list


    def hour_passes(self):
        for car in self.cars_list:
            change_of_speed = random.randint(-10, 300)
            car.accelerate(change_of_speed)
            car.drive(1)


    def print_status(self):
        car_list_table = []
        for car in self.cars_list:
            car_list_table.append([f'Car {car.number}', car.travelled_distance, car.current_speed])
        print(tabulate(car_list_table, headers=['Player', 'Distance', 'Speed'], tablefmt='fancy_grid'))

    def race_finished(self):


race_distance = 115
cars_list = []
for x in range(50):
    car = Car(x, 300, race_distance)
    cars_list.append(car)

r = Race("pasta", race_distance, cars_list)

r.hour_passes()
r.print_status()

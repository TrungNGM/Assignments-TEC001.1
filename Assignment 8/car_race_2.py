class Car:
    def __init__ (self, registration_number, max_speed,):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, speed):
        self.current_speed += speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
    def print_status(self):
        for car in self.cars:
            print(f"Registration Number: {car.registration_number}, Maximum Speed: {car.max_speed} km/h, Current Speed: {car.current_speed} km/h, Travelled Distance: {car.travelled_distance} km")
    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

import random
cars = []
for i in range(1,11):
    car = Car(f"ABC-{i}", random.randint(150, 200))
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
    hours += 1
    race.hour_passes()

    if hours % 10 == 0:
        race.print_status()

print("\nFinal Results:")
race.print_status()
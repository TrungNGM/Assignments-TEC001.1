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
import random
cars = []
for i in range(1,11):
    car = Car(f"ABC-{i}", random.randint(150, 200))
    cars.append(car)
race = True
while race:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_distance >= 10000:
            race = False
            break
cars.sort(key=lambda car: car.travelled_distance, reverse=True)    
for car in cars:
    print(f"Registration Number: {car.registration_number}, Maximum Speed: {car.max_speed} km/h, Final Current Speed: {car.current_speed} km/h, Final Travelled Distance: {car.travelled_distance} km")


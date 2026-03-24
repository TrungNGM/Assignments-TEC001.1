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

car = Car("ABC-123", 142)


print(f'Registration Number: {car.registration_number}')

print(f'Max Speed: {car.max_speed} km/h')

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
car.drive(1.5)
print(f'Speed Before Brake: {car.current_speed} km/h')

car.accelerate(-200)
print(f'Speed After Brake: {car.current_speed} km/h')


print(f'Travelled Distance: {car.travelled_distance} km')

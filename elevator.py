class Elevator:
    def __init__ (self, bottom_floor, top_floor,):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    
    def floor_down(self):
        self.current_floor -= 1
        print(f'Current Floor: {self.current_floor}')
    
    def floor_up(self):
        self.current_floor += 1
        print(f'Current Floor: {self.current_floor}')
    
    def go_to_floor(self, floor):
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()

class Building:
    def __init__(self, nums_of_bottom_floor, nums_of_top_floor, nums_of_elevators):
        self.nums_of_bottom_floor = nums_of_bottom_floor
        self.nums_of_top_floor = nums_of_top_floor
        self.elevators = []

        for i in range(nums_of_elevators):
            elevator = Elevator(self.nums_of_bottom_floor, self.nums_of_top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.elevators[elevator_number]
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.nums_of_bottom_floor)


h = Building(0, 10, 3)

h.run_elevator(0, 5)
h.run_elevator(1, 7)
h.run_elevator(2, 3)

print("FIRE ALARM!")

h.fire_alarm()
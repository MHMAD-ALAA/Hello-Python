from datetime import datetime
from car import Car
from person import Person
from office import Office
from main import empDict


class Employee(Person, Office, Car):
    employeesNum = 0
    distance_to_work = 0

    def __init__(self, name, money, mood, id, car, email, salary, distance_to_work, health_rate):
        super().__init__(name, money, mood, health_rate)
        self.id: str = id
        self.car: str = car
        self.email: str = email
        self.salary: int = salary
        Employee.distance_to_work = distance_to_work
        Employee.employeesNum += 1
        empDict[name] = id

    def work(self, hours):
        if hours == 8:
            return "happy"
        elif hours > 8:
            return "tired"
        else:
            return "lazy"

    def drive(self, distance, instance=0):
        """Give the order to (run-fun -> car-cls) and give it distance and velocity"""
        time_now = datetime.now().strftime("%H")
        time_now = int(time_now)
        velocity = distance / abs(time_now - 9)
        Car.run(self, velocity, instance)

    def refuel(self, gas_amount=100):
        """add gasAmount to (fuelRate-var -> car-cls)"""
        Car.fuel_rate += gas_amount
        return Car.fuel_rate



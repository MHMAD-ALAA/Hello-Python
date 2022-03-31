from employee import Employee


class Car(object):
    fuel_rate = 0

    def __init__(self, name, fuel_rate, velocity):
        self.name: str = name
        self.velocity: int = velocity
        Car.fuel_rate = fuel_rate

    def run(self, _velocity, distance):
        self.fuel_rate -= (Car.fuel_rate * (distance / 100))
        self.velocity = _velocity
        remain_distance = max(0, Employee.distance_to_work - distance)
        Car.stop(self, remain_distance)

    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance == 0:
            print("Arrive the destination!")
        else:
            print("The remaining destination is: {} KM".format(remain_distance))

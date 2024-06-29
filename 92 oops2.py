#Define a property that must have the same value for every class instance
class Vehicle:
    Color="White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
class Car(Vehicle):
    pass

sb=Bus("Volvo",120,23)
print(sb.name,sb.Color,sb.max_speed,sb.mileage)

od=Car("Swift",90,41)
print(od.name,od.Color,od.max_speed,od.mileage)


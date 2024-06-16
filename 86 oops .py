# Determine if School_bus is also an instance of the Vehicle class

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
class Bus(Vehicle):
     def fare(self):
        amount=super().fare()
        amount+=amount*0.1
        return amount

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus,Vehicle))
print(type(School_bus))
print("Total Bus fare is:", School_bus.fare())

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

School_bus=Bus("Volvo",120,23)
print(School_bus.name,School_bus.Color,School_bus.max_speed,School_bus.mileage)

Maruti=Car("Swift",90,41)
print(Maruti.name,Maruti.Color,Maruti.max_speed,Maruti.mileage)


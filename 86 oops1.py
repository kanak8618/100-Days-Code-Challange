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


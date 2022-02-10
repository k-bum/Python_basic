class Car() :
    def __init__(self, fuel = str, wheels = str) :
        self.fuel = fuel
        self.wheels = wheels
    
class Bike(Car) :
    def __init__(self, fuel, wheels, size = int) :
        super().__init__(fuel, wheels)
        self.size = size
    
bike = Bike("gas", 2, "small")
print(bike.fuel, bike.wheels, bike.size)

class Tires:
    def __init__(self, size):
        self.size = size

class CityTires(Tires):
    def __init__(self):
        super().__init__(15)

    def tire_type(self):
        print('The car is equipped with city tires whose size 15.')

class OffRoadTires(Tires):
    def __init__(self):
        super().__init__(18)

    def tire_type(self):
        print('The car is equipped with off road tires whose size is 18.')

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def start(self):
        print('The engine is powered by {}.'.format(self.fuel_type))

    def stop(self):
        print('The engine is stopped.')

    def get_state(self):
        print('The engine get stated.')

class GasEngine(Engine):
    def __init__(self):
        super().__init__('gas')

    def power_fuel(self):
        print('The car is powered by gas.')

class ElectricEngine(Engine):
    def __init__(self):
        super().__init__('electric')

    def power_fuel(self):
        print('The car is powered by electricity.')

class Vehicle:
    def __init__(self,engine, tires, VIN = 'a123'):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires

    def tire_type(self):
        pass

    def power_fuel(self):
        pass


car1 = Vehicle(ElectricEngine,CityTires)
print('*'*20 + 'Car 1 Details' + '*'*20)
car1.engine = ElectricEngine()
car1.engine.power_fuel()
car1.tires = CityTires()
car1.tires.tire_type()

car2 = Vehicle(GasEngine,OffRoadTires)
print('*'*20 + 'Car 2 Details' + '*'*20)
car2.engine = GasEngine()
car2.engine.power_fuel()
car2.tires = OffRoadTires()
car2.tires.tire_type()

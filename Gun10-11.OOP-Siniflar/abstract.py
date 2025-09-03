from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass  

class Car(Vehicle):
    def drive(self):
        print("Araba yolda hızla ilerliyor.")

class Cycle(Vehicle):
    def drive(self):
        print("Bisiklet pedal çevirerek ilerliyor.")

car1 = Car()
cycle1 = Cycle()

car1.drive()
cycle1.drive()

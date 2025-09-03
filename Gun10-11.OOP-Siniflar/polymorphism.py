class Vehicle:
    def drive(self):
        print("Taşıt hareket ediyor.")

class Car(Vehicle):
    def drive(self):
        print("Araba yolda ilerliyor.")

class Bycycle(Vehicle):
    def drive(self):
        print("Bisiklet pedal çevirerek ilerliyor.")


Vehicles = [Vehicle(), Car(), Bycycle()]

for vehicle in Vehicles:
    vehicle.drive()   #method ortak ama farklı çalışır.

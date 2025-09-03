class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand     
        self.model = model      
        self.__speed = speed       # private

    def get_speed(self):
        return self.__speed

    def set_speed(self, yeni_speed):
        if yeni_speed >= 0:
            self.__speed = yeni_speed
        else:
            print("Hız negatif olamaz!")

car1 = Car("Toyota", "Corolla", 120)
print(car1.brand)        
print(car1.get_speed())    
car1.set_speed(150)        
print(car1.get_speed())
      

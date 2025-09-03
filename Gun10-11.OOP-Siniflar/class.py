from datetime import datetime

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def info(self):
        print(f"Araba: {self.brand} {self.model}, Yıl: {self.year}")
    
    def ages(self):
        return datetime.now().year - self.year

car1 = Car("Toyota", "Corolla", 2018)
car2= Car("Honda", "Civic", 2020)

car1.info()  
car2.info()  

print(f"{car1.brand} yaşı: {car1.ages()}")  

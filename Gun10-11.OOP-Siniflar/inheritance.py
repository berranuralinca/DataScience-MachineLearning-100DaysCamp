class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Marka: {self.brand}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model,doors):
        super().__init__(brand, model) 
        self.kapi_sayisi = doors

    def info(self):
        super().info()  
        print(f"Kapı Sayısı: {self.kapi_sayisi}")


car1 = Car("Toyota", "Corolla", 4)
car1.info()


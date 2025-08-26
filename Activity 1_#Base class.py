# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"Device: {self.brand} {self.model}"

# Derived class (Smartphone inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # Inheriting from Device
        self.os = os
        self.__storage = storage  # Encapsulation (private attribute)
    
    def phone_info(self):
        return f"{self.brand} {self.model} runs on {self.os} with {self.__storage}GB storage"
    
    # Encapsulation: getter & setter
    def get_storage(self):
        return self.__storage
    
    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage
        else:
            print("Invalid storage size!")

# Creating objects
phone1 = Smartphone("Apple", "iPhone 15", "iOS", 256)
phone2 = Smartphone("Samsung", "Galaxy S24", "Android", 512)

# Using methods
print(phone1.device_info())
print(phone1.phone_info())

# Using encapsulation
print("Old storage:", phone2.get_storage())
phone2.set_storage(1024)
print("Updated storage:", phone2.get_storage())

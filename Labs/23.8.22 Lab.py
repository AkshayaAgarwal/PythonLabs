class Vehicle:
    def __init__(self,brand,model,vtype,fuel_tank_size,fuel_level):
        self.brand = brand
        self.model = model
        self.vtype = vtype
        self.fuel_tank_size = fuel_tank_size
        self.fuel_level = fuel_level

    def Details(self):
        print(f"Car Brand\t:  {self.brand}\n")
        print(f"Car Model\t:  {self.model}\n")
        print(f"Car Type\t:  {self.vtype}\n")
    def Fulltank(self):
        print("Tank is Full")

    def Update_fuel_tank(self):

        while True:
            new_level = int(input("Enter the new fuel level: "))
            self.fuel_level = new_level
            if new_level < 0:
                print("Invalid")
            elif 3 < new_level <= self.fuel_tank_size:
                print(f"Amount of fuel = {new_level} litres")
                break
            elif new_level > self.fuel_tank_size:
                print("Fuel level exceeding tank limit.")
            else:
                print(f"WARNING! Amount of fuel = {new_level} litres")
                break

    def Get_fuel(self):
        while True:
            moreFuel = int(input("Enter the amount of fuel to add: "))
            Fuel2 = self.fuel_level + moreFuel
            #self.fuel_level += moreFuel
            if Fuel2 < self.fuel_tank_size:
                print(f"Fuel in tank = {self.fuel_level} litres")
                break
            elif Fuel2 == self.fuel_tank_size:
                Fulltank()
                break
            else:
                print("WARNING! Fuel level is exceeding tank capacity.")

    def Drive(self):
        print(f"WOW! I am Driving {self.model}.")

class Fuel(Vehicle):
    def FuelType(self):
        if self.vtype == "Sedan": print("Fuel type is Petrol.")
        if self.vtype == "SUV": print("Fuel type is Diesel.")

class Servicing(Vehicle):
    def FuelType(self):
        if self.brand == "Mercedez Benz": print("Rs.30,000 as maintenance fee.")
        if self.brand == "BMW": print("Rs. 35,000 as maintenance fee.")
        


car1 = Fuel("Mercedez Benz","Mercedez Benz SL 350","Sedan",66,60)
car2 = Fuel("BMW","BMW X1","SUV",70,66)
car3 = Servicing("Maruti Suzuki","Swift Dezire","Sedan",60,55)

print("CAR 1\n")
car1.Details()
car1.Fulltank()
car1.Update_fuel_tank()
car1.Get_fuel()
car1.Drive()
car1.FuelType()

print("CAR 2\n")
car2.Details()
car2.Fulltank()
car2.Update_fuel_tank()
car2.Get_fuel()
car2.Drive()
car2.FuelType()

print("CAR 3\n")
car3.Details()
car3.Fulltank()
car3.Update_fuel_tank()
car3.Get_fuel()
car3.Drive()
car3.FuelType()

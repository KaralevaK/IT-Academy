class Car:

    def __init__(self, model, color, type, regNumber, owner, fuelTankVolumeLitres, amountOfFuelLitres = 0, mileageKilometers = 0, averageFuelConsumption = 9.4):
        self.__model= model.upper()
        self.set_color(color)
        self.__type = type.upper()
        self.set_regNumber(regNumber)
        self.set_owner(owner)
        self.__fuelTankVolumeLitres = fuelTankVolumeLitres
        self.set_mileageKilometers(mileageKilometers)
        self.set_averageFuelConsumption(averageFuelConsumption)
        if amountOfFuelLitres <=  fuelTankVolumeLitres and amountOfFuelLitres > 0:
            self.__amountOfFuelLitres = amountOfFuelLitres
        elif amountOfFuelLitres > fuelTankVolumeLitres:
            self.__amountOfFuelLitres = fuelTankVolumeLitres
        else:
            self.__amountOfFuelLitres = 0
        
    def takeATrip(self, amount_km):
        servise_str = ""
        if amount_km < 0:
            amount_km = 0
        power_reserve = int(self.amountOfFuelLitres*100/self.averageFuelConsumption)
        if power_reserve == 0:
            print("The fuel tank is empty!")
        elif power_reserve < amount_km:
            amount_km = power_reserve
            servise_str = "Go to gas station!"
        if power_reserve >= amount_km:
            print(f"Car {self.regNumber} moves {amount_km} km. {servise_str}")
            self.mileageKilometers = self.mileageKilometers + amount_km
            if servise_str != "":
                self.__amountOfFuelLitres = 0
            else:
                self.__amountOfFuelLitres -= int(amount_km*self.averageFuelConsumption/100)
       
    def fillTheTank(self, count_litres):
        if self.__amountOfFuelLitres + count_litres <= self.__fuelTankVolumeLitres and count_litres > 0:
            self.__amountOfFuelLitres += count_litres
            print(f"The car {self.__regNumber} is filled with {count_litres} litres of fuel")
        elif count_litres < 0:
            print("fuel drain not available")
        else:
            print(f"The car {self.__regNumber} is filled with {self.__fuelTankVolumeLitres - self.__amountOfFuelLitres} litres of fuel")
            self.__amountOfFuelLitres = self.__fuelTankVolumeLitres
            

    def about_car(self):
        print(f"model: {self.model}, color: {self.color}, type: {self.type}, registration number: {self.regNumber}, owner: {self.owner},\n fuel tank volume: {self.fuelTankVolumeLitres} l, amount of fuel: {self.amountOfFuelLitres} l, mileage: {self.mileageKilometers} km, averageFuelConsumption: {self.averageFuelConsumption} l/ 100 km")

    def get_model(self):
        return self.__model
        
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color.upper()

    def get_type(self):
        return self.__type

    def get_regNumber(self):
        return self.__regNumber

    def set_regNumber(self,new_number):
        self.__regNumber = new_number.upper()

    def get_owner(self):
        return self.__owner

    def set_owner(self, new_owner):
        self.__owner = new_owner.upper()

    def get_fuelTankVolumeLitres(self):
        return self.__fuelTankVolumeLitres

    def get_amountOfFuelLitres(self):
        return self.__amountOfFuelLitres

    def get_mileageKilometers(self):
        return self.__mileageKilometers

    def set_mileageKilometers(self, new_mileage):
        self.__mileageKilometers = new_mileage
    
    def get_averageFuelConsumption(self):
        return self.__averageFuelConsumption

    def set_averageFuelConsumption(self, new_averageFuelConsumption):
        self.__averageFuelConsumption = new_averageFuelConsumption

    model = property(get_model)
    color = property(get_color, set_color)
    type = property(get_type)
    regNumber = property (get_regNumber, set_regNumber)
    owner = property(get_owner, set_owner)
    fuelTankVolumeLitres = property(get_fuelTankVolumeLitres)
    amountOfFuelLitres = property(get_amountOfFuelLitres)
    mileageKilometers = property(get_mileageKilometers, set_mileageKilometers)
    averageFuelConsumption = property(get_averageFuelConsumption, set_averageFuelConsumption)

if __name__ == "__main__":
    car1 = Car("mazda", "black", "passenger car", "1111 XX-7","Ivanov Ivan Ivanovich", 50, 0,2000)
    car1.about_car()
    print(f"These vehicle parameters cannot be changed: model: {car1.model}, type: {car1.type}, fuel tank volume: {car1.fuelTankVolumeLitres}")
    print(f"These vehicle parameters can be changed: color: {car1.color}, registration number: {car1.regNumber}, owner: {car1.owner},\n amount of fuel: {car1.amountOfFuelLitres} l, mileage: {car1.mileageKilometers} km, average fuel consumption: {car1.averageFuelConsumption} l/ 100 km")
    car1.takeATrip(100)
    car1.color = "red"
    car1.regNumber = "7777 ZZ-7"
    car1.owner = "Petrov Petr Petrovich"
    car1.fillTheTank(100)
    car1.takeATrip(25)
    car1.about_car()
    car1.takeATrip(2000)
    car1.about_car()
    car1.mileageKilometers = 100
    car1.averageFuelConsumption = 10
    car1.about_car()

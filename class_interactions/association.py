class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print(f"{self.model} is being driven.")


class Driver:
    def __init__(self, name):
        self.name = name

    def driver_car(self, car: Car):
        print(f"{self.name} is driving {car.model}")
        car.drive()


car1 = Car("Toyota Corolla")
car2 = Car("BMW X5")

driver = Driver("Mykola")

driver.driver_car(car1)
driver.driver_car(car2)

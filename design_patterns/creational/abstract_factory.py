from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass


class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass


class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on a modern chair."


class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on a Victorian chair."


class ModernSofa(Sofa):
    def lie_on(self):
        return "Lying on a modern sofa."


class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lying on a Victorian sofa."


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


def client_code(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    print(chair.sit_on())
    print(sofa.lie_on())


print("\nModern Furniture:")
client_code(ModernFurnitureFactory())

print("\nVictorian Furniture:")
client_code(VictorianFurnitureFactory())

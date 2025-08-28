class Room:
    def __init__(self, name):
        self.name = name

    def show_room(self):
        print(f"Room: {self.name}")


class House:
    def __init__(self, address):
        self.address = address
        self.rooms = [
            Room("Living Room"),
            Room("Kitchen"),
            Room("Bedroom"),
        ]

    def show_house(self):
        print(f"House at {self.address} has the following rooms:")
        for room in self.rooms:
            room.show_room()


house = House("123 Main Stree")
house.show_house()
del house

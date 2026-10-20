#Composition
class Room:
    def __init__(self, name):
        self.name = name
 
 
class House:
    def __init__(self, *room_names):
        # House creates its own rooms: they belong to it alone
        self.rooms = [Room(n) for n in room_names]
 
    def show(self):
        print("House has rooms:")
        for r in self.rooms:
            print(f" - {r.name}")
 
    def demolish(self):
        self.rooms.clear()  # destroying the whole destroys the parts
        print(f"House demolished. Rooms left: {len(self.rooms)}")
 
 
house = House("Kitchen", "Bedroom", "Bathroom")
house.show()
house.demolish()
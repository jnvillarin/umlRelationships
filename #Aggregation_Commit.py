#Aggregation
class Professor:
    def __init__(self, name):
        self.name = name
 
 
class Department:
    def __init__(self, name):
        self.name = name
        self.professors = []
 
    def add(self, professor):
        self.professors.append(professor)
 
    def show(self):
        print(f"{self.name} department:")
        for p in self.professors:
            print(f" - {p.name}")
 
 
lee = Professor("Dr. Lee")
cruz = Professor("Dr. Cruz")
cs = Department("Computer Science")
cs.add(lee)
cs.add(cruz)
cs.show()

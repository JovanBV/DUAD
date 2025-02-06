class Bus:
    

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) + 1 > self.max_passengers:
            print("There's no more space on the bus.")
        else:
            self.passengers.append(person)
            print(f"There's {len(self.passengers)} passanger now on the bus.")


    def subs_passenger(self):
        if len(self.passengers) - 1 < 0:
            print("There's no one on the bus.")
        else:
            self.passengers.pop()
            print(f"There's {len(self.passengers)} passanger on the bus.")


class Person:
    def __init__(self, name):
        self.name = name


bus_1 = Bus(2)
bus_2 = Bus(1)
person_1 = Person('Jovan')
person_2 = Person('Alex')
person_3 = Person('Pablo')
person_4 = Person('Jovany Vasquez')
person_5 = Person('Roberto')

bus_1.add_passenger(person_1)
bus_1.add_passenger(person_2)
bus_1.add_passenger(person_3)
bus_2.add_passenger(person_4)
bus_2.add_passenger(person_5)




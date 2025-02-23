#objects exercise 2 from the second book

class Bus:

    def __init__(self, num_seats):
        self.num_seats = num_seats
        self.bus_seats = ["free"] * num_seats
        self.travelers_count = 0


    def get_on(self, passenger_name):
        for i in range(self.num_seats):
            if self.bus_seats[i] == "free":
                self.bus_seats[i] = passenger_name
                self.travelers_count += 1
                print(f"traveler {passenger_name} has gotten on the bus")
                return
        print(f"the bus is full, traveler {passenger_name} did not board the bus")

    def get_off(self, passenger_name):
        for i in range(self.num_seats):
            if self.bus_seats[i] == passenger_name:
                self.travelers_count -= 1
                print(f"traveler {passenger_name} has gotten off the bus")
                return
        print(f"traveler {passenger_name} is not on the bus")

    def __str__(self):
        return f"seats: {self.bus_seats}, travelers on the bus: {self.travelers_count}"




num_seats = int(input("enter the number of seats on the bus: "))
passenger_name = input("enter traveler name: ")
bus = Bus(num_seats)

while True:
     print("\n choose and action")
     print("1 - get on the bus")
     print("2 - fet off the bus")
     print("3 - end the program")

     action = int(input("enter the action number: "))


     if action == 3:
        print("ending program....")
        break
     if action == 1:
        bus.get_on(passenger_name)
     if action == 2:
        bus.get_off(passenger_name)
     else:
        print("invalid action, please choose again")

     print(bus)
     passenger_name = input("enter traveler name: ")




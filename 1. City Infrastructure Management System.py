# Objective:
# The aim of this assignment is to apply the concepts of Object-Oriented Programming 
# in Python to build a simulated City Infrastructure Management System. This system 
# will incorporate classes, objects, methods, and data structures to manage different 
# aspects of a city, such as buildings, traffic, and events.

# Task 1: Vehicle Registration System

#     Problem Statement: Create a Python class Vehicle with attributes registration_number, 
# type, and owner. Implement a method update_owner to change the vehicle's owner. Then, 
# create a few instances of Vehicle and demonstrate changing the owner.

#     Code Example: Provide a basic structure for the Vehicle class without methods.

#     class Vehicle:
#         def __init__(self, reg_num, type, owner):
#             self.registration_number = reg_num
#             self.type = type
#             self.owner = owner

#     Expected Outcome: Completion of the Vehicle class with the update_owner method and a 
# demonstration script showing the creation of Vehicle objects and updating their owners.

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    
    def updateOwner(self, newOwner):
        self.owner = newOwner
        print(f"Succesfully changed owner to {newOwner}!")

Buick = Vehicle(123123, "Sedan", "Tom Selick")
print(Buick.owner)

BMW = Vehicle(907323, "Hatchback", "Albert Einstein")
print(BMW.owner)


Buick.updateOwner("Richard Wagner")
print(Buick.owner)


# Task 2: Event Management System Enhancement

#     Problem Statement: Extend an existing Event class by adding a feature to keep track of 
# the number of participants. Implement a method add_participant that increases the count and 
# a method get_participant_count to retrieve the current count.

#     Code Example: Basic Event class without participant tracking.

class Event:
    def __init__(self, name, date, participants):
        self.name = name
        self.date = date
        self.participants = participants #int

    def add_participants(self, num):
        self.participants += num
        print(f"Succesfully added {num} participants to {self.name}")

    def get_participants(self):
        print(f"The event {self.name} has {self.participants} participants!")

Birthday = Event("Birthday Party", "January 4th", 15)

print(Birthday.name, Birthday.date, Birthday.participants)

Birthday.add_participants(4)

Birthday.get_participants()



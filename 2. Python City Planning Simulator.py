# Objective:
# The aim of this assignment is to solidify understanding of Python's Object-Oriented 
# Programming concepts through the development of a simulated city planning system. 
# This system will integrate the use of classes, objects, inheritance, and file handling 
# to manage various city elements like buildings, traffic systems, and public events.

# Task 1: File Handling for Building Records

#     Problem Statement: Implement a system to handle building records using file operations. 
# Create a Building class and write a script to save and load building details to and from a file.
import os
import json

#     Code Example: Skeleton of the Building class.

class Building:


    def __init__(self, name, floors):
        global buildings
        self.name = name
        self.floors = floors
        print(f"You created a new building named {name}, with {floors} floors!")

    def writeToFile(filePath):
        print("Ok lets write buildings to your file...")
        with open(filePath, "w") as file:
            for building in buildings.values():
                file.write(f"{building.name},{building.floors}\n")
                    

    def loadFromFile(filePath):
        global buildings
        print("Ok lets load buildings from your file...")
        with open(filePath, "r") as file:
            for line in file:
                name, floors = line.strip().split(",")
                building = Building(name, floors)
                buildings[building.name] = building

buildings = {}

def addBuilding():
    global buildings
    name = input("What's the name of your building?")
    floors = input("How many floors are there in your building?")
    building = Building(name, floors)
    buildings[building.name] = building

def listBuildings():

    for building in buildings.values():
        print(f"{building.name}, {building.floors}")



while True:
    action = input("\nSelect an action: add, list, import, export, quit\n").lower()

    if action == "quit":
        print("Ok thanks for visiting our city!")
        break

    try:
        if action == "import":
            Building.loadFromFile("Files/forImport.txt")
            

        elif action == "add":
            addBuilding()
            
        elif action == "export":
            Building.writeToFile("Files/forExport.txt")

        elif action == "list":
            listBuildings()

    except Exception as e:
        print(f"An error occured: {e}")






    # Methods to save to file and load from file

#     Expected Outcome: A complete Building class with methods for saving to and loading details 
#     from a file. A script demonstrating saving multiple buildings to a file and then reading them back into the program.

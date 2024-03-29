# Objective:
# This assignment aims to strengthen your skills in Python Object-Oriented Programming 
# (OOP) and modular programming by building a simulation of city services. The 
# focus will be on using class variables and organizing code into modules, simulating 
# services like public transportation, park management, and city utilities.

# Task 1: Public Transportation Module

#     Problem Statement: Develop a Bus class as part of a public transportation module. 
# Use class variables to represent common attributes like city name and base fare. Implement 
# instance variables for specific attributes like route number and passenger capacity.

#     Expected Outcome: A Bus class with both class and instance variables, and a transportation 
# module to manage different bus routes. A test script should demonstrate creating bus instances 
# and accessing both class and instance attributes.

import pubtrans as pt

Lansdowne = pt.Bus(47, 100)
Roncesvalles = pt.Bus(504, 150)
Queen = pt.Bus(505, 150)

print(Lansdowne.baseFare)
print(Lansdowne.cityName)
print(Lansdowne.routeNum)
print(Queen.baseFare)
print(Roncesvalles.capacity)
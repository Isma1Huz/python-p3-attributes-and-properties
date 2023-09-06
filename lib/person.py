#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
       def __init__(self, name=""):
        if name == "":
            print("Name must be string between 1 and 25 characters.")
        elif type(name) in (int, float):
            print("Name must be string between 1 and 25 characters.")
        elif len(name) > 25 :
            print("Name must be string between 1 and 25 characters.")
        else:
            self.name = name

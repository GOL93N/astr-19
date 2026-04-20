# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:38:23 2026

@author: robgo
"""

#Code Journal 1 prompt 4


''' Write a Python program that declares a class describing your favorite 
animal. Have the data members of the class represent the following physical 
parameters of the animal: length of the arms (float), 
length of the legs (float), number of eyes (int), 
does it have a tail? (bool), is it furry? (bool). 
Write an initialization function that sets the 
values of the data members when an instance of the class is created. 
Write a member function of the class to print out and describe the 
data members representing the physical characteristics of the animal.
'''
class favAn:
    
    def __init__(self, animal, lenarm, lenleg, numeyes, hastail, hasfur):
        self.animal = animal
        self.lenarm = lenarm
        self.lenleg = lenleg
        self.numeyes = numeyes
        self.hastail = hastail
        self.hasfur = hasfur

    def dataPrint(self):
        
        return(f"favorite animal: {animal} \nLength of arms: {lenarm} inches\nLength of legs: {lenleg} inches\nNumber of eyes: {numeyes}\nA {animal} has a tail: {hastail}\nA {animal} is furry: {hasfur}")

animal = "Harbor Seal"
lenarm = 2.0
lenleg = 0.0
numeyes = 2
hastail = True
hasfur = True

my_favorite_animal = favAn(animal, lenarm, lenleg, numeyes, hastail, hasfur)

print(my_favorite_animal.dataPrint())

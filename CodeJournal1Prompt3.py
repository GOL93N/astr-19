# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:31:21 2026

@author: robgo
"""

#code journal 1 prompt 3

'''Write a Python program (.py file) 
that defines a function f(x) that returns x**3 + 8. 
In the main() function of the program, call f(x) with x = 9 
and print the result.  Use an if statement that executes if the 
result is larger than 27 and prints “YAY!”. 
Use if __name__ == “__main__”: to setup the 
program for the command line
'''

def function(x):
    num = (x**3) + 8
    return num
    
def main():
    x = 9
    print(function(x))
    if function(x) > 27:
        print("YAY!")
        
if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:14:42 2026

@author: robgo
"""

''' 
Write a Python program that writes out a table of the function sin(x) 
vs. x, where x is tabulated between 0 and 2 with a thousand entries. 
Follow the basic Python program structure, including a main program 
function and the if __name__ == “__main__” setup.
'''
import math
import numpy as np
from astropy.table import Table 
from astropy.io import ascii 

def main():
    x = np.linspace(0, (2 * math.pi), 1000)
    sinx = np.sin(x)
    data = Table([x,sinx],names=['X','Sin(X)'])
    ascii.write(data, 'table.txt', format='commented_header')
    data_in = ascii.read('table.txt')
    print(data_in)
    


if __name__ == "__main__":
    main()
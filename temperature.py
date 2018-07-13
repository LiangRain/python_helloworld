#!/usr/bin/env/python3
fahrenhert = 0 
while fahrenheit <= 250: 
    celsius = (fahrenheit - 32) / 1.8 #huashi zhuan wendu C
    print("{:5d}{:7.2f}".format(fahrenheit , celsius))
    fahrenheit = fahrenheit + 25 


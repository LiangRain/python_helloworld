#!/usr/bin/env python3
N = 3
sum = 0 
count = 0 
print("please input 3 number: ")
while count < N: 
    number = float(input())
    sum = sum + number
    count = count + 1 
average = sum / N 
print("N = {}, Sum = {}".format(N, sum))
print("Average = {:.2f}".format(average))

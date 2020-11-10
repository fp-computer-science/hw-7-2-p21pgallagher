# Author: PJG (AMDG) 11/9/2020

origstr = input("Write a 6 letter word. ")
oddstr = origstr[0::2]
evenstr = origstr[1::2]

print(oddstr[0:1] + "-" + oddstr[1:2] + "-" + oddstr[2:3])
print(evenstr[0:1] + "-" + evenstr[1:2] + "-" + evenstr[2:3])

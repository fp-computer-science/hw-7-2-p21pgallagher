# Author: PJG (AMDG) 11/9/2020

def isPalindrome(pal):
    return pal == pal[::-1]

pal = input("Write a word. ")
print(isPalindrome(pal))

print("Your word: " + pal)
print("Your word reversed: " + pal[::-1])

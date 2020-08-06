#https://www.youtube.com/watch?v=rfscVS0vtbw
#Day1
print("Hello World")
print(" ")

print("   /|")
print("  / |")
print(" /  |") 
print("/___|")
print(" ")

#print prints what is inside of the quotation marks, has to be in order
charater_name = "Tom"
charater_age = "50"
is_male = True
#This makes the variable, so if you want to change it without doing it manual use variables
print("There once was a man named " + charater_name + ", ")
print("he was " + charater_age + " years old. ")

charater_name = "Mike"
#you can cahnge variables threw out the "story"
print("He really liked the name " + charater_name + ", ")
print("but didn't like being " + charater_age + ".")
#a string is just plane text (the stuff inside the "")

print(" ")

phrase = "Giraffe Academy" 
print(phrase)
print(" ")

# \n makes a line break, \(insert character) will literally put that in
# after the variable put a "." then upper to make the whole string uppercase, or lower to make it lowercase
# (len(variable)) will tell you how many characters are inside those parenthesis


#Day2
print(phrase.index("G"))
#each letter in a string has a number, you can use print(phrase.index("")) to find its place
print(phrase.replace("Giraffe", "Elephant"))
#type print(phrase.replace("example", "example 2")) to replace words
print(" ")

print(2)
print(" ")
# + addition, - subtraction, / division, * multplication, % gives you remander, and oder of operations,
#print(pow(3, 2)) this will do the power of a number
# can do math (does not need "")
print(12 * 12 + 1 - 21)
print(" ")
print(10 % 3)
print(" ")
#To be able to print numbers you must use print(str(*Number*)+ "text")
print(pow(3, 2))
print(" ")
print(round(4859.56866748)) #this will round it
print(" ")
from math import *
#this is importing other math functions, will give a lot more math functions
#sqrt is square root
print(sqrt(36))
print(" ")

name = input("Enter your name: ")
print("Hello " + name +"!")
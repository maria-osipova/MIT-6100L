# objects in memory have types  
types tell Python what operations you can do with the objects  
expressions evaluate to one value and involve objects and operations  
vars bind names and objects  
var = type(5*4)  
var >> int

strings
a sequence of case sensitive characters  
enclose in quotation marks  
a = "me"  
b = 'you'  
concatenate and repeat (a * 3) str  
s = 'abs'
len(s) = length of a string

slicing to get one char in a string:

s[0] = a  
s[1] = b  
s[3] = error  
s[-1] = c  
s[len(s) - 2] = b  
you can slice to get substring starting from one index up to other char
[start:stop:step]  
[start:stop] step = q by default  
s='abcdefgh'  
s[3:6] - without including the 6th elem = 'def'  
s[4:1:-2] = 'ec'  
s[::-1] = 'hgfedcba'

a = 'hehe'
b = 3
c = 'jjsjsjjs'  
print(a + b+ c) = an TypeError  
print(a + str(b) + c)

num1 = input("Type a number: ")  
print(5 * num1) = 33333  
num2 = int(input("Type a number: "))  
print(5 * num2) = 15  
f-string: (available starting with python 3.6) formatted string literal: anything that can be appear in a normal string literal, expressions bracketed by curly braces {}

# conditions for branching

in CS, there are two notions of equal  
variable = value  
2 == 3 >> False  

we can do the same thins with strings:  
'a' == 'A' >> False  

and, or  

![True/False val](Lectures-notes/pics/Screenshot 2025-05-06 at 1.29.58 PM.jpeg)  

<img src="Lectures-notes/pics/Screenshot 2025-05-06 at 1.29.58 PM.jpeg" alt="True/False val">


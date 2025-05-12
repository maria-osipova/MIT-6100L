objects in memory have types
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


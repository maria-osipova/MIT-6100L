programming is practice! do not give up if you can't do something

`types of knowledge:` 

- Declarative kn (statement of fact)
- Imperative kn (how to)

Programming is about writing recipes to generates facts.

algorythm: 
1) sequence of simple steps 
2) flow to control
3) a determinator when to stop

algorythm = recipe

anything computable in one language is computable in another
premitve constructs: words, language

- syntax "hi" 5 (not valid), "hi"*5 (valid)
- static semantics: english: "I are hungry" (syntactically valid but static semantic error); PL: "hi"+5: idem
- semantics: no multiple meanings. problem comes in with semantics

program: in the shell(console)/file

create data objects inside the program and then manipulate them:

- `scalar` [int {-1, 300}, float {real numbers 3.27, -500.0}, bool truth value {T/F}, NoneType - None]
- `no-scalar` [] 

type (5) = int; type(3.0) = float

```python3 -c "print(type(4.0))"```

``float(3)``

``round(5.9)``

``float(round(7.2))``

``type(3+2)``

python reads the expression but doesn't store the expression, but their values.

BIG IDEA
replace complex expressions by ONE value

3+2 = 5

``type((4+2)*6-1) >> int``

``float((4+2)*6-1) >> 35.0``

``int(1/2) >> 0``

- 5//3 >> 1 - getting the integer portion of the division
- 5%3 >> 2 - the remainder
- 2**3 >> 8

so many objects, what can we do with them? >> to start assigning name for them

a = 2
temp = 100.4

math variables = abstract, can represent maany values
CS var = one single value

= sigh is the assignment

pi (var) = 355/113 (value)

6 = x is bad
x*z = 4 is bad too

it's a lot easier to read clear codes
>code needs to read tomorrow, next year by anyone, don't start with a number, not single car, with comments

we can re-bind the var (previous val may still stored in memory but lost the handle for it)

radius = 2.2
radius = radius+1

https://pythontutor.com/visualize.html#mode=edit (very useful debugger)





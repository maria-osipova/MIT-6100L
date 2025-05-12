#newton's method
#find a root of a polinomial
#e.g., find g such that f(g, x) = g^3 - x = 0
#algorythm uses successive approximation:
#next_guess = guess - (f(guess))/(f'(guess))

x = int(input('What x to find the cube root of? '))
g = int(input('What guess to start with? '))

next_g = g - (g**3 - x)/(3*g**2)
print('Next guess to try =', next_g)
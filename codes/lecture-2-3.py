num = 3000
fraction = 1/3

print(num*fraction, 'is', fraction*100,'% of', num) #',' before the '% of' introduces the extra space: 1000.0 is 33.33333333333333 % of 3000
print(num*fraction, 'is', str(fraction*100) + '% of', num)
print(f'{num*fraction} is {fraction*100}% of {num}')
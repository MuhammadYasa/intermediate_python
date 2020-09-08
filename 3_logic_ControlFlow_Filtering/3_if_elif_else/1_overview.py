"""
Comparasion operators
< , > , >= , <= , == , !=

Boolean operators
and, or, not

Conditional Statements
if, else, elif

if condition:
    expression

if condition:
    expression
elif condition:
    expression
else:
    expression
"""

z = 4
if z % 2 == 0: # True
    print('z is even')

if z % 2 == 0:
    print('Checking' + str(z))
    print('z is even')

y = 5
if y % 2 == 0: # false
    print('y is even')
else:
    print('y is odd')

a = 3
if a % 2 == 0:
    print('a is divisible by 2')    # false
elif a % 3 == 0:
    print('a is divisible by 3')    # True
else:
    print('a is neither divisible by 2 nor by 3')


b = 6
if b % 2 == 0:
    print('b is divisible by 2')    # True
elif b % 3 == 0:
    print('b is divisible by 3')    # Never reached
else:
    print('b is neither divisible by 2 nor by 3')
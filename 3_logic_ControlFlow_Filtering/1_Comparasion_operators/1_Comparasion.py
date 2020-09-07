# numpy comparasion
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
print(bmi)

print(f'\n {bmi > 23}')

print(f'{bmi[bmi > 23]}')

# numeric comparasion
print(2 < 3)
print(2 == 3)
print(2 <= 3)
print(3 <= 3)

x = 2
y = 3
print(f'x < y = {x < y}')

# other comparasion
print(f"\ncarl < chris = {'carl' < 'crhis'}")
# print(f"3 < chris = {3 < 'chris'}")
print(f'3 < 4.1 ={3 < 4.1}')

print('\ncomparasion operator'
      '\n< strictly less than'
      '\n<= less than or equal'
      '\n> strictly greater than'
      '\n>= strictly greater or equal'
      '\n== equal'
      '\n!= not equal')

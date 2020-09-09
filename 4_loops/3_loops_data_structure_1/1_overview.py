"""
Dictionary

for var in seq:
    expression
"""
world = {"afghanistan" : 30.55,
    "albania" : 2.77,
    "algeria" : 39.21
}

for key, value in world.items():
    print(key + " -- " + str(value))

"""
numpy arrays
for var in seq:
    expression
"""
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
for val in bmi:
    print(val)

"""
2D Numpy arrays
"""
print('\n')
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height, np_weight])
for val in meas:
    print(val)

print('\n')
for val in np.nditer(meas):
    print(val)
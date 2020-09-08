import pandas as pd
brics = pd.read_csv("brics.csv", index_col=0)
# print(brics)

# get column
print('get column')
print(brics['area'])
print('\n')
print(brics.loc[:, 'area'])
print('\n')
print(brics.iloc[:,2])

# compare
print('Compare')

print(brics['area'])
print('\n')
print(brics['area'] > 8)
is_huge = brics['area'] > 8

# subset DF
print('\n')
print(brics[is_huge])
print('\n')
print(brics[brics['area'] > 8])

print('\n')
# boolean operators
import numpy as np
print(np.logical_and(brics['area'] > 8, brics['area'] < 10))

print(brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)])
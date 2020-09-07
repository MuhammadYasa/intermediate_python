# brics
import pandas as pd
brics = pd.read_csv('brics.csv', index_col=0)
print(brics)

print('\nprint colom tertentu')
print(brics['country']) # tapi masih ada yg ngikut tipe nya

print('\n')
print(brics[['country']])

print('\n')
print(brics[['country', 'capital']])

print('\n')
print(brics[1:4]) # melakukan print data ke 2 sampai ke 3

# row access loc
print('\n')
print(brics.loc['RU'])

print('\n')
print(brics.loc[['RU']])

print('\n')
print(brics.loc[['RU', 'IN', 'CH']])

# row and column loc
print('\n')
print(brics.loc[['RU', 'IN', 'CH'], ['country', 'capital']])

print('\n')
print(brics.loc[:, ['country','capital']]) # print dari awal sampai akhir / semuanya

# row access iloc

print('\n')
print(brics.iloc[1])

print('\n')
print(brics.iloc[[1,2,3]])

print('\n')
print(brics.iloc[[1,2,3],[0,1]])

print('\n')
print(brics.iloc[:, [0,1]])
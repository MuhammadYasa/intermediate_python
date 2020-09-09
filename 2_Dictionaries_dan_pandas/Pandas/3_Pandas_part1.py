dict = {
    "country": ["Brazil","Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.211],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

print('\n')

brics.index = ['BR', 'RU', 'IN', 'CH', 'SA']
print(brics)

print('\n')
brics = pd.read_csv("brics.csv")
print(brics)

print('\n')
brics = pd.read_csv("brics.csv", index_col=0)
print(brics)

brics.to_csv("data.csv")
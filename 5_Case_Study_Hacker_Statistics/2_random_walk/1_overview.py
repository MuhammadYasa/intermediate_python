import numpy as np
np.random.seed(123)
outcomes = []

for x in range(10):
    coin = np.random.randint(0,2)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")

print(outcomes)

# head or tails random walk
np.random.seed(123)
tails = [0]
for x in range(10):
    coins = np.random.randint(0,2)
    tails.append(tails[x] + coins)
print(tails)
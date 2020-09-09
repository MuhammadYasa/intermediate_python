import numpy as np
print(np.random.rand())    # Pseudo random numbers
print(np.random.seed(123))
print(np.random.rand())
print(np.random.rand())

# coin tos
print('coin tos')
np.random.seed(123)
coin = np.random.randint(0,2) # random generate 0 or 1
print(coin)
if coin == 0:
    print("heads")
else:
    print("tails")
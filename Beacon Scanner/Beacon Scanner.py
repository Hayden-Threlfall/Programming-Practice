import numpy as np
with open('input-large.txt') as f:
    input = f.readlines()
arr = np.eye(1,2,3) 
scan = list()
print(np.zeros(3,3,3))
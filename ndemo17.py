#NumPy Array Shape _ Reshape From 1-D to 2-D

import numpy as nparr

arr= nparr.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)

print(newarr)
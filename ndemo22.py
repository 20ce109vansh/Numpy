#Concatenating Arrays

import numpy as nparray1

array1= nparray1.array([(30,10,20),(110,101,102)])
array2 = nparray1.array([(24,31,22), (41,17,8)])

print('After concatenating:')
print(nparray1.concatenate((array1,array2),axis=1))
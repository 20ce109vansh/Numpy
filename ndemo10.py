#Access 3-D Arrays  _  Access the third element of the second array of the first array:

import numpy as nparr
arr= nparr.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
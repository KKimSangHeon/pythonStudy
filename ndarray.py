import numpy as np

data1 = [6,7.5,8,0,1]
arr1 = np.array(data1)
print(arr1)

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)

print(arr2)

A = np.array([
            [
                [0,1],
                [2,3],
                [4,5],
                [6,7]
            ],
            [
                [8,9],
                [10,11],
                [12,13]
            ]
           ])
Flattened_X = A.flatten()
print(Flattened_X)
print(A.ravel(order="C"))


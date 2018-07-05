import numpy as np

B = np.array([[142,56,189,65],
              [299,288,10,12],
              [55,142,17,18]
              ])

e0 = np.array([0,0,0,0])
e1 = np.array([0,3,2,1])
print(e0)
print(e1)



f = B[(e0,e1)]

print(f)
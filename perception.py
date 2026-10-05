import numpy as np
def perceptron(entrees, poids, biais):
    z = np.dot(entrees, poids) + biais    
    if z >= 0:                             
        return 1                           
    else:
        return 0                       
poids = np.array([0.5, 0.5])   
biais = -0.7

print(perceptron(np.array([1, 1]), poids, biais))   
print(perceptron(np.array([0, 0]), poids, biais))   
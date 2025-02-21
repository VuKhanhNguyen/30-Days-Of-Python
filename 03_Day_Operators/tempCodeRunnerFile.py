import numpy as np
def findY(x):
    return x**2 + 6*x + 9
    
x_val = np.arange(-10,10,1)
y_val = [findY(x) for x in x_val]

roots = np.roots([1,6,9])
print(f"Giá trị x: {x_val}")
print(f"Giá trị y: {y_val}\n")
print(roots)
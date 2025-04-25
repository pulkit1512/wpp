import numpy as np

arr = np.array(["apple", "banana", "cherry"])

print("Left-aligned:")
print([f"{x:_<15}" for x in arr])

print("Right-aligned:")
print([f"{x:_>15}" for x in arr])

print("Center-aligned:")
print([f"{x:_^15}" for x in arr])

import numpy as np

N = 10
points = np.random.rand(N, 2) * 100

for x, y in points:
    r = (x**2 + y**2)**0.5
    theta = np.arctan2(y, x)
    print(f"Point ({x:.2f}, {y:.2f}) -> Polar (r={r:.2f}, θ={theta:.2f})")

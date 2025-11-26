import numpy as np

data = np.loadtxt("output.csv", delimiter=",")
col1 = data[:, 0]
col2 = data[:, 1]
ratio = col2 / col1
avg = ratio.mean()

print(f"{avg:.2f} is the average difference in size")
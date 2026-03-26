import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("/home/A_Tam/projects/python/Labs/LV2/mtcars.csv",
                  "rb"), usecols=(1, 2, 3, 4, 5, 6), delimiter=",", skiprows=1)
plt.scatter(data[:, 0], data[:, 3], color='blue', s=data[:, 5]*15)
plt.title('mpg vs hp')
plt.xlabel('mpg')
plt.ylabel('hp')
plt.show()

print("mean mpg:", np.mean(data[:, 0]), "max mpg:", np.max(
    data[:, 0]), "min mpg:", np.min(data[:, 0]))


mpg6cyl = []

for list in data.tolist():
    if list[1] == 6:
        mpg6cyl.append(list[0])

print("for over 6 cylinders")
print("mean mpg:", np.mean(mpg6cyl), "max mpg:",
      np.max(mpg6cyl), "min mpg:", np.min(mpg6cyl))

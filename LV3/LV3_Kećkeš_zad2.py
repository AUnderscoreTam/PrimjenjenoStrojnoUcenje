import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


cars = pd.read_csv('mtcars.csv')
# a)
# cars.pivot(index="cyl", columns="car", values="mpg").plot(
#     kind="bar", ylabel="mpg", figsize=(16, 9))
# b)
# cars.pivot(index="cyl", columns="car", values="wt").plot(
#     kind="bar", ylabel="wt", figsize=(16, 9))
# c)
# cars.pivot(index="am", columns="car", values="mpg").plot(
#     kind="bar", ylabel="mpg", figsize=(16, 9))
# d)
cars.pivot(index="am", columns="car", values="vs").plot(
    kind="bar", ylabel="mpg", figsize=(16, 9))

plt.legend(loc="upper right", bbox_to_anchor=(1.1, 1))
plt.show()

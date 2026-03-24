import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cars=pd.read_csv('mtcars.csv')
carsF =cars.groupby("cyl")
print(carsF)
cars[(cars.cyl==4)|(cars.cyl==6)|(cars.cyl==8)].mpg.plot.bar(xlabel="mpg",ylabel="cyl") # NEDOVRŠENO
plt.show()
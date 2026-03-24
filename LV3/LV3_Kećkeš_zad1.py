import pandas as pd
import numpy as np

cars=pd.read_csv('mtcars.csv')

print(cars.sort_values("mpg").tail(5).car)
print("\n")
print(cars[cars.cyl==8].sort_values("mpg").head(3).car)
print("\n")
print(cars[cars.cyl == 6].mpg.mean())
print("\n")
print(cars[(cars.cyl == 4) & ((cars.wt>2.0) & (cars.wt <2.2))].mpg.mean())
print("\n")
print("automatska transmisija = ", cars[cars.am ==1].am.count())
print("rucna transmisija = ", cars[cars.am ==0].am.count())
print("\n")
print(cars[(cars.am==1) & (cars.hp > 100)].hp.count())
print("\n")
print(cars.wt.aggregate([sum])*2.20462262*1000)
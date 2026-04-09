import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1 6699 automobila
"""
2 str    
int64  
float64
int64  
str    
str    
str    
str    
float64
int64  
float64
int64 
"""
#3 automobil 2591 najvecu, a automobil 4778 najmanju cijenu
#4 575
#5 automobil 3067 najvise, a autmobil 6514 najmanje km

# ucitavanje ociscenih podataka
df = pd.read_csv('cars_processed.csv')
print(df.info())

print(df.selling_price.idxmax())
print(df.selling_price.idxmin())
count=0
for year in df.year:
    if year == 2012:
        count+=1
print(count)

print(df.km_driven.idxmax())
print(df.km_driven.idxmin())

dfseats=df.groupby(['seats']).agg(total_seats=('seats','sum'))
print(dfseats.info)


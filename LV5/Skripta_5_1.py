'''
Room occupancy classification 

R.Grbic, 2024.

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression

# a)da co2 povećabva sa temperatrurom, ali sporije kad je soba zauzeta i napoćetku je mali skok co2 kad je soba najhladnija 0
# b) 10129
# c) class 0= 0.8123210583473196 81%
# c) class 1= 0.18767894165268043 19%

# ucitaj podatke za ucenje
df1 = 0
df0 = 0
df = pd.read_csv('occupancy_processed.csv')
for numb in df['Room_Occupancy_Count']:
    if numb == 0:
        df0 += 1
    else:
        df1 += 1

print("class 0=", df0/len(df))
print("class 1=", df1/len(df))


feature_names = ['S3_Temp', 'S5_CO2']
target_name = 'Room_Occupancy_Count'
class_names = ['Slobodna', 'Zauzeta']

X = df[feature_names].to_numpy()
y = df[target_name].to_numpy()


# Scatter plot
"""
plt.figure()
for class_value in np.unique(y):
    mask = y == class_value
    plt.scatter(X[mask, 0], X[mask, 1], label=class_names[class_value])
plt.xlabel('S3_Temp')
plt.ylabel('S5_CO2')
plt.title('Zauzetost prostorije')
plt.legend()
plt.show()
"""
# 2)

# e)manja promjena daje boje rezultate ali prevelika promjena daje loše rezultate
# f)medel radi bolje sa skaliranim ulazim veličinama
dfX = df.drop(["Room_Occupancy_Count"], axis=1)
dfY = df["Room_Occupancy_Count"]
X_train, X_test, y_train, y_test = train_test_split(
    dfX, dfY, test_size=0.20, stratify=y)


scaler = StandardScaler()
scaler = scaler.fit_transform(X_train, y_train)

kn = KNeighborsClassifier(12)
kn.fit(X_train, y_train)
y_pred = kn.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,  display_labels=['Class  0',
                                                                    'Class 1'])
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

precision = precision_score(y_test, y_pred)
print("prec= ", precision)
# Izracunaj odziv
recall = recall_score(y_test, y_pred)
print("recall= ", recall)
# Izracunaj tocnost
accuracy = accuracy_score(y_test, y_pred)
print("accuracy= ", accuracy)

# 3)
scaler = StandardScaler()
scaler = scaler.fit_transform(X_train, y_train)

kn = DecisionTreeClassifier(max_depth=5)
kn.fit(X_train, y_train)
y_pred = kn.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,  display_labels=['Class  0',
                                                                    'Class 1'])
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.figure(3)
plot_tree(kn, fontsize=7, filled=True)
plt.show()


precision = precision_score(y_test, y_pred)
print("prec= ", precision)
# Izracunaj odziv
recall = recall_score(y_test, y_pred)
print("recall= ", recall)
# Izracunaj tocnost
accuracy = accuracy_score(y_test, y_pred)
print("accuracy= ", accuracy)

# 4)
lr = LogisticRegression(max_iter=50000)
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,  display_labels=['Class  0',
                                                                    'Class 1'])
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

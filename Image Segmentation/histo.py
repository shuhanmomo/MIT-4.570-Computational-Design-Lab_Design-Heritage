import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
scene_tp = ['Calm','Romantic','Happiness','Sadness']
path = f"D:\OneDrive\GSD4thTerm\Design Heritage\ASS1\output\{scene}\images_scores.csv"
df = pd.read_csv(path)
df = df.drop(['Unnamed: 0'],axis= 1)
df.head()


data = df.iloc[25][1:].to_dict()

names = list(data.keys())
values = list(data.values())
names_new =[]
values_new = []

values_st = sorted(values)

base = values_st[-20]

for i in range(len(names)):
    if values[i]>base:
        values_new.append(values[i])
        names_new.append(names[i])

print(values)
print(values_st)


y_pos = np.arange(len(names_new))
plt.figure(figsize=(10, 8))
plt.bar(y_pos,values_new, align='center', alpha=0.5)
plt.xticks(y_pos, names_new,rotation='vertical')
plt.ylabel('Proportion')
plt.show()

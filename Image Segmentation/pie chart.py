import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


locations = ['bostoncommon','kowloonpark','luxembourggardens']
location = locations[1]
path = f'D:\OneDrive\GSD4thTerm\Design Heritage\ASS3\{location}_predict.csv'
df = pd.read_csv(path)
df = df.drop(['Unnamed: 0'],axis= 1)
df.head()
class_num = len(df.columns)-1
means = []
headers = []
colours = {}
for i in range(class_num):
    header = df.columns[i+1]
    column_arr = df[header]
    column_mean = np.mean(column_arr)
    if column_mean - 0 > 0:
        means.append(column_mean)
        headers.append(header)
        colours[header] = f"C{i}"



means_dp = means[::]
means.sort()
headers_st = [x for _,x in sorted(zip(means_dp,headers))]
data = (means[-10:])
labels = headers_st[-10:]
data.reverse()
labels.reverse()

fig1, ax1 = plt.subplots(figsize=(10, 7))
fig1.subplots_adjust(0.3, 0, 1, 1)

theme = plt.get_cmap('jet')
ax1.set_prop_cycle("color", [theme(1.12 * i / len(means_dp))
                             for i in range(len(means_dp))])
for i in range(len(headers)):
    colours[headers[i]] = f'C{i}'


_, _ = ax1.pie(data, startangle=90, radius=1500,colors = [colours[key] for key in labels])

ax1.axis('equal')

total = sum(data)
plt.legend(
    loc='upper left',
    labels=['%s, %1.1f%%' % (
        l, (float(s) / total) * 100)
            for l, s in zip(labels, data)],
    prop={'size': 11},
    bbox_to_anchor=(0.0, 1),
    bbox_transform=fig1.transFigure
)

plt.show()



#if __name__ == '__main__':


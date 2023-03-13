import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
scene_tp = ['Calm','Romantic','Happiness','Sadness']
target = ['sky','sea','tree','water','person','building','wall','floor','ceiling','window']
results = {}
names = []
for scene in scene_tp:
    location = f"D:\OneDrive\GSD4thTerm\Design Heritage\ASS1\output\{scene}\images_scores.csv"
    df = pd.read_csv(location)
    df = df.drop(['Unnamed: 0'], axis=1)
    class_num = len(df.columns) - 1
    means = [0]*len(target)
    for i in range(class_num):
        header = df.columns[i + 1]
        if header in target:
            t_i = target.index(header)
            column_arr = df[header]
            column_mean = np.mean(column_arr)
            means[t_i] =column_mean
            if header not in names:
                names.append(header)
    means =[x/np.sum(means) for x in means]

    results[scene] = means

def survey(results, category_names):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.colormaps['RdBu'](
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
       # ax.bar_label(rects, label_type='center', color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(-0.1, 1.02),
              loc='lower left', fontsize='small')

    return fig, ax


survey(results, target)
plt.show()



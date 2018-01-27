from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('font', size=18)
machines =       ['SVM',   'MLP',   'RBM',   'SAE',   'WnD']
train_accuracy = [93.7322, 99.4230, 94.5055, 94.7194, 99.9999]
test_accuracy =  [81.5017, 87.3549, 86.4548, 88.0666, 90.3245]
width = 0.4
ind = np.arange(len(machines))

fig, ax = plt.subplots()

rects1 = ax.bar(ind, train_accuracy, width, color='b',
                hatch='/', label='Train')
rects2 = ax.bar(ind + width, test_accuracy, width, color='r',
                hatch='\\', label='Test')

ax.set_ylabel('Accuracy(%)')
ax.set_xlabel('Classifiers')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(machines)
ax.set_xlim([-0.5, len(machines)])
ax.set_ylim([78, 105])
plt.grid(linestyle=':')
plt.legend()


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.005*height,
                '%.1f' % height, ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
plt.tight_layout()
plt.savefig('comp_accuracy_unsw.pdf', fmt='pdf')
plt.show()

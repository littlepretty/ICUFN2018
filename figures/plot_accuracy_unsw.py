from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.005 * height,
                '%.1f' % height, ha='center', va='bottom')

matplotlib.rc('font', size=18)
machines =   ['SVM',   'MLP',   'RBM',   'SAE',   'WnD']
train_accu = [93.6306, 94.3630, 94.3947, 94.3969, 93.5365]
test_accu =  [81.5041, 86.9926, 87.0168, 86.7393, 90.3245]
train_std =  [0.00000, 0.23000, 0.00033, 0.00025, 2.28320]
test_std =   [0.00000, 1.01820, 0.00731, 0.01192, 3.17770]

width = 0.4
ind = np.arange(len(machines))
fig, ax = plt.subplots()
rects1 = ax.bar(ind, train_accu, width, yerr=train_std, color='b',
                hatch='/', label='Train')
rects2 = ax.bar(ind + width, test_accu, width, yerr=test_std, color='r',
                hatch='\\', label='Test')
ax.set_ylabel('Accuracy(%)')
ax.set_xlabel('Classifiers')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(machines)
ax.set_xlim([-0.5, len(machines)])
ax.set_ylim([65, 100])
plt.grid(linestyle=':')
plt.legend(loc='lower right')
autolabel(rects1)
autolabel(rects2)
plt.tight_layout()
plt.savefig('comp_accuracy_unsw.pdf', fmt='pdf')
plt.show()

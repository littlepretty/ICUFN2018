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

matplotlib.rc('font', size=20)
machines =       ['SVM',   'MLP',   'RBM',   'SAE',   'WnD']
train_accuracy = [99.2077, 99.3966, 99.4912, 99.3449, 99.7261]
test_accuracy =  [78.5353, 78.3521, 78.8347, 79.1519, 78.9567]
train_std =      [0.00000, 0.0246,  0.0231,  0.0216,  0.0121]
test_std =       [0.00000, 0.5162,  0.3499,  0.4215,  0.0813]

width = 0.4
ind = np.arange(0, len(machines))
fig, ax = plt.subplots()
rects1 = ax.bar(ind, train_accuracy, width, yerr=train_std,
                color='b', error_kw=dict(ecolor='g'),
                hatch='/', label='Train')
rects2 = ax.bar(ind + width, test_accuracy, width, yerr=test_std,
                color='r', error_kw=dict(ecolor='g'),
                hatch='\\', label='Test')
ax.set_ylabel('Accuracy(%)')
ax.set_xlabel('Classifiers')
ax.set_xticks(ind + width)
ax.set_xticklabels(machines)
ax.set_xlim([-0.5, len(machines)])
ax.set_ylim([65, 102])
plt.grid(linestyle=':')
plt.legend(loc='lower right')
autolabel(rects1)
autolabel(rects2)
plt.tight_layout()
plt.savefig('comp_accuracy_nsl.pdf', fmt='pdf')
plt.show()

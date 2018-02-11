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
machines =   ['SVM',   'MLP',   'RBM',   'SAE',   'WnD']
accuracy =   [81.5041, 86.8216, 87.1252, 88.0666, 91.1513]
precision =  [81.5000, 88.8800, 88.6200, 89.2700, 92.4562]
recall    =  [80.5000, 86.8200, 87.1300, 88.0700, 90.9821]
# train_accu = [93.6306, 94.3630, 94.3947, 94.3969, 93.5365]
# train_std =  [0.00000, 0.23000, 0.00033, 0.00025, 2.28320]
# test_std =   [0.00000, 1.01820, 0.00731, 0.01192, 3.17770]

width = 0.93
ind = np.arange(0, len(machines) * 3, 3)
fig, ax = plt.subplots()
rects1 = ax.bar(ind, accuracy, width, color='r', hatch='/', label='Accuracy')
rects2 = ax.bar(ind + width, precision, width, color='b', alpha=0.4,
                hatch='\\', label='Precision')
rects3 = ax.bar(ind + 2 * width, recall, width, color='g',
                hatch='-', label='Recall')

ax.set_ylabel('Testset Performance(%)')
ax.set_xlabel('Classifiers')
ax.set_xticks(ind + width)
ax.set_xticklabels(machines)
ax.set_xlim([-1.5, len(machines) * 3])
ax.set_ylim([60, 95])
plt.grid(linestyle=':')
plt.legend(loc='lower right')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.tight_layout()
# plt.savefig('comp_accuracy_unsw.pdf', fmt='pdf')
plt.show()

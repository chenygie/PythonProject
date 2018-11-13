import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import ShuffleSplit
from plot_learning_curve import plot_learning_curve
digits = load_digits()
X, y = digits.data, digits.target  # 加载样例数据

# 图一
title = r"Learning Curves (Naive Bayes)"
cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)
estimator = GaussianNB()  # 建模
plot_learning_curve(estimator, title, X, y, ylim=(0.7, 1.01), cv=cv, n_jobs=1)

# 图二
title = r"Learning Curves (SVM, RBF kernel, $\gamma=0.001$)"
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
estimator = SVC(gamma=0.001)  # 建模
plot_learning_curve(estimator, title, X, y, (0.7, 1.01), cv=cv, n_jobs=1)

plt.show()
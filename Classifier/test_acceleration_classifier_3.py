import numpy as np
from methods.data_load import load_data_acceleration
from numpy import ndarray
from sklearn import svm, tree, naive_bayes
from methods.load_my_data import read_my_data


target_list, data_list = load_data_acceleration('data_set2/train/y_train.txt',
                                                'data_set2/train/Inertial Signals/total_acc_x_train.txt',
                                                'data_set2/train/Inertial Signals/total_acc_y_train.txt',
                                                'data_set2/train/Inertial Signals/total_acc_z_train.txt')

data = ndarray(shape=(len(data_list), 12), dtype=float, buffer=np.asanyarray(data_list))
target = ndarray(shape=(len(target_list),), dtype=int, buffer=np.asanyarray(target_list))

clf = svm.SVC()
clf.fit(data, target)


data_list = read_my_data()
data = ndarray(shape=(1, 12), dtype=float, buffer=np.asanyarray(data_list))

y_predicted = clf.predict(data)
print("Number of mislabeled points out of a total %d points : %d" % (data.shape[0], (target != y_predicted).sum()))

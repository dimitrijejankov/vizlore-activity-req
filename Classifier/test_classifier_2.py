import numpy as np
from methods.data_load import load_data
from numpy import ndarray
from sklearn import svm, tree, naive_bayes

target_list, data_list = load_data('data_set2/train/y_train.txt',
                                   'data_set2/train/Inertial Signals/body_acc_x_train.txt',
                                   'data_set2/train/Inertial Signals/body_acc_y_train.txt',
                                   'data_set2/train/Inertial Signals/body_acc_z_train.txt',
                                   'data_set2/train/Inertial Signals/body_gyro_x_train.txt',
                                   'data_set2/train/Inertial Signals/body_gyro_y_train.txt',
                                   'data_set2/train/Inertial Signals/body_gyro_z_train.txt')


data = ndarray(shape=(len(data_list), 21), dtype=float, buffer=np.asanyarray(data_list))
target = ndarray(shape=(len(target_list),), dtype=int, buffer=np.asanyarray(target_list))

clf = tree.DecisionTreeClassifier()
clf.fit(data, target)

target_list, data_list = load_data('data_set2/test/y_test.txt',
                                   'data_set2/test/Inertial Signals/body_acc_x_test.txt',
                                   'data_set2/test/Inertial Signals/body_acc_y_test.txt',
                                   'data_set2/test/Inertial Signals/body_acc_z_test.txt',
                                   'data_set2/test/Inertial Signals/body_gyro_x_test.txt',
                                   'data_set2/test/Inertial Signals/body_gyro_y_test.txt',
                                   'data_set2/test/Inertial Signals/body_gyro_z_test.txt')

data = ndarray(shape=(len(data_list), 21), dtype=float, buffer=np.asanyarray(data_list))
target = ndarray(shape=(len(target_list),), dtype=int, buffer=np.asanyarray(target_list))

y_predicted = clf.predict(data)
print("Number of mislabeled points out of a total %d points : %d" % (data.shape[0], (target != y_predicted).sum()))

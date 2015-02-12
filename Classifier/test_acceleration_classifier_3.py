import numpy as np
from methods.data_load import load_data_acceleration
from methods.data_set_load_acceleration_wrist import load_data_set
from numpy import ndarray
from sklearn import svm, tree, naive_bayes


target_list, data_list = load_data_acceleration('data_set2/train/y_train.txt',
                                                'data_set2/train/Inertial Signals/total_acc_x_train.txt',
                                                'data_set2/train/Inertial Signals/total_acc_y_train.txt',
                                                'data_set2/train/Inertial Signals/total_acc_z_train.txt')

data = ndarray(shape=(len(data_list), 12), dtype=float, buffer=np.asanyarray(data_list))
target = ndarray(shape=(len(target_list),), dtype=int, buffer=np.asanyarray(target_list))

clf = tree.DecisionTreeClassifier()
clf.fit(data, target)

target_list, data_list = load_data_set('data_set/Participant_4.csv')
data = ndarray(shape=(len(data_list), 12), dtype=float, buffer=np.asanyarray(data_list))
target = ndarray(shape=(len(target_list),), dtype=int, buffer=np.asanyarray(target_list))

y_predicted = clf.predict(data)
print("Number of mislabeled points out of a total %d points : %d" % (data.shape[0], (target != y_predicted).sum()))

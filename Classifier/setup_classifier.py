import numpy as np
from methods.data_set_load import load_data_set
from numpy import ndarray
from sklearn.externals import joblib
from sklearn import svm, tree, naive_bayes

target_list, data_list = load_data_set('data_set/Participant_1.csv')
target_list1, data_list1 = load_data_set('data_set/Participant_2.csv')
target_list2, data_list2 = load_data_set('data_set/Participant_3.csv')
target_list3, data_list3 = load_data_set('data_set/Participant_10.csv')
target_list4, data_list4 = load_data_set('data_set/Participant_5.csv')
target_list5, data_list5 = load_data_set('data_set/Participant_6.csv')
target_list6, data_list6 = load_data_set('data_set/Participant_7.csv')
target_list8, data_list8 = load_data_set('data_set/Participant_9.csv')

target_list.extend(target_list1)
target_list.extend(target_list2)
target_list.extend(target_list3)
target_list.extend(target_list4)
target_list.extend(target_list5)
target_list.extend(target_list6)
target_list.extend(target_list8)

data_list.extend(data_list1)
data_list.extend(data_list2)
data_list.extend(data_list3)
data_list.extend(data_list4)
data_list.extend(data_list5)
data_list.extend(data_list6)
data_list.extend(data_list8)


data = ndarray(shape=(len(data_list), 21), dtype=float, buffer=np.asanyarray(data_list))
target = ndarray(shape=(len(target_list),), dtype=int, buffer=np.asanyarray(target_list))

clf = tree.DecisionTreeClassifier()
clf.fit(data, target)
joblib.dump(clf, '../ActivityRecognition/activity_server/classifier/classifier.pkl')


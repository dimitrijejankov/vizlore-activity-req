import numpy as np

from activity_server.models import DataRecord, AcceleratorRecord, GyroscopeRecord
from activity_server.utilities.sensor_features import get_acceleration_features, get_gyroscope_features
from numpy import ndarray
from sklearn.externals import joblib

clf = joblib.load('activity_server/classifier/classifier.pkl')


def find_record(uuid):

    record = DataRecord.objects.filter(user_id=uuid).latest('record_date')

    if record.activity_calculated:
        return record
    else:
        acceleration_data = AcceleratorRecord.objects.filter(data_record=record.id).order_by("time_stamp")
        acc_x, acc_y, acc_z = process_sensor_data(acceleration_data)
        acc_features = get_acceleration_features(acc_x, acc_y, acc_z)

        gyroscope_data = GyroscopeRecord.objects.filter(data_record=record.id).order_by("time_stamp")
        gyo_x, gyo_y, gyo_z = process_sensor_data(gyroscope_data)
        gyo_features = get_gyroscope_features(gyo_x, gyo_y, gyo_z)

        features = []
        features.extend(acc_features)
        features.extend(gyo_features)

        data = ndarray(shape=(1, 21), dtype=float, buffer=np.asanyarray(features))

        probability = clf.predict_proba(data)

        record.activity_calculated = True

        record.walking = probability[0][0]
        record.sitting = probability[0][1]
        record.standing = probability[0][2]
        record.jogging = probability[0][3]
        record.biking = probability[0][4]
        record.upstairs = probability[0][5]
        record.downstairs = probability[0][6]

        record.save()

        return record


def process_sensor_data(sensor_data):
    x = []
    y = []
    z = []

    current_time = sensor_data[0].time_stamp
    current_index = 0

    for i in xrange(0, 128):

        while current_time >= sensor_data[current_index].time_stamp and current_index != len(sensor_data) - 1:
            current_index += 1

        x.append(sensor_data[current_index - 1].x)
        y.append(sensor_data[current_index - 1].y)
        z.append(sensor_data[current_index - 1].z)

        current_time += 20

    return x, y, z
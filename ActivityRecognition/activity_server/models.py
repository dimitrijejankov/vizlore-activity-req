from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField
from django_mongodb_engine.contrib import MongoDBManager

"""
    1: "Sitting Hand"
    2: "Sitting Pocket"
    3: "Walking Hand"
    4: "Walking Pocket"
    5: "Standing Hand"
    6: "Standing Pocket"
    7: "Upstairs"
    8: "Downstairs"
"""

activity_table_json = {
    1: "sitting",
    2: "sitting",
    3: "walking",
    4: "walking",
    5: "standing",
    6: "standing",
    7: "upstairs",
    8: "downstairs"
}


class WifiEntry(models.Model):
    time_stamp = models.BigIntegerField()
    ssids = ListField()


class LocationEntry(models.Model):
    time_stamp = models.BigIntegerField()
    lat = models.FloatField()
    lon = models.FloatField()


class ActivityEntry(models.Model):
    svm_ech = ListField()
    svm = ListField()
    dt_ech = ListField()
    dt = ListField()


class DataRecord(models.Model):
    user_id = models.CharField(max_length=40)
    date_time = models.DateTimeField()
    objects = MongoDBManager()

    activity = EmbeddedModelField('ActivityEntry')
    wifi = ListField(EmbeddedModelField('WifiEntry'))
    location = ListField(EmbeddedModelField('LocationEntry'))


def reduce_activity_vector(vector):
    activities = {"sitting": 0.0, "walking": 0.0, "standing": 0.0, "upstairs": 0.0, "downstairs": 0.0}

    for i in xrange(len(vector)):
        activities[activity_table_json[i + 1]] += vector[i]
    return activities

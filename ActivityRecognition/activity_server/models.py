from django.db import models

activity_table = {1: 'walking',
                  2: 'sitting',
                  3: 'standing',
                  4: 'jogging',
                  5: 'biking',
                  6: 'upstairs',
                  7: 'downstairs'}


class DataRecord(models.Model):
    user_id = models.CharField(max_length=40)
    record_date = models.DateTimeField()
    activity_calculated = models.BooleanField()

    walking = models.FloatField()
    sitting = models.FloatField()
    standing = models.FloatField()
    jogging = models.FloatField()
    biking = models.FloatField()
    upstairs = models.FloatField()
    downstairs = models.FloatField()

    def get_activity_name(self):
        return activity_table.get(self.activity.real)


class WifiRecord(models.Model):
    time_stamp = models.BigIntegerField()
    data_record = models.ForeignKey(DataRecord)
    wifi_name = models.CharField(max_length=32)


class LocationRecord(models.Model):
    data_record = models.ForeignKey(DataRecord)
    time_stamp = models.BigIntegerField()
    lat = models.FloatField()
    lon = models.FloatField()


class AcceleratorRecord(models.Model):
    data_record = models.ForeignKey(DataRecord)
    time_stamp = models.BigIntegerField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()


class GyroscopeRecord(models.Model):
    data_record = models.ForeignKey(DataRecord)
    time_stamp = models.BigIntegerField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
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
    activity = models.PositiveSmallIntegerField()

    def get_activity_name(self):
        return activity_table.get(self.activity.real)


class WifiRecord(models.Model):
    time_stamp = models.BigIntegerField()
    data_record = models.ForeignKey(DataRecord)
    wifi_name = models.CharField(max_length=32)


class LocationRecord(models.Model):
    data_record = models.ForeignKey(DataRecord)
    time_stamp = models.BigIntegerField()
    lat = models.DecimalField(max_digits=20, decimal_places=17)
    lon = models.DecimalField(max_digits=20, decimal_places=17)


class AcceleratorRecord(models.Model):
    data_record = models.ForeignKey(DataRecord)
    time_stamp = models.BigIntegerField()
    x = models.DecimalField(max_digits=20, decimal_places=17)
    y = models.DecimalField(max_digits=20, decimal_places=17)
    z = models.DecimalField(max_digits=20, decimal_places=17)


class GyroscopeRecord(models.Model):
    data_record = models.ForeignKey(DataRecord)
    time_stamp = models.BigIntegerField()
    x = models.DecimalField(max_digits=20, decimal_places=17)
    y = models.DecimalField(max_digits=20, decimal_places=17)
    z = models.DecimalField(max_digits=20, decimal_places=17)
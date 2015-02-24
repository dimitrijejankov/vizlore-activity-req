from django.db import models

activity_table = {1: "Sitting Hand",
                  2: "Sitting Pocket",
                  3: "Walking Hand",
                  4: "Walking Pocket",
                  5: "Standing Hand",
                  6: "Standing Pocket",
                  7: "Upstairs",
                  8: "Downstairs"}


class DataRecord(models.Model):
    user_id = models.CharField(max_length=40)
    record_date = models.DateTimeField()

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
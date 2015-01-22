from django.db import models


class DataRecord(models.Model):
    user_id = models.CharField(max_length=40)
    record_date = models.DateTimeField()


class WifiRecord(models.Model):
    data_record = models.ForeignKey(DataRecord)
    wifi_name = models.CharField(max_length=32)


class LocationRecord(models.Model):
    data_record = models.ForeignKey(DataRecord)
    time_stamp = models.BigIntegerField()
    lat = models.DecimalField(max_digits=20, decimal_places=17)
    lon = models.DecimalField(max_digits=20, decimal_places=17)
    #accuracy = models.DecimalField(max_digits=20, decimal_places=15)


class AcceleratorRecord(models.Model):
    data_record = models.ForeignKey(DataRecord)
    time_stamp = models.BigIntegerField()
    x = models.DecimalField(max_digits=20, decimal_places=17)
    y = models.DecimalField(max_digits=20, decimal_places=17)
    z = models.DecimalField(max_digits=20, decimal_places=17)
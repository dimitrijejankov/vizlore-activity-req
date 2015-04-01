from django.db import models
from djangotoolbox.fields import ListField

activity_table = {1: "Sitting Hand",
                  2: "Sitting Pocket",
                  3: "Walking Hand",
                  4: "Walking Pocket",
                  5: "Standing Hand",
                  6: "Standing Pocket",
                  7: "Upstairs",
                  8: "Downstairs"}

reduced_activity_table = {
    0: 0,
    1: 0,
    2: 1,
    3: 1,
    4: 2,
    5: 2,
    6: 3,
    7: 4
}

reduced_activity_table_json = {
    1: "sitting",
    2: "walking",
    3: "standing",
    4: "upstairs",
    5: "downstairs",
}


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


class DataRecord(models.Model):
    user_id = models.CharField(max_length=40)
    time_stamp = models.BigIntegerField()

    acceleration_t = ListField()
    acceleration_x = ListField()
    acceleration_y = ListField()
    acceleration_z = ListField()

    gyroscope_t = ListField()
    gyroscope_x = ListField()
    gyroscope_y = ListField()
    gyroscope_z = ListField()

    wifi_t = ListField()
    wifi_ssid = ListField()

    location_t = ListField()
    location_lan = ListField()
    location_lon = ListField()


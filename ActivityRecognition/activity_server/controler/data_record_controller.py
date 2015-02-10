from activity_server.models import DataRecord, LocationRecord, AcceleratorRecord, WifiRecord, GyroscopeRecord
from datetime import datetime
from decimal import Decimal


def store_data_record(json_object):

    if 'uuid' in json_object.keys() and \
       'acceleration' in json_object.keys() and \
       'gyroscope' in json_object.keys() and \
       'location' in json_object.keys() and \
       'wifi' in json_object.keys():

        record = DataRecord(user_id=json_object.get('uuid'), record_date=datetime.now())
        record.save()

        store_location_record(json_object.get('location'), record)
        store_acceleration_record(json_object.get('acceleration'), record)
        store_gyroscope_record(json_object.get('gyroscope'), record)
        store_wifi_record(json_object.get('wifi'), record)

    else:
        raise Exception("Invalid json format")


def store_location_record(locations_object, data_object):

    for location_record_json in locations_object:
        if 'timestamp' in location_record_json.keys() and 'coords' in location_record_json.keys():
            coords_json = location_record_json.get('coords')
            if "longitude" in coords_json.keys() and "latitude" in coords_json.keys():
                location_record = LocationRecord(data_record=data_object,
                                                 time_stamp=location_record_json.get('timestamp'),
                                                 lat=Decimal.from_float(coords_json.get('latitude')),
                                                 lon=Decimal.from_float(coords_json.get('longitude')))
                location_record.save()
            else:
                raise Exception("Invalid json format")
        else:
            raise Exception("Invalid json format")


def store_acceleration_record(acceleration_object, data_object):
    for i in range(len(acceleration_object)):
        if 'x' in acceleration_object[i].keys() and \
           'y' in acceleration_object[i].keys() and \
           'z' in acceleration_object[i].keys() and \
           'timestamp' in acceleration_object[i].keys():

            acceleration_record = AcceleratorRecord(data_record=data_object,
                                                    time_stamp=acceleration_object[i].get('timestamp'),
                                                    x=Decimal.from_float(acceleration_object[i].get('x')),
                                                    y=Decimal.from_float(acceleration_object[i].get('y')),
                                                    z=Decimal.from_float(acceleration_object[i].get('z')))
            acceleration_record.save()
        else:
            raise Exception("Invalid json format")


def store_gyroscope_record(gyroscope_object, data_object):
    for i in range(len(gyroscope_object)):
        if 'x' in gyroscope_object[i].keys() and \
           'y' in gyroscope_object[i].keys() and \
           'z' in gyroscope_object[i].keys() and \
           'timestamp' in gyroscope_object[i].keys():

            acceleration_record = GyroscopeRecord(data_record=data_object,
                                                  time_stamp=gyroscope_object[i].get('timestamp'),
                                                  x=Decimal.from_float(gyroscope_object[i].get('x')),
                                                  y=Decimal.from_float(gyroscope_object[i].get('y')),
                                                  z=Decimal.from_float(gyroscope_object[i].get('z')))
            acceleration_record.save()
        else:
            raise Exception("Invalid json format")


def store_wifi_record(wifi_objects, data_object):
    for wifi_object in wifi_objects:
        if 'ssids' in wifi_object.keys() and 'timestamp' in wifi_object.keys():
            timestamp = wifi_object.get('timestamp')
            for ssid in wifi_object.get('ssids'):
                wifi_record = WifiRecord(data_record=data_object, time_stamp=timestamp, wifi_name=ssid)
                wifi_record.save()
        else:
            raise Exception("Invalid json format")
import numpy as np

from scipy.signal import butter, lfilter, medfilt
from methods.utilities import get_mean, get_correlation, get_energy, get_standard_deviation


def butter_bandpass(low_cut, high_cut, fs, order=5):
    nyq = 0.5 * fs
    low = low_cut / nyq
    high = high_cut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(x, low_cut, high_cut, fs, order=5):
    b, a = butter_bandpass(low_cut, high_cut, fs, order=order)
    y = lfilter(b, a, x)
    return y


def read_my_data():

    x = []
    y = []
    z = []

    f = open('my_data/standing.csv', 'r')

    i = 0

    for line in f:
        sp = line.split(',')

        x.append(float(sp[1]))
        y.append(float(sp[2]))
        z.append(float(sp[3]))

        if i == 127:
            break

        i += 1

    x = medfilt(np.array(x))
    x = butter_bandpass_filter(x, 0, 20, 50, order=3)
    y = medfilt(np.array(y))
    y = butter_bandpass_filter(y, 0, 20, 50, order=3)
    z = medfilt(np.array(z))
    z = butter_bandpass_filter(z, 0, 20, 50, order=3)

    x_mean = get_mean(x)
    x_energy = get_energy(x)
    x_st_deviation = get_standard_deviation(x, x_mean)
    
    y_mean = get_mean(y)
    y_energy = get_energy(y)
    y_st_deviation = get_standard_deviation(y, y_mean)
    
    z_mean = get_mean(z)
    z_energy = get_energy(z)
    z_st_deviation = get_standard_deviation(z, z_mean)

    xy_cor = get_correlation(x, y, x_mean, y_mean, x_st_deviation, y_st_deviation)
    xz_cor = get_correlation(x, z, x_mean, z_mean, x_st_deviation, z_st_deviation)
    zy_cor = get_correlation(z, y, z_mean, y_mean, z_st_deviation, y_st_deviation)

    return [x_mean, x_energy, x_st_deviation,
            y_mean, y_energy, y_st_deviation,
            z_mean, z_energy, z_st_deviation,
            xy_cor, xz_cor, zy_cor]
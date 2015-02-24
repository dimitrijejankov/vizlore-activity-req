from math import sqrt
from numpy import ndarray, array


def get_mean(x_array):
    return sum(x_array) / len(x_array)


def get_standard_deviation(x_array, mean):
    s = 0
    for i in xrange(len(x_array)):
        s += (x_array[i] - mean)**2
    return sqrt(s / len(x_array))


def get_energy(x_array):
    s = 0
    for i in xrange(len(x_array)):
        s += x_array[i]**2
    return s / len(x_array)


def get_correlation(x_array, y_array, x_mean, y_mean, x_sd, y_sd):
    s = 0
    for i in range(len(x_array)):
        s += (x_array[i] - x_mean)*(y_array[i] - y_mean)
    return s / (len(x_array)*x_sd*y_sd)


def get_features(x_acc, y_acc, z_acc, x_gyo, y_gyo, z_gyo):
    
    x_acc_mean = get_mean(x_acc)
    y_acc_mean = get_mean(y_acc)
    z_acc_mean = get_mean(z_acc)
    
    x_gyo_mean = get_mean(x_gyo)
    y_gyo_mean = get_mean(y_gyo)
    z_gyo_mean = get_mean(z_gyo)
    
    x_acc_energy = get_energy(x_acc)
    y_acc_energy = get_energy(y_acc)
    z_acc_energy = get_energy(z_acc)
    
    x_acc_std_dev = get_standard_deviation(x_acc, x_acc_mean)
    y_acc_std_dev = get_standard_deviation(y_acc, y_acc_mean)
    z_acc_std_dev = get_standard_deviation(z_acc, z_acc_mean)
    
    x_gyo_std_dev = get_standard_deviation(x_gyo, x_gyo_mean)
    y_gyo_std_dev = get_standard_deviation(y_gyo, y_gyo_mean)
    z_gyo_std_dev = get_standard_deviation(z_gyo, z_gyo_mean)
    
    xy_acc_cor = get_correlation(x_acc, y_acc, x_acc_mean, y_acc_mean, x_acc_std_dev, y_acc_std_dev)
    xz_acc_cor = get_correlation(x_acc, z_acc, x_acc_mean, z_acc_mean, x_acc_std_dev, z_acc_std_dev)
    zy_acc_cor = get_correlation(z_acc, y_acc, z_acc_mean, y_acc_mean, z_acc_std_dev, y_acc_std_dev)    
    
    xy_gyo_cor = get_correlation(x_gyo, y_gyo, x_gyo_mean, y_gyo_mean, x_gyo_std_dev, y_gyo_std_dev)
    xz_gyo_cor = get_correlation(x_gyo, z_gyo, x_gyo_mean, z_gyo_mean, x_gyo_std_dev, z_gyo_std_dev)
    zy_gyo_cor = get_correlation(z_gyo, y_gyo, z_gyo_mean, y_gyo_mean, z_gyo_std_dev, y_gyo_std_dev)

    data = ndarray(shape=(1, 21), dtype=float)
    data[0] = array([x_acc_mean, x_acc_energy, x_acc_std_dev,
                     y_acc_mean, y_acc_energy, y_acc_std_dev,
                     z_acc_mean, z_acc_energy, z_acc_std_dev,
                     xy_acc_cor, xz_acc_cor, zy_acc_cor,
                     x_gyo_mean, x_gyo_std_dev,
                     y_gyo_mean, y_gyo_std_dev,
                     z_gyo_mean, z_gyo_std_dev,
                     xy_gyo_cor, xz_gyo_cor, zy_gyo_cor])
    return data
from math import sqrt


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
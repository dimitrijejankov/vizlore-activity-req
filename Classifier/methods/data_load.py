from numpy import ndarray, array
from methods.utilities import get_mean, get_correlation, get_energy, get_standard_deviation


def load_data_acceleration(results_filename, acc_x_filename, acc_y_filename, acc_z_filename):

    subject = open(results_filename, 'r')
    subject_data = []

    for line in subject:
        subject_data.append(int(line))

    target = ndarray(shape=(len(subject_data),), dtype=int, buffer=array(subject_data))

    x_data = []
    x_mean = []
    x_energy = []
    x_st_deviation = []

    x_file = open(acc_x_filename, 'r')

    for line in x_file:
        x_values = line.split()
        temp = []
        for value in x_values:
            temp.append(float(value))
        mean = get_mean(temp)

        x_data.append(temp)
        x_mean.append(mean)
        x_energy.append(get_energy(temp))
        x_st_deviation.append(get_standard_deviation(temp, mean))

    y_data = []
    y_mean = []
    y_energy = []
    y_st_deviation = []

    y_file = open(acc_y_filename, 'r')

    for line in y_file:
        y_values = line.split()
        temp = []
        for value in y_values:
            temp.append(float(value))
        mean = get_mean(temp)

        y_data.append(temp)
        y_mean.append(mean)
        y_energy.append(get_energy(temp))
        y_st_deviation.append(get_standard_deviation(temp, mean))

    z_data = []
    z_mean = []
    z_energy = []
    z_st_deviation = []

    z_file = open(acc_z_filename, 'r')

    for line in z_file:
        z_values = line.split()
        temp = []
        for value in z_values:
            temp.append(float(value))
        mean = get_mean(temp)

        z_data.append(temp)
        z_mean.append(mean)
        z_energy.append(get_energy(temp))
        z_st_deviation.append(get_standard_deviation(temp, mean))

    xy_cor = []
    xz_cor = []
    zy_cor = []

    for i in xrange(len(x_data)):

        cor_xy = get_correlation(x_data[i], y_data[i], x_mean[i], y_mean[i], x_st_deviation[i], y_st_deviation[i])
        cor_xz = get_correlation(x_data[i], z_data[i], x_mean[i], z_mean[i], x_st_deviation[i], z_st_deviation[i])
        cor_zy = get_correlation(z_data[i], y_data[i], z_mean[i], y_mean[i], z_st_deviation[i], y_st_deviation[i])

        xy_cor.append(cor_xy)
        xz_cor.append(cor_xz)
        zy_cor.append(cor_zy)

    data = ndarray(shape=(len(subject_data), 12), dtype=float)

    for i in xrange(len(x_data)):

        data[i] = array([x_mean[i], x_energy[i], x_st_deviation[i],
                         y_mean[i], y_energy[i], y_st_deviation[i],
                         z_mean[i], z_energy[i], z_st_deviation[i],
                         xy_cor[i], xz_cor[i], zy_cor[i]])

    return target, data


def load_data(results_filename,
              acc_x_filename, acc_y_filename, acc_z_filename,
              gyo_x_filename, gyo_y_filename, gyo_z_filename):

    subject = open(results_filename, 'r')
    subject_data = []

    for line in subject:
        subject_data.append(int(line))

    target = ndarray(shape=(len(subject_data),), dtype=int, buffer=array(subject_data))

    x_data = []
    x_mean = []
    x_energy = []
    x_st_deviation = []

    x_file = open(acc_x_filename, 'r')

    for line in x_file:
        x_values = line.split()
        temp = []
        for value in x_values:
            temp.append(float(value))
        mean = get_mean(temp)

        x_data.append(temp)
        x_mean.append(mean)
        x_energy.append(get_energy(temp))
        x_st_deviation.append(get_standard_deviation(temp, mean))

    y_data = []
    y_mean = []
    y_energy = []
    y_st_deviation = []

    y_file = open(acc_y_filename, 'r')

    for line in y_file:
        y_values = line.split()
        temp = []
        for value in y_values:
            temp.append(float(value))
        mean = get_mean(temp)

        y_data.append(temp)
        y_mean.append(mean)
        y_energy.append(get_energy(temp))
        y_st_deviation.append(get_standard_deviation(temp, mean))

    z_data = []
    z_mean = []
    z_energy = []
    z_st_deviation = []

    z_file = open(acc_z_filename, 'r')

    for line in z_file:
        z_values = line.split()
        temp = []
        for value in z_values:
            temp.append(float(value))
        mean = get_mean(temp)

        z_data.append(temp)
        z_mean.append(mean)
        z_energy.append(get_energy(temp))
        z_st_deviation.append(get_standard_deviation(temp, mean))

    xy_cor = []
    xz_cor = []
    zy_cor = []

    for i in xrange(len(x_data)):

        cor_xy = get_correlation(x_data[i], y_data[i], x_mean[i], y_mean[i], x_st_deviation[i], y_st_deviation[i])
        cor_xz = get_correlation(x_data[i], z_data[i], x_mean[i], z_mean[i], x_st_deviation[i], z_st_deviation[i])
        cor_zy = get_correlation(z_data[i], y_data[i], z_mean[i], y_mean[i], z_st_deviation[i], y_st_deviation[i])

        xy_cor.append(cor_xy)
        xz_cor.append(cor_xz)
        zy_cor.append(cor_zy)

    x_data_gyo = []
    x_mean_gyo = []
    x_st_deviation_gyo = []

    x_file = open(gyo_x_filename, 'r')

    for line in x_file:
        x_values = line.split()
        temp = []
        for value in x_values:
            temp.append(float(value))
        mean = get_mean(temp)

        x_data_gyo.append(temp)
        x_mean_gyo.append(mean)
        x_st_deviation_gyo.append(get_standard_deviation(temp, mean))

    y_data_gyo = []
    y_mean_gyo = []
    y_st_deviation_gyo = []

    y_file = open(gyo_y_filename, 'r')

    for line in y_file:
        y_values = line.split()
        temp = []
        for value in y_values:
            temp.append(float(value))
        mean = get_mean(temp)

        y_data_gyo.append(temp)
        y_mean_gyo.append(mean)
        y_st_deviation_gyo.append(get_standard_deviation(temp, mean))

    z_data_gyo = []
    z_mean_gyo = []
    z_st_deviation_gyo = []

    z_file = open(gyo_z_filename, 'r')

    for line in z_file:
        z_values = line.split()
        temp = []
        for value in z_values:
            temp.append(float(value))
        mean = get_mean(temp)

        z_data_gyo.append(temp)
        z_mean_gyo.append(mean)
        z_st_deviation_gyo.append(get_standard_deviation(temp, mean))

    xy_cor_gyo = []
    xz_cor_gyo = []
    zy_cor_gyo = []

    for i in xrange(len(x_data_gyo)):

        cor_xy_gyo = get_correlation(x_data_gyo[i], y_data_gyo[i],
                                     x_mean_gyo[i], y_mean_gyo[i],
                                     x_st_deviation_gyo[i], y_st_deviation_gyo[i])

        cor_xz_gyo = get_correlation(x_data_gyo[i], z_data_gyo[i],
                                     x_mean_gyo[i], z_mean_gyo[i],
                                     x_st_deviation_gyo[i], z_st_deviation_gyo[i])

        cor_zy_gyo = get_correlation(z_data_gyo[i], y_data_gyo[i],
                                     z_mean_gyo[i], y_mean_gyo[i],
                                     z_st_deviation_gyo[i], y_st_deviation_gyo[i])

        xy_cor_gyo.append(cor_xy_gyo)
        xz_cor_gyo.append(cor_xz_gyo)
        zy_cor_gyo.append(cor_zy_gyo)

    data = ndarray(shape=(len(subject_data), 21), dtype=float)

    for i in xrange(len(x_data)):

        data[i] = array([x_mean[i], x_energy[i], x_st_deviation[i],
                         y_mean[i], y_energy[i], y_st_deviation[i],
                         z_mean[i], z_energy[i], z_st_deviation[i],
                         xy_cor[i], xz_cor[i], zy_cor[i],
                         x_mean_gyo[i], x_st_deviation_gyo[i],
                         y_mean_gyo[i], y_st_deviation_gyo[i],
                         z_mean_gyo[i], z_st_deviation_gyo[i],
                         xy_cor_gyo[i], xz_cor_gyo[i], zy_cor_gyo[i]])

    return target, data
from methods.utilities import get_mean, get_correlation, get_energy, get_standard_deviation
import matplotlib.pyplot as plt

activity_table = {'walking\r\n': 1,
                  'sitting\r\n': 2,
                  'standing\r\n': 3,
                  'jogging\r\n': 4,
                  'biking\r\n': 5,
                  'upstairs\r\n': 6,
                  'downstairs\r\n': 7}

activity_map = {1: 1, 6: 2, 7: 3, 2: 4, 5: 3}


def load_data_set(filename):
    data_file = open(filename, 'r')

    data_list = []
    target_list = []

    skip = 2

    wr_buffer_acc_x = []
    wr_buffer_acc_y = []
    wr_buffer_acc_z = []

    i = 0

    current_activity = -1

    for line in data_file:
        if skip <= 0:
            sp_line = line.split(',')

            wr_buffer_acc_x.append(float(sp_line[1]))
            wr_buffer_acc_y.append(float(sp_line[2]))
            wr_buffer_acc_z.append(float(sp_line[3]))

            i += 1

            if current_activity == -1:
                current_activity = activity_table.get(sp_line[69])

            if current_activity != activity_table.get(sp_line[69]):
                current_activity = -1
                i = 0

                wr_buffer_acc_x = []
                wr_buffer_acc_y = []
                wr_buffer_acc_z = []

            if i == 128:

                # acceleration means

                #plt.plot(wr_buffer_acc_x)
                #plt.show()

                wr_mean_acc_x = get_mean(wr_buffer_acc_x)
                wr_mean_acc_y = get_mean(wr_buffer_acc_y)
                wr_mean_acc_z = get_mean(wr_buffer_acc_z)

                # acceleration standard deviations

                wr_standard_deviation_acc_x = get_standard_deviation(wr_buffer_acc_x, wr_mean_acc_x)
                wr_standard_deviation_acc_y = get_standard_deviation(wr_buffer_acc_y, wr_mean_acc_y)
                wr_standard_deviation_acc_z = get_standard_deviation(wr_buffer_acc_z, wr_mean_acc_z)

                # acceleration energies

                wr_energy_acc_x = get_energy(wr_buffer_acc_x)
                wr_energy_acc_y = get_energy(wr_buffer_acc_y)
                wr_energy_acc_z = get_energy(wr_buffer_acc_z)

                # correlations

                wr_correlation_acc_xy = get_correlation(wr_buffer_acc_x, wr_buffer_acc_y,
                                                        wr_mean_acc_x, wr_mean_acc_y,
                                                        wr_standard_deviation_acc_x, wr_standard_deviation_acc_y)

                wr_correlation_acc_xz = get_correlation(wr_buffer_acc_x, wr_buffer_acc_z,
                                                        wr_mean_acc_x, wr_mean_acc_z,
                                                        wr_standard_deviation_acc_x, wr_standard_deviation_acc_z)

                wr_correlation_acc_yz = get_correlation(wr_buffer_acc_z, wr_buffer_acc_y,
                                                        wr_mean_acc_z, wr_mean_acc_y,
                                                        wr_standard_deviation_acc_z, wr_standard_deviation_acc_y)

                # storing the fucking data

                if current_activity != 4 and current_activity != 5:
                    data_list.append([wr_mean_acc_x, wr_energy_acc_x, wr_standard_deviation_acc_x,
                                     wr_mean_acc_y, wr_energy_acc_y, wr_standard_deviation_acc_y,
                                     wr_mean_acc_z, wr_energy_acc_z, wr_standard_deviation_acc_z,
                                     wr_correlation_acc_xy, wr_correlation_acc_xz, wr_correlation_acc_yz])

                    target_list.append(activity_map.get(current_activity))

                wr_buffer_acc_x = []
                wr_buffer_acc_y = []
                wr_buffer_acc_z = []

                i = 0

        else:
            skip -= 1

    return target_list, data_list
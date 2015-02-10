from methods.utilities import get_mean, get_correlation, get_energy, get_standard_deviation

activity_table = {'walking\r\n': 1,
                  'sitting\r\n': 2,
                  'standing\r\n': 3,
                  'jogging\r\n': 4,
                  'biking\r\n': 5,
                  'upstairs\r\n': 6,
                  'downstairs\r\n': 7}


def load_data_set(filename):
    data_file = open(filename, 'r')

    data_list = []
    target_list = []

    skip = 2

    lp_buffer_acc_x = []
    lp_buffer_acc_y = []
    lp_buffer_acc_z = []

    lp_buffer_gyo_x = []
    lp_buffer_gyo_y = []
    lp_buffer_gyo_z = []

    rp_buffer_acc_x = []
    rp_buffer_acc_y = []
    rp_buffer_acc_z = []

    rp_buffer_gyo_x = []
    rp_buffer_gyo_y = []
    rp_buffer_gyo_z = []

    wr_buffer_acc_x = []
    wr_buffer_acc_y = []
    wr_buffer_acc_z = []

    wr_buffer_gyo_x = []
    wr_buffer_gyo_y = []
    wr_buffer_gyo_z = []

    ua_buffer_acc_x = []
    ua_buffer_acc_y = []
    ua_buffer_acc_z = []

    ua_buffer_gyo_x = []
    ua_buffer_gyo_y = []
    ua_buffer_gyo_z = []

    be_buffer_acc_x = []
    be_buffer_acc_y = []
    be_buffer_acc_z = []

    be_buffer_gyo_x = []
    be_buffer_gyo_y = []
    be_buffer_gyo_z = []

    i = 0

    current_activity = -1

    for line in data_file:
        if skip <= 0:
            sp_line = line.split(',')

            lp_buffer_acc_x.append(float(sp_line[1]))
            lp_buffer_acc_y.append(float(sp_line[2]))
            lp_buffer_acc_z.append(float(sp_line[3]))

            lp_buffer_gyo_x.append(float(sp_line[7]))
            lp_buffer_gyo_y.append(float(sp_line[8]))
            lp_buffer_gyo_z.append(float(sp_line[9]))

            rp_buffer_acc_x.append(float(sp_line[15]))
            rp_buffer_acc_y.append(float(sp_line[16]))
            rp_buffer_acc_z.append(float(sp_line[17]))

            rp_buffer_gyo_x.append(float(sp_line[21]))
            rp_buffer_gyo_y.append(float(sp_line[22]))
            rp_buffer_gyo_z.append(float(sp_line[23]))

            wr_buffer_acc_x.append(float(sp_line[29]))
            wr_buffer_acc_y.append(float(sp_line[30]))
            wr_buffer_acc_z.append(float(sp_line[31]))

            wr_buffer_gyo_x.append(float(sp_line[35]))
            wr_buffer_gyo_y.append(float(sp_line[36]))
            wr_buffer_gyo_z.append(float(sp_line[37]))

            ua_buffer_acc_x.append(float(sp_line[43]))
            ua_buffer_acc_y.append(float(sp_line[44]))
            ua_buffer_acc_z.append(float(sp_line[45]))

            ua_buffer_gyo_x.append(float(sp_line[49]))
            ua_buffer_gyo_y.append(float(sp_line[50]))
            ua_buffer_gyo_z.append(float(sp_line[51]))

            be_buffer_acc_x.append(float(sp_line[57]))
            be_buffer_acc_y.append(float(sp_line[58]))
            be_buffer_acc_z.append(float(sp_line[59]))

            be_buffer_gyo_x.append(float(sp_line[63]))
            be_buffer_gyo_y.append(float(sp_line[64]))
            be_buffer_gyo_z.append(float(sp_line[65]))

            i += 1

            if current_activity == -1:
                current_activity = activity_table.get(sp_line[69])

            if current_activity != activity_table.get(sp_line[69]):

                current_activity = -1
                i = 0

                lp_buffer_acc_x = []
                lp_buffer_acc_y = []
                lp_buffer_acc_z = []

                lp_buffer_gyo_x = []
                lp_buffer_gyo_y = []
                lp_buffer_gyo_z = []

                rp_buffer_acc_x = []
                rp_buffer_acc_y = []
                rp_buffer_acc_z = []

                rp_buffer_gyo_x = []
                rp_buffer_gyo_y = []
                rp_buffer_gyo_z = []

                wr_buffer_acc_x = []
                wr_buffer_acc_y = []
                wr_buffer_acc_z = []

                wr_buffer_gyo_x = []
                wr_buffer_gyo_y = []
                wr_buffer_gyo_z = []

                ua_buffer_acc_x = []
                ua_buffer_acc_y = []
                ua_buffer_acc_z = []

                ua_buffer_gyo_x = []
                ua_buffer_gyo_y = []
                ua_buffer_gyo_z = []

                be_buffer_acc_x = []
                be_buffer_acc_y = []
                be_buffer_acc_z = []

                be_buffer_gyo_x = []
                be_buffer_gyo_y = []
                be_buffer_gyo_z = []

            if i == 128:

                # acceleration means

                lp_mean_acc_x = get_mean(lp_buffer_acc_x)
                lp_mean_acc_y = get_mean(lp_buffer_acc_y)
                lp_mean_acc_z = get_mean(lp_buffer_acc_z)

                rp_mean_acc_x = get_mean(rp_buffer_acc_x)
                rp_mean_acc_y = get_mean(rp_buffer_acc_y)
                rp_mean_acc_z = get_mean(rp_buffer_acc_z)

                wr_mean_acc_x = get_mean(wr_buffer_acc_x)
                wr_mean_acc_y = get_mean(wr_buffer_acc_y)
                wr_mean_acc_z = get_mean(wr_buffer_acc_z)

                ua_mean_acc_x = get_mean(ua_buffer_acc_x)
                ua_mean_acc_y = get_mean(ua_buffer_acc_y)
                ua_mean_acc_z = get_mean(ua_buffer_acc_z)

                be_mean_acc_x = get_mean(be_buffer_acc_x)
                be_mean_acc_y = get_mean(be_buffer_acc_y)
                be_mean_acc_z = get_mean(be_buffer_acc_z)

                # acceleration standard deviations

                lp_standard_deviation_acc_x = get_standard_deviation(lp_buffer_acc_x, lp_mean_acc_x)
                lp_standard_deviation_acc_y = get_standard_deviation(lp_buffer_acc_y, lp_mean_acc_y)
                lp_standard_deviation_acc_z = get_standard_deviation(lp_buffer_acc_z, lp_mean_acc_z)

                rp_standard_deviation_acc_x = get_standard_deviation(rp_buffer_acc_x, rp_mean_acc_x)
                rp_standard_deviation_acc_y = get_standard_deviation(rp_buffer_acc_y, rp_mean_acc_y)
                rp_standard_deviation_acc_z = get_standard_deviation(rp_buffer_acc_z, rp_mean_acc_z)

                wr_standard_deviation_acc_x = get_standard_deviation(wr_buffer_acc_x, wr_mean_acc_x)
                wr_standard_deviation_acc_y = get_standard_deviation(wr_buffer_acc_y, wr_mean_acc_y)
                wr_standard_deviation_acc_z = get_standard_deviation(wr_buffer_acc_z, wr_mean_acc_z)

                ua_standard_deviation_acc_x = get_standard_deviation(ua_buffer_acc_x, ua_mean_acc_x)
                ua_standard_deviation_acc_y = get_standard_deviation(ua_buffer_acc_y, ua_mean_acc_y)
                ua_standard_deviation_acc_z = get_standard_deviation(ua_buffer_acc_z, ua_mean_acc_z)

                be_standard_deviation_acc_x = get_standard_deviation(be_buffer_acc_x, be_mean_acc_x)
                be_standard_deviation_acc_y = get_standard_deviation(be_buffer_acc_y, be_mean_acc_y)
                be_standard_deviation_acc_z = get_standard_deviation(be_buffer_acc_z, be_mean_acc_z)

                # acceleration energies

                lp_energy_acc_x = get_energy(lp_buffer_acc_x)
                lp_energy_acc_y = get_energy(lp_buffer_acc_y)
                lp_energy_acc_z = get_energy(lp_buffer_acc_z)

                rp_energy_acc_x = get_energy(rp_buffer_acc_x)
                rp_energy_acc_y = get_energy(rp_buffer_acc_y)
                rp_energy_acc_z = get_energy(rp_buffer_acc_z)

                wr_energy_acc_x = get_energy(wr_buffer_acc_x)
                wr_energy_acc_y = get_energy(wr_buffer_acc_y)
                wr_energy_acc_z = get_energy(wr_buffer_acc_z)

                ua_energy_acc_x = get_energy(ua_buffer_acc_x)
                ua_energy_acc_y = get_energy(ua_buffer_acc_y)
                ua_energy_acc_z = get_energy(ua_buffer_acc_z)

                be_energy_acc_x = get_energy(be_buffer_acc_x)
                be_energy_acc_y = get_energy(be_buffer_acc_y)
                be_energy_acc_z = get_energy(be_buffer_acc_z)

                # correlations

                lp_correlation_acc_xy = get_correlation(lp_buffer_acc_x, lp_buffer_acc_y,
                                                        lp_mean_acc_x, lp_mean_acc_y,
                                                        lp_standard_deviation_acc_x, lp_standard_deviation_acc_y)

                lp_correlation_acc_xz = get_correlation(lp_buffer_acc_x, lp_buffer_acc_z,
                                                        lp_mean_acc_x, lp_mean_acc_z,
                                                        lp_standard_deviation_acc_x, lp_standard_deviation_acc_z)

                lp_correlation_acc_yz = get_correlation(lp_buffer_acc_z, lp_buffer_acc_y,
                                                        lp_mean_acc_z, lp_mean_acc_y,
                                                        lp_standard_deviation_acc_z, lp_standard_deviation_acc_y)

                rp_correlation_acc_xy = get_correlation(rp_buffer_acc_x, rp_buffer_acc_y,
                                                        rp_mean_acc_x, rp_mean_acc_y,
                                                        rp_standard_deviation_acc_x, rp_standard_deviation_acc_y)

                rp_correlation_acc_xz = get_correlation(rp_buffer_acc_x, rp_buffer_acc_z,
                                                        rp_mean_acc_x, rp_mean_acc_z,
                                                        rp_standard_deviation_acc_x, rp_standard_deviation_acc_z)

                rp_correlation_acc_yz = get_correlation(rp_buffer_acc_z, rp_buffer_acc_y,
                                                        rp_mean_acc_z, rp_mean_acc_y,
                                                        rp_standard_deviation_acc_z, rp_standard_deviation_acc_y)

                wr_correlation_acc_xy = get_correlation(wr_buffer_acc_x, wr_buffer_acc_y,
                                                        wr_mean_acc_x, wr_mean_acc_y,
                                                        wr_standard_deviation_acc_x, wr_standard_deviation_acc_y)

                wr_correlation_acc_xz = get_correlation(wr_buffer_acc_x, wr_buffer_acc_z,
                                                        wr_mean_acc_x, wr_mean_acc_z,
                                                        wr_standard_deviation_acc_x, wr_standard_deviation_acc_z)

                wr_correlation_acc_yz = get_correlation(wr_buffer_acc_z, wr_buffer_acc_y,
                                                        wr_mean_acc_z, wr_mean_acc_y,
                                                        wr_standard_deviation_acc_z, wr_standard_deviation_acc_y)

                ua_correlation_acc_xy = get_correlation(ua_buffer_acc_x, ua_buffer_acc_y,
                                                        ua_mean_acc_x, ua_mean_acc_y,
                                                        ua_standard_deviation_acc_x, ua_standard_deviation_acc_y)

                ua_correlation_acc_xz = get_correlation(ua_buffer_acc_x, ua_buffer_acc_z,
                                                        ua_mean_acc_x, ua_mean_acc_z,
                                                        ua_standard_deviation_acc_x, ua_standard_deviation_acc_z)

                ua_correlation_acc_yz = get_correlation(ua_buffer_acc_z, ua_buffer_acc_y,
                                                        ua_mean_acc_z, ua_mean_acc_y,
                                                        ua_standard_deviation_acc_z, ua_standard_deviation_acc_y)

                be_correlation_acc_xy = get_correlation(be_buffer_acc_x, be_buffer_acc_y,
                                                        be_mean_acc_x, be_mean_acc_y,
                                                        be_standard_deviation_acc_x, be_standard_deviation_acc_y)

                be_correlation_acc_xz = get_correlation(be_buffer_acc_x, be_buffer_acc_z,
                                                        be_mean_acc_x, be_mean_acc_z,
                                                        be_standard_deviation_acc_x, be_standard_deviation_acc_z)

                be_correlation_acc_yz = get_correlation(be_buffer_acc_z, be_buffer_acc_y,
                                                        be_mean_acc_z, be_mean_acc_y,
                                                        be_standard_deviation_acc_z, be_standard_deviation_acc_y)

                # gyroscope means

                lp_mean_gyo_x = get_mean(lp_buffer_gyo_x)
                lp_mean_gyo_y = get_mean(lp_buffer_gyo_y)
                lp_mean_gyo_z = get_mean(lp_buffer_gyo_z)

                rp_mean_gyo_x = get_mean(rp_buffer_gyo_x)
                rp_mean_gyo_y = get_mean(rp_buffer_gyo_y)
                rp_mean_gyo_z = get_mean(rp_buffer_gyo_z)

                wr_mean_gyo_x = get_mean(wr_buffer_gyo_x)
                wr_mean_gyo_y = get_mean(wr_buffer_gyo_y)
                wr_mean_gyo_z = get_mean(wr_buffer_gyo_z)

                ua_mean_gyo_x = get_mean(ua_buffer_gyo_x)
                ua_mean_gyo_y = get_mean(ua_buffer_gyo_y)
                ua_mean_gyo_z = get_mean(ua_buffer_gyo_z)

                be_mean_gyo_x = get_mean(be_buffer_gyo_x)
                be_mean_gyo_y = get_mean(be_buffer_gyo_y)
                be_mean_gyo_z = get_mean(be_buffer_gyo_z)

                # gyo standard deviations

                lp_standard_deviation_gyo_x = get_standard_deviation(lp_buffer_gyo_x, lp_mean_gyo_x)
                lp_standard_deviation_gyo_y = get_standard_deviation(lp_buffer_gyo_y, lp_mean_gyo_y)
                lp_standard_deviation_gyo_z = get_standard_deviation(lp_buffer_gyo_z, lp_mean_gyo_z)

                rp_standard_deviation_gyo_x = get_standard_deviation(rp_buffer_gyo_x, rp_mean_gyo_x)
                rp_standard_deviation_gyo_y = get_standard_deviation(rp_buffer_gyo_y, rp_mean_gyo_y)
                rp_standard_deviation_gyo_z = get_standard_deviation(rp_buffer_gyo_z, rp_mean_gyo_z)

                wr_standard_deviation_gyo_x = get_standard_deviation(wr_buffer_gyo_x, wr_mean_gyo_x)
                wr_standard_deviation_gyo_y = get_standard_deviation(wr_buffer_gyo_y, wr_mean_gyo_y)
                wr_standard_deviation_gyo_z = get_standard_deviation(wr_buffer_gyo_z, wr_mean_gyo_z)

                ua_standard_deviation_gyo_x = get_standard_deviation(ua_buffer_gyo_x, ua_mean_gyo_x)
                ua_standard_deviation_gyo_y = get_standard_deviation(ua_buffer_gyo_y, ua_mean_gyo_y)
                ua_standard_deviation_gyo_z = get_standard_deviation(ua_buffer_gyo_z, ua_mean_gyo_z)

                be_standard_deviation_gyo_x = get_standard_deviation(be_buffer_gyo_x, be_mean_gyo_x)
                be_standard_deviation_gyo_y = get_standard_deviation(be_buffer_gyo_y, be_mean_gyo_y)
                be_standard_deviation_gyo_z = get_standard_deviation(be_buffer_gyo_z, be_mean_gyo_z)

                # correlations gyo

                lp_correlation_gyo_xy = get_correlation(lp_buffer_gyo_x, lp_buffer_gyo_y,
                                                        lp_mean_gyo_x, lp_mean_gyo_y,
                                                        lp_standard_deviation_gyo_x, lp_standard_deviation_gyo_y)

                lp_correlation_gyo_xz = get_correlation(lp_buffer_gyo_x, lp_buffer_gyo_z,
                                                        lp_mean_gyo_x, lp_mean_gyo_z,
                                                        lp_standard_deviation_gyo_x, lp_standard_deviation_gyo_z)

                lp_correlation_gyo_yz = get_correlation(lp_buffer_gyo_z, lp_buffer_gyo_y,
                                                        lp_mean_gyo_z, lp_mean_gyo_y,
                                                        lp_standard_deviation_gyo_z, lp_standard_deviation_gyo_y)

                rp_correlation_gyo_xy = get_correlation(rp_buffer_gyo_x, rp_buffer_gyo_y,
                                                        rp_mean_gyo_x, rp_mean_gyo_y,
                                                        rp_standard_deviation_gyo_x, rp_standard_deviation_gyo_y)

                rp_correlation_gyo_xz = get_correlation(rp_buffer_gyo_x, rp_buffer_gyo_z,
                                                        rp_mean_gyo_x, rp_mean_gyo_z,
                                                        rp_standard_deviation_gyo_x, rp_standard_deviation_gyo_z)

                rp_correlation_gyo_yz = get_correlation(rp_buffer_gyo_z, rp_buffer_gyo_y,
                                                        rp_mean_gyo_z, rp_mean_gyo_y,
                                                        rp_standard_deviation_gyo_z, rp_standard_deviation_gyo_y)

                wr_correlation_gyo_xy = get_correlation(wr_buffer_gyo_x, wr_buffer_gyo_y,
                                                        wr_mean_gyo_x, wr_mean_gyo_y,
                                                        wr_standard_deviation_gyo_x, wr_standard_deviation_gyo_y)

                wr_correlation_gyo_xz = get_correlation(wr_buffer_gyo_x, wr_buffer_gyo_z,
                                                        wr_mean_gyo_x, wr_mean_gyo_z,
                                                        wr_standard_deviation_gyo_x, wr_standard_deviation_gyo_z)

                wr_correlation_gyo_yz = get_correlation(wr_buffer_gyo_z, wr_buffer_gyo_y,
                                                        wr_mean_gyo_z, wr_mean_gyo_y,
                                                        wr_standard_deviation_gyo_z, wr_standard_deviation_gyo_y)

                ua_correlation_gyo_xy = get_correlation(ua_buffer_gyo_x, ua_buffer_gyo_y,
                                                        ua_mean_gyo_x, ua_mean_gyo_y,
                                                        ua_standard_deviation_gyo_x, ua_standard_deviation_gyo_y)

                ua_correlation_gyo_xz = get_correlation(ua_buffer_gyo_x, ua_buffer_gyo_z,
                                                        ua_mean_gyo_x, ua_mean_gyo_z,
                                                        ua_standard_deviation_gyo_x, ua_standard_deviation_gyo_z)

                ua_correlation_gyo_yz = get_correlation(ua_buffer_gyo_z, ua_buffer_gyo_y,
                                                        ua_mean_gyo_z, ua_mean_gyo_y,
                                                        ua_standard_deviation_gyo_z, ua_standard_deviation_gyo_y)

                be_correlation_gyo_xy = get_correlation(be_buffer_gyo_x, be_buffer_gyo_y,
                                                        be_mean_gyo_x, be_mean_gyo_y,
                                                        be_standard_deviation_gyo_x, be_standard_deviation_gyo_y)

                be_correlation_gyo_xz = get_correlation(be_buffer_gyo_x, be_buffer_gyo_z,
                                                        be_mean_gyo_x, be_mean_gyo_z,
                                                        be_standard_deviation_gyo_x, be_standard_deviation_gyo_z)

                be_correlation_gyo_yz = get_correlation(be_buffer_gyo_z, be_buffer_gyo_y,
                                                        be_mean_gyo_z, be_mean_gyo_y,
                                                        be_standard_deviation_gyo_z, be_standard_deviation_gyo_y)

                # storing the fucking data

                data_list.append([lp_mean_acc_x, lp_mean_acc_y, lp_mean_acc_z,
                                  lp_standard_deviation_acc_x, lp_standard_deviation_acc_y, lp_standard_deviation_acc_z,
                                  lp_correlation_acc_xy, lp_correlation_acc_xz, lp_correlation_acc_yz,
                                  lp_energy_acc_x, lp_energy_acc_y, lp_energy_acc_z,
                                  lp_mean_gyo_x, lp_mean_gyo_y, lp_mean_gyo_z,
                                  lp_standard_deviation_gyo_x, lp_standard_deviation_gyo_y, lp_standard_deviation_gyo_z,
                                  lp_correlation_gyo_xy, lp_correlation_gyo_xz, lp_correlation_gyo_yz])

                data_list.append([rp_mean_acc_x, rp_mean_acc_y, rp_mean_acc_z,
                                  rp_standard_deviation_acc_x, rp_standard_deviation_acc_y, rp_standard_deviation_acc_z,
                                  rp_correlation_acc_xy, rp_correlation_acc_xz, rp_correlation_acc_yz,
                                  rp_energy_acc_x, rp_energy_acc_y, rp_energy_acc_z,
                                  rp_mean_gyo_x, rp_mean_gyo_y, rp_mean_gyo_z,
                                  rp_standard_deviation_gyo_x, rp_standard_deviation_gyo_y, rp_standard_deviation_gyo_z,
                                  rp_correlation_gyo_xy, rp_correlation_gyo_xz, rp_correlation_gyo_yz])

                data_list.append([wr_mean_acc_x, wr_mean_acc_y, wr_mean_acc_z,
                                  wr_standard_deviation_acc_x, wr_standard_deviation_acc_y, wr_standard_deviation_acc_z,
                                  wr_correlation_acc_xy, wr_correlation_acc_xz, wr_correlation_acc_yz,
                                  wr_energy_acc_x, wr_energy_acc_y, wr_energy_acc_z,
                                  wr_mean_gyo_x, wr_mean_gyo_y, wr_mean_gyo_z,
                                  wr_standard_deviation_gyo_x, wr_standard_deviation_gyo_y, wr_standard_deviation_gyo_z,
                                  wr_correlation_gyo_xy, wr_correlation_gyo_xz, wr_correlation_gyo_yz])

                data_list.append([ua_mean_acc_x, ua_mean_acc_y, ua_mean_acc_z,
                                  ua_standard_deviation_acc_x, ua_standard_deviation_acc_y, ua_standard_deviation_acc_z,
                                  ua_correlation_acc_xy, ua_correlation_acc_xz, ua_correlation_acc_yz,
                                  ua_energy_acc_x, ua_energy_acc_y, ua_energy_acc_z,
                                  ua_mean_gyo_x, ua_mean_gyo_y, ua_mean_gyo_z,
                                  ua_standard_deviation_gyo_x, ua_standard_deviation_gyo_y, ua_standard_deviation_gyo_z,
                                  ua_correlation_gyo_xy, ua_correlation_gyo_xz, ua_correlation_gyo_yz])

                data_list.append([be_mean_acc_x, be_mean_acc_y, be_mean_acc_z,
                                  be_standard_deviation_acc_x, be_standard_deviation_acc_y, be_standard_deviation_acc_z,
                                  be_correlation_acc_xy, be_correlation_acc_xz, be_correlation_acc_yz,
                                  be_energy_acc_x, be_energy_acc_y, be_energy_acc_z,
                                  be_mean_gyo_x, be_mean_gyo_y, be_mean_gyo_z,
                                  be_standard_deviation_gyo_x, be_standard_deviation_gyo_y, be_standard_deviation_gyo_z,
                                  be_correlation_gyo_xy, be_correlation_gyo_xz, be_correlation_gyo_yz])

                target_list.append(current_activity)
                target_list.append(current_activity)
                target_list.append(current_activity)
                target_list.append(current_activity)
                target_list.append(current_activity)

                lp_buffer_acc_x = []
                lp_buffer_acc_y = []
                lp_buffer_acc_z = []

                lp_buffer_gyo_x = []
                lp_buffer_gyo_y = []
                lp_buffer_gyo_z = []

                rp_buffer_acc_x = []
                rp_buffer_acc_y = []
                rp_buffer_acc_z = []

                rp_buffer_gyo_x = []
                rp_buffer_gyo_y = []
                rp_buffer_gyo_z = []

                wr_buffer_acc_x = []
                wr_buffer_acc_y = []
                wr_buffer_acc_z = []

                wr_buffer_gyo_x = []
                wr_buffer_gyo_y = []
                wr_buffer_gyo_z = []

                ua_buffer_acc_x = []
                ua_buffer_acc_y = []
                ua_buffer_acc_z = []

                ua_buffer_gyo_x = []
                ua_buffer_gyo_y = []
                ua_buffer_gyo_z = []

                be_buffer_acc_x = []
                be_buffer_acc_y = []
                be_buffer_acc_z = []

                be_buffer_gyo_x = []
                be_buffer_gyo_y = []
                be_buffer_gyo_z = []

                i = 0

        else:
            skip -= 1

    return target_list, data_list
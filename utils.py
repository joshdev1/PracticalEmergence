import numpy as np


def get_xt_window(xt_window, est_rates, counter, WINDOW_SIZE):
    if counter > WINDOW_SIZE:
        for i in range(WINDOW_SIZE):
            xt_window[:, i] = est_rates[(counter - WINDOW_SIZE) + i]


def get_xt(xt, xt_list, counter):
    xt[:, 0] = xt_list[counter]
    xt[:, 1] = xt_list[counter+1]


def get_vt(vt, xt, xt_window):
    for i in range(len(xt)):
        vt[i] = np.mean(xt_window[i, :])  # calculate mean for each row of data


def get_spatial_vt(neighbours, xt, vt):
    out = []
    load = xt[:, 1]
    tmp = np.pad(load, [neighbours, neighbours])
    for i in range(len(load) + neighbours):
        out.append(sum(tmp[i-neighbours:i+neighbours+1]))
    vt[:, 0] = out[neighbours:]


def get_spatial_vt_all(xt, vt):
    vt[:] = np.mean(xt[:, 1])


def get_vt_full_ca_mean(vt, xt, xt_window):
    for i in range(len(xt)):
        vt[i] = np.mean(xt_window[:, :])


def get_vt_trace(vt_trace, vt, total_mean_vt_trace):
    vt_trace.append(vt[0] * 10)  # added the constant terms for better plotting
    total_mean_vt_trace.append(np.mean(vt))

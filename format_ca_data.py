import math


def get_potentials_and_ca_ovlps(data):
    raw_potentials = []
    raw_ca1_ovlps = []
    for line in range(len(data)):
        if line % 2 == 0:
            raw_potentials.append(data[line].strip())
        else:
            raw_ca1_ovlps.append(data[line].strip())
    return raw_potentials, raw_ca1_ovlps


def get_estr_and_ovlps(data):
    estr = []
    ovlps = []
    for line in range(len(data)):
        if line % 2 == 0:
            estr.append(data[line].strip())
        else:
            ovlps.append(data[line].strip())
    return estr, ovlps


def remove_newlines(data):
    ca_ovlps = []
    for line in range(len(data)):
        ca_ovlps.append(data[line].strip())
    return ca_ovlps


def get_control(data):
    control = []
    for line in range(len(data)):
        control.append(data[line].strip())
    return control


def format_data(data):
    formatted_data = []
    for timestep in range(len(data)):
        float_data = []
        string_data = data[timestep].split()
        for value in range(len(string_data)):
            float_data.append(float(string_data[value]))
        formatted_data.append(float_data)
    return formatted_data


def get_ca_activation_level(ovlps, ca_size):
    ca_activation_level = []
    for i in range(len(ovlps)):
        ca_activation_level.append(sum(ovlps[i])/ca_size)  # normalize activation level
    return ca_activation_level


def get_normalised_rate(est_rates):
    normalised_rates = []
    for rates in est_rates:
        normalised_rates.append(sum(rates)/len(rates))
    return normalised_rates


def string_to_float_list(string_list):
    float_list = []
    for i in range(len(string_list)):
        if math.isnan(float(string_list[i])):
            float_list.append(0)
        else:
            float_list.append(float(string_list[i]))
    return float_list


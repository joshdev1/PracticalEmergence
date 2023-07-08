import numpy as np
from scipy import stats
from format_ca_data import string_to_float_list


def get_criteria_mean(criteria):
    string_data = criteria.split()
    float_data = string_to_float_list(string_data)
    return np.mean(float_data)


control_psi_means = []
control_delta_means = []
control_gamma_means = []
for file_num in range(1, 30):
    file = open(f"data_sets/Dataset1/control_results/ca1_control_{file_num}_res.txt", "r")
    control_data = file.readlines()
    file.close()

    control_psi_means.append(get_criteria_mean(control_data[0]))  # psi
    control_delta_means.append(get_criteria_mean(control_data[1]))  # delta
    control_gamma_means.append(get_criteria_mean(control_data[2]))  # gamma

print(control_gamma_means)


psi_means = []
delta_means = []
gamma_means = []
for file_num in range(1, 30):
    file = open(f"data_sets/Dataset1/timelocked_results/ca1_d1_{file_num}_res.txt", "r")
    data = file.readlines()
    file.close()

    psi_means.append(get_criteria_mean(data[0]))  # psi
    delta_means.append(get_criteria_mean(data[1]))  # delta
    gamma_means.append(get_criteria_mean(data[2]))  # gamma

print(gamma_means)

print(stats.ttest_ind(control_gamma_means, gamma_means))




import numpy as np
from scipy.stats import wilcoxon, ttest_ind
from format_ca_data import string_to_float_list
from matplotlib import pyplot as plt
import seaborn as sns


def subtract(L1,L2):
    return [x1-x2 for x1, x2 in zip(L1, L2)]


def get_criteria_mean(criteria):
    string_data = criteria.split()
    float_data = string_to_float_list(string_data)
    return np.mean(float_data)


control_psi_means = []
control_delta_means = []
control_gamma_means = []
for file_name in ["ca1_control_", "ca3_control_", "ca6_control_"]:
    for file_num in range(1, 31):
        file = open(f"data_sets/Dataset1/control_results/{file_name}{file_num}_res.txt", "r")
        control_data = file.readlines()
        file.close()

        control_psi_means.append(get_criteria_mean(control_data[0]))  # psi
        control_delta_means.append(get_criteria_mean(control_data[1]))  # delta
        control_gamma_means.append(get_criteria_mean(control_data[2]))  # gamma


psi_means = []
delta_means = []
peak_gamma_values = []
for file_name in ["ca1_d1_", "ca3_d1_", "ca6_d1_"]:
    for file_num in range(1, 31):
        file = open(f"data_sets/Dataset1/timelocked_results/{file_name}{file_num}_res.txt", "r")
        data = file.readlines()
        file.close()

        psi_means.append(get_criteria_mean(data[0]))  # psi
        delta_means.append(get_criteria_mean(data[1]))  # delta
        # gamma_means.append(get_criteria_mean(data[2]))  # gamma
        string_data = data[2].split()
        peak_gamma_values.append(float(string_data[25]))



print("----------------Results---------------------")
# Wilcox signed rank
# x = subtract(control_gamma_means, gamma_means)
# rx = list(np.around(np.array(x), 5))
# print("Gamma result: ", wilcoxon(rx))

# Paired t-test
print("Psi Result:", ttest_ind(psi_means, control_psi_means))
print("Peak Gamma Result:", ttest_ind(peak_gamma_values, control_gamma_means))


# plot gamma
# fig, ax = plt.subplots(figsize=(10, 7))
# ax.hist(peak_gamma_values)
# ax.set_title("Peak Gamma")
# ax.set_xlabel("Bins")
# ax.set_ylabel("occurrences")
#
# fig2, ax2 = plt.subplots(figsize=(10, 7))
# ax2.hist(control_gamma_means)
# ax2.set_title("Control Gamma means")
# ax2.set_xlabel("Bins")
# ax2.set_ylabel("occurrences")
# plt.show()

# plot psi
# fig1, ax1 = plt.subplots(figsize=(10, 7))
# ax1.hist(psi_means)
# ax1.set_title("Psi Means")
# ax1.set_xlabel("Bins")
# ax1.set_ylabel("occurrences")
#
# fig3, ax3 = plt.subplots(figsize=(10, 7))
# ax3.hist(control_psi_means)
# ax3.set_title("Control Psi Means")
# ax3.set_xlabel("Bins")
# ax3.set_ylabel("occurrences")

# boxplots for final results
# fig4, ax4 = plt.subplots(figsize=(6, 5))
# ax4.boxplot([control_psi_means, psi_means])
# ax4.set_title("Emergence", fontsize=18)
# ax4.set_xticklabels(["Baseline", "CA ignition"], fontsize=18)
# ax4.set_ylabel("Psi Level", fontsize=18)
#
#
# fig5, ax5 = plt.subplots(figsize=(6, 5))
# ax5.boxplot([control_gamma_means, peak_gamma_values])
# ax5.set_title("Causal Decoupling", fontsize=18)
# ax5.set_xticklabels(["Baseline", "CA ignition"], fontsize=18)
# ax5.set_ylabel("Gamma Level", fontsize=18)
# plt.show()

ax = sns.boxplot([control_psi_means, psi_means])
ax = sns.swarmplot([control_psi_means, psi_means], color=".25")
plt.show()

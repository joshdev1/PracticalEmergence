from matplotlib import pyplot as plt
from format_ca_data import format_data, get_normalised_rate, get_estr_and_ovlps
import numpy as np
from oct2py import Oct2Py
from graph import plot_practical_criteria

from vt import get_xt, get_vt_trace, get_spatial_vt

oc = Oct2Py()
oc.addpath('D:\Projects\PracticalEmergence\ReconcilingEmergences-master\ReconcilingEmergences-master')

ca = "ca6_d1_30"
file = open(f"data_sets/Dataset1/timelocked_data/{ca}.txt", "r")

data = file.readlines()
file.close()

raw_est_rates, raw_ovlps = get_estr_and_ovlps(data)
est_rates = format_data(raw_est_rates)
ovlps = format_data(raw_ovlps)


CA_SIZE = 136
NEIGHBOURS = 20
xt = np.zeros([CA_SIZE, 2])
vt = np.ones((CA_SIZE, 1))
vt_trace = []
total_mean_vt_trace = []

rates_level = get_normalised_rate(est_rates)
# ca_activation_level = get_ca_activation_level(ovlps, CA_SIZE)

psi_trace = []
surr_psi_mean = []
delta_trace = []
gamma_trace = []
counter = 0
for epoch in range(len(est_rates) - 1):
    get_xt(xt, est_rates, counter)
    get_spatial_vt(NEIGHBOURS, xt, vt)
    get_vt_trace(vt_trace, vt, total_mean_vt_trace)
    counter += 1

    psi = oc.EmergencePsi(xt, vt)      # psi > 0, then V is causally emergent.
    delta = oc.EmergenceDelta(xt, vt)  # delta > 0, then V shows downward causation.
    gamma = oc.EmergenceGamma(xt, vt)  # gamma(psi > 0 and Γ = 0), then V shows causal decoupling.

    surr_vt = vt
    surr_psi = []
    for i in range(10):
        shuffled_xt = np.random.permutation(xt)
        shuffled_vt = np.random.permutation(surr_vt)
        spsi = oc.EmergencePsi(shuffled_xt, shuffled_vt)
        surr_psi.append(spsi)
        print(spsi)

    surr_psi_mean.append(np.mean(surr_psi))

    psi_trace.append(psi)
    delta_trace.append(delta)
    gamma_trace.append(gamma)

    print(f"psi = {psi}\n delta = {delta}\n gamma = {gamma}\n epoch = {epoch}")
    print(f"surr_psi_mean: {surr_psi_mean[epoch]}")


print("------------\n")

with open(f'data_sets/Dataset1/surrogate_data/{ca}_surr.txt', 'w') as f:
    for line in surr_psi_mean:
        f.write(f"{line} ")
    f.write(f"\n")

# with open(f'data_sets/Dataset1/timelocked_results/{ca}_res.txt', 'w') as f:
#     for line in psi_trace:
#         f.write(f"{line} ")
#     f.write(f"\n")
#     for line in delta_trace:
#         f.write(f"{line} ")
#     f.write(f"\n")
#     for line in gamma_trace:
#         f.write(f"{line} ")
#     f.write(f"\n")
#     for line in rates_level:
#         f.write(f"{line} ")


plt.figure(1)
plot_practical_criteria(len(est_rates) - 1, psi_trace, "psi", "CA6")
plot_practical_criteria(len(est_rates) - 1, surr_psi_mean, "surr_psi_mean", "CA6")
plot_practical_criteria(len(est_rates) - 1, delta_trace, "delta", "CA6")
plot_practical_criteria(len(est_rates) - 1, gamma_trace, "gamma", "CA6")
# plt.plot(range(len(est_rates) - 1), total_mean_vt_trace, label='Vt (Mean membrane potential)')
plt.plot(range(len(est_rates) - 1), rates_level[:len(est_rates) - 1], label="Estimated Firing Rates")
# plt.plot(range(len(ovlps) - 1), ca_activation_level[:len(ovlps) - 1], label="ca activation (ovlps)")
plt.legend()

plt.show()

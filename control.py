from matplotlib import pyplot as plt
from format_ca_data import format_data, get_normalised_rate, get_control
import numpy as np
from oct2py import Oct2Py
from graph import plot_practical_criteria

from vt import get_xt, get_vt_trace, get_spatial_vt

oc = Oct2Py()
oc.addpath('D:\Projects\PracticalEmergence\ReconcilingEmergences-master\ReconcilingEmergences-master')

ca = "ca1_control_30"
file = open(f"data_sets/Dataset1/control_data/{ca}.txt", "r")
data = file.readlines()
file.close()

raw_control = get_control(data)
est_rates = format_data(raw_control)


CA_SIZE = 151
NEIGHBOURS = 20
xt = np.zeros([CA_SIZE, 2])
vt = np.ones((CA_SIZE, 1))
vt_trace = []
total_mean_vt_trace = []

rates_level = get_normalised_rate(est_rates)
# random.shuffle(est_rates)  # shuffle the data for surrogate testing/resampling

psi_trace = []
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

    psi_trace.append(psi)
    delta_trace.append(delta)
    gamma_trace.append(gamma)

    print(f"psi = {psi}\n delta = {delta}\n gamma = {gamma}\n epoch = {epoch}")


print("------------\n")

with open(f'data_sets/Dataset1/control_results/{ca}_res.txt', 'w') as f:
    for line in psi_trace:
        f.write(f"{line} ")
    f.write(f"\n")
    for line in delta_trace:
        f.write(f"{line} ")
    f.write(f"\n")
    for line in gamma_trace:
        f.write(f"{line} ")
    f.write(f"\n")
    for line in rates_level:
        f.write(f"{line} ")


plt.figure(1)
plot_practical_criteria(len(est_rates) - 1, psi_trace, "psi", "Firing rate - Control Condition")
plot_practical_criteria(len(est_rates) - 1, delta_trace, "delta", "Firing rate - Control Condition")
plot_practical_criteria(len(est_rates) - 1, gamma_trace, "gamma", "Firing rate - Control Condition")
plt.plot(range(len(est_rates) - 1), rates_level[:len(est_rates) - 1], label="Firing Rates")
plt.legend()

plt.show()




from random import random

import numpy as np
from oct2py import Oct2Py
from graph import plot_supervenient_feature, plot_practical_criteria
from lif_neuron import LIFNeuron
from matplotlib import pyplot as plt

oc = Oct2Py()
oc.addpath('D:\Projects\PracticalEmergence\ReconcilingEmergences-master\ReconcilingEmergences-master')

NEURONS = 10

xt = np.random.uniform(-0.07, -0.05, (NEURONS, 2))  # The microscopic elements of the system ie the neurons
vt = np.ones((NEURONS, 1))  # The macroscopic elements of the system ie the supervenient/emergent feature
                            # In this case this is the mean activity of each neurons in the netowrk calculated as the
                            # moving average of the last 2 timesteps. Possibly make number of timesteps variable.

vt_trace = []
total_mean_vt_trace = []


input_v_standard = 0.1e-3

lif_neuron = LIFNeuron(3e-9, random.uniform(10.5, 75.5), 15e-3)  # lif neuron for calculating membrane potentials
update_membrane_potentials = np.vectorize(lif_neuron.get_membrane_potential)  # apply membrane potential calculation to numpy array


def get_xt_window(xt_window, potentials, counter):
    if counter > 4:
        for i in range(4):
            xt_window[:, i] = potentials[counter+i]
        # else:
        #     xt[:, 0] = potentials[counter]
        #     xt[:, 1] = potentials[counter + 1]


def get_vt_trace(vt_trace, vt):
    vt_trace.append(vt[0] * 10)  # added the constant terms for better plotting
    total_mean_vt_trace.append(np.mean(vt) * 10)


def get_vt(vt, xt):
    for i in range(len(xt)):
        vt[i] = np.mean(xt[i, :])  # calculate mean for each row of data


def get_xt(xt):
    xt[:, 0] = xt[:, 1]                              # update first column (t-1) with the values from t
    xt[:, 1] = update_membrane_potentials(xt[:, 1])  # update second column (t) with new membrane potential values


EPOCHS = 20
psi_trace = []
delta_trace = []
gamma_trace = []

for epoch in range(EPOCHS):
    get_xt(xt)
    get_vt(vt, xt)

    get_vt_trace(vt_trace, vt)

    psi = oc.EmergencePsi(xt, vt)      # psi > 0, then V is causally emergent.
    delta = oc.EmergenceDelta(xt, vt)  # delta > 0, then V shows downward causation.
    gamma = oc.EmergenceGamma(xt, vt)  # gamma(psi > 0 and Γ = 0), then V shows causal decoupling.

    psi_trace.append(psi)
    delta_trace.append(delta)
    gamma_trace.append(gamma)

    print(f"psi = {psi}\n delta = {delta}\n gamma = {gamma}\n epoch = {epoch}")


# plot_supervenient_feature(range(EPOCHS), vt_trace, 1)
# plot_supervenient_feature(range(EPOCHS), total_mean_vt_trace, 2)

plot_practical_criteria(EPOCHS, psi_trace, "psi")
plot_practical_criteria(EPOCHS, delta_trace, "delta")
plot_practical_criteria(EPOCHS, gamma_trace, "gamma")
plt.show()

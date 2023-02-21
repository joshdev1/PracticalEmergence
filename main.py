import numpy as np
from oct2py import Oct2Py
from graph import plot_supervenient_feature
from lif_neuron import LIFNeuron
from matplotlib import pyplot as plt

oc = Oct2Py()
oc.addpath('D:\Projects\PracticalEmergence\ReconcilingEmergences-master\ReconcilingEmergences-master')

xt = np.random.uniform(-0.07, -0.05, (10, 2))  # The microscopic elements of the system ie the neurons
vt = np.ones((10, 1))  # The macroscopic elements of the system ie the supervenient/emergent feature

vt_trace = []
total_mean_vt_trace = []

lif_neuron = LIFNeuron(3e-9, 0.1e-3, 15e-3)  # lif neuron for calculating membrane potentials
# TODO add a random input current to each neuron to compare with this value
mem_vector = np.vectorize(lif_neuron.get_membrane_potential)  # apply membrane potential calculation to numpy array


def get_vt_trace(vt_trace, vt):
    vt_trace.append(vt[0] * 10)  # added the constant terms for better plotting
    total_mean_vt_trace.append(np.mean(vt) * 10)


def get_vt(vt, xt):
    for i in range(2):
        vt[i] = np.mean(xt[i])


def get_xt(xt):
    x = mem_vector(xt[:, 1])
    xt[:, 0] = xt[:, 1]  # update first column with the second columns values (old xt+1 values)
    xt[:, 1] = x         # update second column with new xt+1 values


EPOCHS = 3
for epoch in range(EPOCHS):
    get_xt(xt)
    get_vt(vt, xt)

    get_vt_trace(vt_trace, vt)

    psi = oc.EmergencePsi(xt, vt)
    delta = oc.EmergenceDelta(xt, vt)
    gamma = oc.EmergenceGamma(xt, vt)

    print(f"psi = {psi}\n delta = {delta}\n gamma = {gamma}\n epoch = {epoch}")
    # TODO add plotting for psi delta and gamma
    # TODO could be interesting to also compute the mutual information of the neurons to build more
    #  intuition for the system

plot_supervenient_feature(range(EPOCHS), vt_trace, 1)
plot_supervenient_feature(range(EPOCHS), total_mean_vt_trace, 2)
plt.show()

# plot_membrane_potential(neuron_num="1", time_steps=EPOCHS, membrane_trace=membrane_trace[0], figure_num=1)
# plot_membrane_potential(neuron_num="2", time_steps=EPOCHS, membrane_trace=membrane_trace[1], figure_num=2)
# plot_supervenient_feature(EPOCHS, vt_trace, 3)
# plt.show()

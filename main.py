from matplotlib import pyplot as plt
import numpy as np
from lif_neuron import LIFNeuron
from supervenient import get_membranes_average, get_running_membrane_average
from graph import plot_membrane_potential, plot_supervenient_feature
import random
from oct2py import Oct2Py

oc = Oct2Py()
oc.addpath('D:\Projects\PracticalEmergence\ReconcilingEmergences-master\ReconcilingEmergences-master')

NETWORK_SIZE = range(4)
EPOCHS = range(5)
vt_trace = []  # The supervenient feature aka the average activity across all neurons.

# vectors for Xt and Vt
vt = np.ones((4, 1))

lif_neuron = LIFNeuron(3e-9, 0.1e-3, 15e-3)  # for calculating membrane potentials

# create network and set random initial membrane potentials
network = [random.uniform(-0.07, -0.05) for i in NETWORK_SIZE]
membrane_trace = [[] for membrane in NETWORK_SIZE]  # track membrane potentials across time


def init_random_xt():
    return np.random.uniform(-0.07, -0.05, (4, 2))


def get_xt(xt):
    for i in NETWORK_SIZE:
        for j in NETWORK_SIZE:
            xt[i, j] = lif_neuron.get_membrane_potential(xt[i, j])
    return xt


def get_vt(xt, vt, epoch):
    for i in range(2):
        vt[i] += xt[i, 1]
        if epoch % 5 == 0:
            vt[i] = vt[i] / 5
    return vt


for epoch in EPOCHS:
    for neuron in range(len(network)):
        network[neuron] = lif_neuron.get_membrane_potential(network[neuron])
        membrane_trace[neuron].append(network[neuron])
    vt_trace.append(get_membranes_average(membrane_trace))

    xt = init_random_xt()
    print(get_xt(xt))
    get_vt(xt, vt, epoch)

    psi = oc.EmergencePsi(xt, vt)
    delta = oc.EmergenceDelta(xt, vt)
    gamma = oc.EmergenceGamma(xt, vt)

    print(f"psi = {psi}\n delta = {delta}\n gamma = {gamma}\n epoch = {epoch} ")


# plot_membrane_potential(neuron_num="1", time_steps=EPOCHS, membrane_trace=membrane_trace[0], figure_num=1)
# plot_membrane_potential(neuron_num="2", time_steps=EPOCHS, membrane_trace=membrane_trace[1], figure_num=2)
# plot_supervenient_feature(EPOCHS, vt_trace, 3)
# plt.show()

import numpy as np
from oct2py import Oct2Py
from lif_neuron import LIFNeuron

oc = Oct2Py()
oc.addpath('D:\Projects\PracticalEmergence\ReconcilingEmergences-master\ReconcilingEmergences-master')

xt = np.random.uniform(-0.07, -0.05, (10, 2))
vt = np.ones((10, 1))

lif_neuron = LIFNeuron(3e-9, 0.1e-3, 15e-3)  # for calculating membrane potentials
mem_vector = np.vectorize(lif_neuron.get_membrane_potential)  # apply membrane potential calculation to numpy array


def get_vt(vt, xt):
    for i in range(2):
        vt[i] = np.mean(xt[i])
        # TODO return the list of vt for plotting


def get_xt(xt):
    x = mem_vector(xt[:, 1])
    xt[:, 0] = xt[:, 1]  # update first column with old xt+1 values
    xt[:, 1] = x         # update second column with new xt+1 values
    # TODO return the list of xt for plotting


for epoch in range(3):
    get_xt(xt)
    get_vt(vt, xt)

    psi = oc.EmergencePsi(xt, vt)
    delta = oc.EmergenceDelta(xt, vt)
    gamma = oc.EmergenceGamma(xt, vt)

    print(f"psi = {psi}\n delta = {delta}\n gamma = {gamma}\n epoch = {epoch} ")
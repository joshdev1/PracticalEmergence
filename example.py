import numpy as np
from oct2py import Oct2Py

oc = Oct2Py()
oc.addpath('D:\Projects\PracticalEmergence\ReconcilingEmergences-master\ReconcilingEmergences-master')

for epoch in range(3):
    xt = np.random.randn(5, 2)
    vt = np.random.randn(5, 1)

    psi = oc.EmergencePsi(xt, vt)
    delta = oc.EmergenceDelta(xt, vt)
    gamma = oc.EmergenceGamma(xt, vt)

    print(f"psi = {psi}\n delta = {delta}\n gamma = {gamma}\n epoch = {epoch} ")
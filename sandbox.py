import numpy as np
from lif_neuron import LIFNeuron
from graph import plot_membrane_potential

lif_neuron = LIFNeuron(3e-9, 0.1e-3, 15e-3)  # for calculating membrane potentials

vt = np.ones((2, 1))
xt = np.random.uniform(-0.07, -0.05, (2, 2))

# mem_vector = np.vectorize(lif_neuron.get_membrane_potential)


def get_xt(xt):
    mem_vector = np.vectorize(lif_neuron.get_membrane_potential)
    xt_1_values = xt[:, 1]
    new_xt_1_values = mem_vector(xt_1_values)

    xt[:, 0] = xt[:, 1]         # update first column with old xt+1 values
    xt[:, 1] = new_xt_1_values  # update second column with new xt+1 values


my_volts = []
for i in range(1000):
    xt_1_values = xt[:, 1]
    x = mem_vector(xt_1_values)
    xt[:, 0] = xt[:, 1]  # update first column with old xt+1 values
    xt[:, 1] = x         # update second column with new xt+1 values



    print(xt)
    print("---------------------")



    # my_volts.append(x[0])
    # print(my_volts)


plot_membrane_potential(neuron_num="1", time_steps=range(1000), membrane_trace=my_volts, figure_num=1)

from matplotlib import pyplot as plt
plt.show()

















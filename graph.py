from matplotlib import pyplot as plt


def plot_membrane_potential(neuron_num, time_steps, membrane_trace, figure_num):
    plt.figure(figure_num)
    plt.plot(time_steps, membrane_trace, color=u'#FFBB6C', label='Voltage')
    plt.title(f'Leaky Integrate-and-Fire Neuron {neuron_num}')
    plt.ylabel('Membrane Potential (Vm)')
    plt.xlabel('Time (ms)')


def plot_supervenient_feature(EPOCHS, vt, figure_num):
    plt.figure(figure_num)
    plt.plot(EPOCHS, vt, color=u'#FFBB6C', label='Voltage')
    plt.title(f'supervenient feature Vt')
    plt.ylabel('Average Membrane Potential (Vm)')
    plt.xlabel('Time (ms)')


def plot_practical_criteria(timesteps, criteria_trace, criteria_name, title):
    plt.plot(range(timesteps), criteria_trace, label=criteria_name)
    plt.legend()
    plt.title(f'Practical Criteria: {title}')
    plt.ylabel(f'value')
    plt.xlabel('Simulation Timestep')

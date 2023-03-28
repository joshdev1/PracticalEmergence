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


def plot_practical_criteria(EPOCHS, criteria_trace, criteria_name, figure_number):
    plt.figure(figure_number)
    plt.plot(range(EPOCHS), criteria_trace, color=u'#FFBB6C', label=criteria_name)
    plt.title(f'{criteria_name} trace')
    plt.ylabel(f'{criteria_name}')
    plt.xlabel('Epoch')

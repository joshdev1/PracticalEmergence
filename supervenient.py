def get_membrane_average(membrane):
    return sum(membrane) / len(membrane)


def get_membranes_average(membrane_traces):
    membrane_averages = []
    for membrane in membrane_traces:
        membrane_averages.append(get_membrane_average(membrane))
    return get_membrane_average(membrane_averages)


def get_running_membrane_average(xt, vt, epoch):
    for i in range(2):
        vt[i] += xt[i, 1]
        if epoch % 5 == 0:
            vt[i] = vt[i] / 5
    return vt

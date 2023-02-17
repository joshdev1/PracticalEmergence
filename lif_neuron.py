from matplotlib import pyplot as plt


class LIFNeuron:
    def __init__(self, input_voltage, dt, tau):
        self.input_voltage = input_voltage
        self.dt = dt
        self.tau = tau
        self.E = -0.065
        self.R = 10e6
        self.v_0 = -0.07
        self.v_thresh = -0.05
        self.v_reset = -0.067
        self.v = self.v_0

    def get_membrane_potential(self, previous_membrane_potential):
        return self._set_membrane_potential(previous_membrane_potential)

    def _set_membrane_potential(self, previous_membrane_potential):
        dv = self.dt * (self.E - previous_membrane_potential + self.R * self.input_voltage) / self.tau
        self.v = previous_membrane_potential + dv
        self._check_spike_threshold()
        return self.v

    def _check_spike_threshold(self):
        if self.v > self.v_thresh:
            self.v = self.v_reset

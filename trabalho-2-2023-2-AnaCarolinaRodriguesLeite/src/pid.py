class PID:
    Kp = 0.5  # Proportional Gain
    Ki = 0.05  # Integral Gain
    Kd = 40.0  # Derivative Gain
    T = 0.8  # Sampling Period (ms)

    total_error = 0
    previous_error = 0

    control_signal_MAX = 100
    control_signal_MIN = 0
    control_signal = 0
    reference = 10000
    
    def update_reference(self, reference):
        self.reference = reference

    def control(self, measured_output):
        errors = [ref - measured_output for ref in self.reference]
        for error in errors:
            self.total_error += error

        if self.total_error >= self.control_signal_MAX:
            self.total_error = self.control_signal_MAX
        elif self.total_error <= self.control_signal_MIN:
            self.total_error = self.control_signal_MIN

        delta_error = error - self.previous_error
        self.control_signal = self.Kp * error + (self.Ki * self.T) * self.total_error + (self.Kd / self.T) * delta_error

        if self.control_signal >= self.control_signal_MAX:
            self.control_signal = self.control_signal_MAX
        elif self.control_signal <= self.control_signal_MIN:
            self.control_signal = self.control_signal_MIN

        self.previous_error = error

        return self.control_signal
    
    # def control(self, measured_output):
    #     error = self.reference - measured_output
    #     self.total_error += error

    #     # Limitando o total_error
    #     self.total_error = max(min(self.total_error, self.control_signal_MAX), self.control_signal_MIN)

    #     delta_error = error - self.previous_error
    #     self.control_signal = self.Kp * error + (self.Ki * self.T) * self.total_error + (self.Kd / self.T) * delta_error

    #     # Limitando o control_signal
    #     self.control_signal = max(min(self.control_signal, self.control_signal_MAX), self.control_signal_MIN)

    #     self.previous_error = error

    #     return self.control_signal
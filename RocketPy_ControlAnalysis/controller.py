class AirbrakePID:
    def __init__(self, kp=0.01, ki=0.001, kd=0.005, target_apogee=3000):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.target_apogee = target_apogee
        self.integral_error = 0
        self.previous_error = 0

    def compute(self, altitude, velocity, dt=0.1):
        error = altitude - self.target_apogee
        self.integral_error += error * dt
        derivative_error = (error - self.previous_error) / dt if dt > 0 else 0
        self.previous_error = error
        
        output = (self.kp * error) + (self.ki * self.integral_error) + (self.kd * derivative_error)
        return max(0.0, min(1.0, output))  # Clamp between 0.0 and 1.0

pid_instance = AirbrakePID()

def airbrake_controller(time, sampling_rate, state, state_history, observed_variables, air_brakes):
    z = state[2]   # Altitude
    vz = state[5]  # Vertical velocity
    
    dt = 1.0 / sampling_rate if sampling_rate else 0.1
    deployment = pid_instance.compute(altitude=z, velocity=vz, dt=dt)
    
    air_brakes.deployment_level = deployment
    return deployment
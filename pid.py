import time

# Constants
DESIRED_ANGLE = 0.0     # Ideal angle (standing) = 0 degrees
LOOP_RATE = 10          # Hz
P_SCALAR = 1.0          # Modifying lines 6-8 would 'tune' the controller
I_SCALAR = 1.0
D_SCALAR = 1.0

class PID:

    ##
    # Class constructor
    #
    def __init__(self):
        self.last_angle = None
        self.integral_error = 0.0
        self.cycle_length = 1.0 / LOOP_RATE
        self.cycles = 0
        self.running = True

    ##
    # This would be connected to the sensor inputs
    #
    def get_angle(self):
        return None

    ##
    # This would be connected to the motor(s)
    #
    def power_motors(self, output):
        return

    ##
    # Main control loop
    #
    def run(self):
        while self.running:
            cycle_start = time.time()

            # Read sensor data and determine an angle
            angle = self.get_angle()

            # This will only happen the first cycle
            if self.last_angle is None:
                self.last_angle = angle

            else:
                # Attempts to account for any drifts
                self.integral_error += (DESIRED_ANGLE - angle) * self.cycle_length

                # Attempts to account for sharp changes
                derivative = (angle - self.last_angle) / self.cycle_length

                # Output is the sum of PID values * thier respecive scalars
                motor_output = angle * P_SCALAR + self.integral_error * I_SCALAR + derivative * D_SCALAR
                self.power_motors(motor_output)

            # Prepare for next cycle
            self.last_angle = angle
            self.cycles += 1

            # Enforce a constant loop rate
            cycle_time = time.time() - cycle_start
            if cycle_time < self.cycle_length:
                time.sleep(self.cycle_length - cycle_time)

##
# Python equivalent of "int main()" in C++ 
#
if __name__ == "__main__":
    pid_controller = PID()
    pid_controller.run()
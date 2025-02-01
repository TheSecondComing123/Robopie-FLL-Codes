import motor
from hub import port, motion_sensor
import time

# Define motor ports
lift_arm_port = port.D
razor_blade_port = port.C
left_motor_port = port.A
right_motor_port = port.E

# PID Constants for Precision
KP = 4.0   # Proportional (higher = faster correction)
KI = 0.01  # Integral (helps eliminate steady-state error)
KD = 1.2   # Derivative (reduces overshoot)

# Speed Control
MAX_SPEED = 600   # Maximum motor speed
MIN_SPEED = 40    # Minimum motor speed to avoid stall
ACCEL_RATE = 10   # How quickly it accelerates
DECEL_THRESHOLD = 30  # When to start slowing down (degrees from target)
TOLERANCE = 0.5   # Precision deadband (degrees)

def forward(degrees, speed=360, *, delay=0.25):
    motor.run_for_degrees(left_motor_port, -degrees, speed)
    motor.run_for_degrees(right_motor_port, degrees, speed)
    time.sleep(abs(degrees) / speed + delay)

def turn(degrees):
    if not (-720 <= degrees <= 720):
        print("Error: Turn angle out of range (-720 to 720).")
        return

    motion_sensor.reset_yaw()
    time.sleep(0.1)
    
    previous_error = 0
    integral = 0
    current_speed = MIN_SPEED

    while True:
        yaw_angle = motion_sensor.tilt_angles()[0] * -0.1
        error = degrees - yaw_angle
        integral += error
        derivative = error - previous_error
        previous_error = error

        # Calculate PID output
        power = (KP * error) + (KI * integral) + (KD * derivative)

        # Apply acceleration and deceleration
        if abs(error) > DECEL_THRESHOLD:
            current_speed = min(current_speed + ACCEL_RATE, MAX_SPEED)
        else:
            current_speed = max(current_speed - ACCEL_RATE, MIN_SPEED)

        power = max(min(power, current_speed), MIN_SPEED) if abs(error) > TOLERANCE else 0
        
        if power == 0:
            break

        motor.run(left_motor_port, power if degrees > 0 else -power)
        motor.run(right_motor_port, -power if degrees > 0 else power)
        time.sleep(0.01)

    motor.stop(left_motor_port)
    motor.stop(right_motor_port)
    time.sleep(0.1)

def move_front_motor(degrees, speed=360):
    motor.run_for_degrees(lift_arm_port, degrees, speed)
    time.sleep(0.25)

def move_back_motor(degrees, speed=360):
    motor.run_for_degrees(razor_blade_port, degrees, speed)
    time.sleep(0.25)

def run_lift_arm(degrees, speed=360, *, delay=0.25):
    motor.run_for_degrees(lift_arm_port, degrees, speed)
    time.sleep(abs(degrees) / speed + delay)

def reset_lift_arm_port():
    motor.run_for_degrees(lift_arm_port, 300, 360)
    time.sleep(0.25)

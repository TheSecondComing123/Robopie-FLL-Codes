import motor
from hub import port
import time

# Define motor ports
lift_arm_port = port.D
razor_blade_port = port.C
left_motor_port = port.A
right_motor_port = port.E

def forward(degrees, speed=360, *, delay=0.25): # postitive = forward, negative = backward
    motor.run_for_degrees(left_motor_port, -degrees, speed)
    motor.run_for_degrees(right_motor_port, degrees, speed)
    time.sleep(abs(degrees) / speed + delay)

def turn(degrees, speed=360, *, delay=0.25): # positive = left, negative = right
    degrees = int(degrees)
    motor.run_for_degrees(left_motor_port, degrees, speed)
    motor.run_for_degrees(right_motor_port, degrees, speed)
    time.sleep(abs(degrees) / speed + delay)
def move_front_motor(degrees, speed=360):
    motor.run_for_degrees(port.D, degrees, speed)
    time.sleep(0.25)
def move_back_motor(degrees, speed=360):
    motor.run_for_degrees(port.C, degrees, speed)
    time.sleep(0.25)
def run_lift_arm(degrees, speed=360, *, delay=0.25): # positive = up, negative = down
    motor.run_for_degrees(lift_arm_port, degrees, speed)
    time.sleep(abs(degrees) / speed + delay)

def reset_lift_arm_port(): 
    motor.run_for_degrees(lift_arm_port, 300, 360) 
    time.sleep(0.25)

import motor
from hub import port
import time

# Define motor ports
lift_arm_port = port.D
razor_blade_port = port.C
left_motor_port = port.A
right_motor_port = port.E

def forward(degrees, speed=360): # postitive = forward, negative = backward
    motor.run_for_degrees(left_motor_port, -degrees, speed)
    motor.run_for_degrees(right_motor_port, degrees, speed)
    time.sleep(abs(degrees) / speed + 0.25)

def turn(degrees, speed=360): # positive = left, negative = right
    degrees = int(degrees)
    motor.run_for_degrees(left_motor_port, degrees, speed)
    motor.run_for_degrees(right_motor_port, degrees, speed)
    time.sleep(abs(degrees) / speed + 0.25)

def run_lift_arm(degrees, speed=360): # positive = up, negative = down
    motor.run_for_degrees(lift_arm_port, degrees, speed)
    time.sleep(abs(degrees) / speed + 0.25)

def krakens_treasure():
    forward(100)
    turn(-75)
    forward(170)
    turn(60)
    forward(420)
    turn(-131)
    forward(214.5,100)
    forward(-250)

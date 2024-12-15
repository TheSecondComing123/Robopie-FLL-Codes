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


# --- run_1.py ---
def run1a():
    forward(0.2)
    turn(85)
    forward(2)

def run1b():
    forward(-1)

    turn(-100)
    motor.run_for_degrees(lift_arm_port, -360, 360)
    time.sleep(1)
    forward(0.55)
    motor.run_for_degrees(lift_arm_port, 360, 360)
    time.sleep(0.5)
    turn(-100)
    forward(-0.5)
    motor.run_for_degrees(lift_arm_port, 360, 360)


# --- run_4.py ---
def run4a():
    forward(-100, 180)
    turn(-20, 180)
    forward(165, 180)
    forward(-180)
    turn(100, 180)
    forward(-750, 180)
    turn(45, 180)
    forward(-130, 205)

def run4b():
    forward(270)
    turn(90, 180)
    forward(360, 270)
    turn(-30, 180)
    forward(200, 180)
    turn(-70, 180)
    forward(215, 180)
    turn(-75, 180)
    forward(360, 170)
    forward(-345, 150)

def run4c():
    forward(20)
    turn(60)
    forward(200)
    turn(90)
    forward(300)
    turn(50)
    forward(140)
    turn(-110,2200)
    forward(-150)
    forward(230)
    motor.run_for_degrees(lift_arm_port,600,2200)
    forward(300)
    forward(-250)
    motor.run_for_degrees(lift_arm_port,-200,2200)
    turn(-10)
    forward(400,2200)
    forward(-240)
    motor.run_for_degrees(lift_arm_port,100,2000)
    forward(200)


# --- run_6.py ---
def run6():
    # Aligner two spaces right of corner
    run_lift_arm(300)
    forward(150)
    turn(-70)
    forward(170)
    turn(45)
    forward(620)
    turn(115)
    forward(58)
    # Shark
    run_lift_arm(-320, 1660)
    run_lift_arm(240)
    forward(-150)
    turn(-238)
    # Coral Nursery
    forward(-200)
    run_lift_arm(-100)
    turn(140)
    forward(200)
    turn(-65)
    #Coral Habitat
    run_lift_arm(-300, 660)
    forward(20)
    run_lift_arm(-25, 660)
    forward(-60)
    #Angler Fish
    run_lift_arm(290)
    turn(-95)
    forward(300)
    turn(60)
    forward(160)
    run_lift_arm(-305, 660)
    turn(-40)
    forward(170)
    turn(-250)


# Call all functions in order
run1a()
run1b()
run4a()
run4b()
run4c()
run6()

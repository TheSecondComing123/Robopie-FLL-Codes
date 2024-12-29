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

def run_lift_arm(degrees, speed=360, *, delay=0.25): # positive = up, negative = down
    motor.run_for_degrees(lift_arm_port, degrees, speed)
    time.sleep(abs(degrees) / speed + delay)

def reset_lift_arm_port(): 
    motor.run_for_degrees(lift_arm_port, 300, 360) 
    time.sleep(0.25)


# --- run_1.py ---
def run1a():
    # Octopus, one left of right corner of right base
    reset_lift_arm_port()
    forward(100)
    turn(85)
    forward(700)

def run1b():
    # Change Shipping Lanes
    forward(-360)
    turn(-110)
    motor.run_for_degrees(lift_arm_port, -360, 360)
    time.sleep(1)
    forward(230)
    motor.run_for_degrees(lift_arm_port, 360, 360)
    time.sleep(0.5)
    turn(-100)
    forward(-180)
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
    motor.run_for_degrees(lift_arm_port, -250, 2200)
    forward(60)
    turn(60)
    forward(200)
    turn(100)
    forward(300)
    turn(45)
    forward(100)
    turn(-102,2200)
    turn(10,2200)
    forward(-100)
    #turn(15)
    forward(180)
    # turn(70)
    motor.run_for_degrees(lift_arm_port, 550, 2200)
    forward(250)
    forward(-175)
    motor.run_for_degrees(lift_arm_port, -210, 2200)
    turn(-10)
    forward(280,2200)
    forward(-500)
    # motor.run_for_degrees(lift_arm_port, -100, 2000)
    # motor.run_for_degrees(lift_arm_port,100,2000)
    # forward(200)

def run4c2():
    forward(40)
    turn(60)
    forward(200)
    turn(90)
    forward(290)
    turn(60)


# --- run_5.py ---
def run5():  
    # part of pink run!!! this should be taken when it arrives to be aligned.  
    motor.run_for_degrees(lift_arm_port, -250, 2200)
    forward(120)
    turn(-90)
    forward(200)
    turn(-25)
    forward(400)
    turn(-30)
    forward(1200)
    turn(-70)
    forward(600)
    
def run5b():
    motor.run_for_degrees(lift_arm_port, 180,2200)
    forward(230)
    turn(35)
    forward(200)
    turn(42)
    forward(300)
    turn(-30)
    forward(200)
    motor.run_for_degrees(lift_arm_port, -1000,2200)
    forward(180)
    forward(-200,2200)
    turn(40,2200)
    motor.run_for_degrees(lift_arm_port, -400,2200)
    forward(60,2200)
    turn(40,2200)
    #forward(90)
    #turn(-300)
    #forward(300)
    #turn(20)
    #turn(50)


# --- run_6.py ---
def run6():
    # Aligner two spaces right of corner
    forward(150)
    turn(-70)
    forward(170)
    turn(45)
    forward(620)
    turn(125)
    forward(110)
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
    # Coral Habitat
    run_lift_arm(-300, 660)
    forward(20)
    run_lift_arm(-25, 660)
    forward(-60)
    # Angler Fish
    run_lift_arm(290)
    turn(-95)
    forward(300)
    turn(60)
    forward(190)
    run_lift_arm(-305, 660)
    turn(-60)
    forward(200)
    turn(-250)
    #Back to home base
    forward(-100)
    turn(-90)
    forward(100)
    turn(-50)
    forward(250)
    turn(60)
    forward(330)
    


# Call all functions in order
run1a()
run1b()
run4a()
run4b()
run4c()
run5()
run5b()
run6()

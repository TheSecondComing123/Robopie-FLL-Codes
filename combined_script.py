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


# --- artificial_habitat.py ---
def run4c():
    #Artificial Habitat
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


# --- collect_krill.py ---
def run4a(): 
    #Collects the krill 
    forward(270) 
    turn(90, 180) 
    forward(280, 270) 
    turn(-20, 180) 
    forward(164, 180) 
    turn(-50, 180) 
    forward(200 , 180) 
    turn(-75, 180) 
    forward(185, 170) 
    forward(-150, 150)


# --- feed_whale.py ---
def run4a2():
    #Working version as of 1/18/2025
    #next to one left of right corner
    #dumps the krill in the whale
    forward(270)
    turn(90, 180)
    forward(280, 270)
    turn(-20, 180)
    forward(164, 180)
    turn(-50, 180)
    forward(200 , 180)
    turn(-90, 180)
    forward(500, 160)
    forward(-150, 150)
    #Back to home base
    forward(-220, 190)
    turn(90, 100)
    forward(-840, 200)


# --- get_hoop.py ---
def run4b():
    forward(-100, 180)
    turn(-20, 180)
    forward(225, 180)
    forward(-180)
    turn(150, 180)
    turn(-30)
    forward(-750, 180)

    # Back to home base
    turn(90, 100)
    forward(-840, 180)


# --- krakens_treasure.py ---
def krakens_treasure():
    #Version 1/18/2025
    #Aligner four spaces right of corner
    forward(100)
    turn(-80)
    forward(225)
    turn(70)
    forward(335)
    turn(-141)
    forward(350)
    time.sleep(1)
    forward(-250,120)
    turn(80)
    forward(-200)
    turn(20)
    forward(-500)


# --- run5.py ---
#Sonar discovery and send the submersible!
#Version 1/11/2025
#Currently unfinished
def run5():
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


# --- run_1.py ---
def unexpected_encouter1a(): # 1/18/2025
    # One to the left of right corner
    reset_lift_arm_port()
    forward(150)
    turn(395)
    forward(-720)

def changing_shipping_lanes1b(): # 1/18/2025
    forward(200)
    time.sleep(1)
    turn(150)
    forward(-50)
    motor.run_for_degrees(lift_arm_port, -360, 380)
    time.sleep(0.5)
    forward(175)
    motor.run_for_degrees(lift_arm_port, 160, 380)
    time.sleep(0.5)
    turn(-105,200)
    motor.run_for_degrees(lift_arm_port, 50, 380)
    turn(-10,2200)
    turn(-50,2200)
    forward(-60)
    turn(-50)
    forward(500)


# --- run_6.py ---
def run6(): # 1/18/2025
    # Aligner two spaces right of corner
    reset_lift_arm_port()
    forward(150)
    turn(-70)
    forward(170)
    turn(45)
    forward(620)
    turn(105)
    forward(65)
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
    turn(-55)
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
    forward(220)
    run_lift_arm(-305, 660)
    turn(-60)
    forward(200)
    turn(-150)
    #Back to home base
    forward(-100)
    reset_lift_arm_port()
    turn(-125)
    forward(450)
    turn(70)
    forward(900)


# --- unspecified_run.py ---
def run4c2():
    #Not known in this time situation.
    forward(40)
    turn(60)
    forward(200)
    turn(90)
    forward(290)
    turn(60)


# Call all functions in file order
run4c()
run4a()
run4a2()
run4b()
krakens_treasure()
run5()
unexpected_encouter1a()
changing_shipping_lanes1b()
run6()
run4c2()

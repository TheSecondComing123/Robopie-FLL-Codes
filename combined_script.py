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
def artificialhabitat():
   # TODO: write transition from run1b() into right home base
   reset_lift_arm_port()
   forward(216)
   turn(160)
   motor.run_for_degrees(lift_arm_port, -360, 380)
   time.sleep(0.2)
   forward(360)
   turn(35)
   forward(108)
   turn(-90, 1660)
   forward(90)
   turn(50)
   forward(72)
   motor.run_for_degrees(lift_arm_port, 180, 390)
   forward(144)
   # motor.run_for_degrees(lift_arm_port, 180, 390)
   # forward(0.4)
   # forward(-0.5)
   # motor.run_for_degrees(lift_arm_port, -120, 360)
   # time.sleep(0.5)
   # forward(1)
   # forward(-0.75)
   # turn(-30)


# --- feed_whale.py ---
def feed_whale():
    forward(270)
    turn(90, 180)
    forward(360, 270)
    turn(-30, 180)
    forward(200, 180)
    turn(-70, 180)
    forward(230, 180)
    turn(-80, 180)
    forward(200, 180)
    forward(-90, 180)


# --- krakens_treasure.py ---
def krakens_treasure():
    #Aligner four spaces right of corner
    forward(100)
    turn(-80)
    forward(200)
    turn(70)
    forward(335)
    turn(-141)
    forward(305)
    time.sleep(1)
    forward(-250,120)


# --- run5.py ---
#Sonar discovery and send the submersible!
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
def unexpected_encouter1a(): # 1/5/2025
    # Two to the left
    forward(200)
    turn(395)
    forward(-720)

def changing_shipping_lanes1b(): # 1/5/2025
    # forward(-360)
    # turn(-100)
    # motor.run_for_degrees(lift_arm_port, -360, 360)
    # time.sleep(360)
    # forward(198)
    # motor.run_for_degrees(lift_arm_port, 360, 360)
    # time.sleep(0.5)
    # turn(-100)
    # forward(-180)
    # motor.run_for_degrees(lift_arm_port, 360, 360)
    forward(200)
    time.sleep(1)
    turn(165)
    forward(-50)
    motor.run_for_degrees(lift_arm_port, -360, 380)
    time.sleep(0.5)
    forward(160)
    motor.run_for_degrees(lift_arm_port, 135, 380)
    time.sleep(0.5)
    turn(-105,200)
    motor.run_for_degrees(lift_arm_port, 50, 380)
    turn(-10,2200)
    turn(-50,2200)
    forward(-60)
    turn(-50)
    forward(500)


# --- run_4.py ---

def run4a():
    #Collects the krill + dumps the krill in the whale
    forward(270)
    turn(90, 180)
    forward(360, 270)
    turn(-30, 180)
    forward(160, 180)
    turn(-60, 180)
    forward(175 , 180)
    turn(-75, 180)
    forward(185, 170)
    forward(-150, 150)

def run4b():
    #Get hoop while comes back
    forward(-100, 180)
    turn(-20, 180)
    forward(165, 180)
    forward(-180)
    turn(100, 180)
    forward(-750, 180)
    turn(45, 180)
    forward(-130, 205)

    # Back to home base
    turn(90, 100)
    forward(-840, 180)

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

def run4c2():
    #Not known in this time situation.
    forward(40)
    turn(60)
    forward(200)
    turn(90)
    forward(290)
    turn(60)


# --- run_6.py ---
def run6(): # 1/4/2025
    # Aligner two spaces right of corner
    reset_lift_arm_port()
    forward(150)
    turn(-70)
    forward(170)
    turn(45)
    forward(620)
    turn(100)
    forward(70)
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
    forward(-250)
    turn(-90)
    forward(100)
    turn(-75)
    forward(300)
    turn(60)
    forward(840)


# Call all functions in file order
artificialhabitat()
feed_whale()
krakens_treasure()
run5()
unexpected_encouter1a()
changing_shipping_lanes1b()
run4a()
run4b()
run4c()
run4c2()
run6()

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

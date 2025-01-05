def run1a():
    # Octopus, one left of right corner of right base
    reset_lift_arm_port()
    forward(200)
    turn(395)
    forward(-720)
    turn(85)
    forward(-100)

def run1b():
    # Change Shipping Lane
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

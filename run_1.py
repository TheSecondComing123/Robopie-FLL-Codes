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

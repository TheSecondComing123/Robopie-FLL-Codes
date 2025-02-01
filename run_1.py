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

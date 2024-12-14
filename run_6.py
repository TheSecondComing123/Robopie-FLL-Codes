def run_6():
    #Aligner two spaces right of corner
    run_lift_arm(300)
    forward(150)
    turn(-70)
    forward(170)
    turn(45)
    forward(620)
    turn(115)
    forward(55)
    #Shark
    run_lift_arm(-320, 1660)
    run_lift_arm(250)
    forward(-150)
    turn(-238)
    #Coral Nursery
    forward(-200)
    run_lift_arm(-100)
    turn(130)
    forward(210)
    turn(-60)
    #Coral Habitat
    run_lift_arm(-300, 660)
    forward(25)
    run_lift_arm(-25, 660)
    forward(-60)
    #Angler Fish
    run_lift_arm(290)
    turn(-90)
    forward(500)
    run_lift_arm(-305, 660)
    turn(75)
    forward(175)
    turn(-230)


run_6()

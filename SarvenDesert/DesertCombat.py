# while-loops repeat until the condition is false.

ordersGiven = 0
while ordersGiven < 5:
    # Move down 10 meters.
    PosX = hero.pos.x
    PosY = hero.pos.y
    hero.moveXY(PosX, PosY - 10)
    if ordersGiven == 2:
        hero.moveXY(PosX - 3, PosY - 10)
    elif ordersGiven > 2:
        hero.moveXY(PosX - 2, PosY - 10)
    elif ordersGiven >= 4:
        hero.moveXY(PosX, PosY - 10)
    # Order your ally to "Attack!" with hero.say
    # They can only hear you if you are on the X.
    hero.say("Attack!")
    hero.say(ordersGiven)


    # Be sure to increment ordersGiven!
    ordersGiven += 1
    if ordersGiven >= 5:
        break
    

    
while True:
    enemy = hero.findNearestEnemy()
    # When you're done giving orders, join the attack.
    if ordersGiven == 5:
        if enemy:
            hero.bash(enemy)
            hero.shield()
            hero.attack(enemy)
        

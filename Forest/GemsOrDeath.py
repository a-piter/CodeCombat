# If-statement code only runs when the if’s condition is true.
# Fix all the if-statements to beat the level.

# == means "is equal to".
if 1 + 1 == 3:  # ∆ Make this false.
    hero.moveXY(5, 15)  # Move to the first mines.

if 2 + 3 == 5:  # ∆ Make this true.
	hero.moveXY(15, 40)  # Move to the first gem.

# != means "is not equal to".
if 2 + 1 != 4:  # ∆ Make this true.
	hero.moveXY(25, 15)  # Move to the second gem.
	
# < means "is less than".
if 2 + 0 < 3:  # ∆ Make this true.
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)

if 5 < 4:  # ∆ Make this false.
	hero.moveXY(40, 55)

if 1 + 3 == 2: # ∆ Make this false.
    hero.moveXY(50, 10)

if 1 + 3 == 4:  # ∆ Make this true.
	hero.moveXY(55, 25)

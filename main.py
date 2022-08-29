#!/usr/bin/env python3 

# enemy below - codename sector clone in python for fun

import random
from movement import move_object


# GAME BOARD
# initially, this is going to be a 10x10 board, but future version
# will have option to change board size. Right now the movement
# lib is just written to handle a pre-determined board size. 

#initial submarine position
sub_position = random.randrange(2,99,1)

#initial destroyer position
destroyer_position = random.randrange(3,100,1)

# make sure the two ships don't start on top of each other 
if sub_position == destroyer_position:
	# change the sub position
	sub_position = random.randrange(sub_position, 99, 1)

# start the game !
while True: 
		print(
		'''
		Captain! A submarine has been spotted in the area. 
		To hunt, follow the game prompts to enter the new
		speed and direction you want to go. You can go any
		direction (N,S,E,W) and (NE,SE,NW,SW) and your
		speed is variable between 1 - 9 knots. A knot is 
		a grid-square reference. For instance, if you're 
		on grid square reference 54, setting your direction
		WEST at 4 knots will put you at grid square reference
		50. Each time you move, the enemy sub will move 1 space
		in any direction. Your job is to get within 2 grid
		squares from the sub and fire. Good luck!

		Now, let's get some bearings...

		...<<PING>>...
		The enemy submarine is currently at grid square reference
		''', sub_position)

		print("Captain, our current position is ", destroyer_position)
		print("Now we need to input our new course to chase the enemy!")
		
		new_direction = input("Captain, what direction should we head? ") 
		new_speed = int(input("What speed, captain ? 1 - 9 knots: "))

		# move the destroyer to intercept!
		destroyer_position = move_object(destroyer_position, new_speed, new_direction)
		
		# move submarine 1 spot in any direction - for now... south... 
		sub_position = move_object(sub_position, 1, "S")

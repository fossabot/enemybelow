def move_object(position, speed, direction):

	# move_object: this gets current position of each ship (both destroyers and sub)
	# and validates boundaries before moving the ship to the corresponding 
	# position based on user input in the game.

	#NORTH
	if direction == "N":
		# verify we're not too far north already
		while (position < 11):
			direction = input("You can't navigate any further NORTH. ")

		while speed > 0:
			position -= 10
			speed -=1
			
	#NORTHEAST
	if direction == "NE":
		while speed > 0:
			position -= 9
			speed -= 1

	#NORTHWEST
	if direction == "NW":
		while speed > 0:
			position -= 11
			speed -= 1

	#SOUTH
	if direction == "S":
		while (position > 90):
			direction = input("You can't navigate any further SOUTH. ")

		while speed > 0:
			position += 10
			speed -= 1

	#SOUTHEAST
	if direction == "SE":
		while speed > 0:
			position += 11
			speed -= 1

	#SOUTHWEST
	if direction == "SW":
		while speed > 0:
			position += 9
			speed -= 1

	#EAST
	if direction == "E":
		while position % 10 == 0:
			direction = input("You can't navigate any further EAST. ")

		while speed > 0:
			position += 1
			speed -= 1

	#WEST
	
	if direction == "W": 
		# west boundaries  are 1,11,21,31,41,51...and we don't want them to hit them
		west_boundary = [1,11,21,31,41,51,61,71,81,91]
		
		for w in west_boundary:
			if position == w:
				direction = input("You can't navigate any further WEST. ")

	while speed > 0:
		position -= 1
		speed -= 1

		
	return position



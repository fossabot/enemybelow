def diagonal(position, speed, direction):


	# start and end points of the board
	# this will allow the board to later be
	# increased in size 

	# TOP and BOT are constants in the main program file

	# manage movement / direction

	#NORTH
	if direction == "N":
		# verify we're not too far north already
		if (position < 11):
			direction = input("You can't navigate any further NORTH. ")

		while speed > 0:
			position -= 10
			speed -=1
		# we now have the new NORTH position. Let's make sure it's not a 
		# number off the map (i.e. less than ZERO)
		if position < TOP:
			diff = TOP - position
			position += diff 
			
	#NORTHEAST
	if direction == "NE":
		while speed > 0:
			position -= 9
			speed -= 1

	elif direction == "NW":
		while speed > 0:
			position -= 11
			speed -= 1
	
	elif direction == "SE":
		while speed > 0:
			position += 11
			speed -= 1

	elif direction == "SW":
		while speed > 0:
			position += 9
			speed -= 1

	
	return position

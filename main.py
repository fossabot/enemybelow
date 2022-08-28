#!/usr/bin/env python3 

# enemy below - codename sector clone in python for fun

import random

# GAME BOARD
TOP=10
BOT=90

# used to get the current pos and plot a new position based on user input
def check_bearing(pos,course,speed):


	## NORTH MOVEMENT ##
	if course == "N":
    	# if they're at the top of the map already
		while pos < TOP:
			course = input("You can't go any further NORTH: ")
	
		new_pos = pos - speed
		
	## SOUTH MOVEMENT ##
	elif course == "S":
		while pos > BOT:
       		# if they're at the bottom of the map already
			course = input("You can't go any further SOUTH: ")
		new_pos = pos + speed
	
	## EAST MOVEMENT ##
	elif course == "E":
		while pos % 10 == 0: 
			course = input("You can't go any further EAST")

			if pos < 11:
				row = 1
				row_end = 10
			elif (pos < 21) and (pos > 10):
				row = 2
				row_end = 20
			elif (pos < 31) and (pos > 20):
				row = 3
				row_end = 30
			elif (pos < 41) and (pos > 30):
				row = 4
				row_end = 40
			elif (pos < 51) and (pos > 40):
				row = 5
				row_end = 50
			elif (pos < 61) and (pos > 50):
				row = 6
				row_end = 60
			elif (pos < 71) and (pos > 60):
				row = 7
				row_end = 70
			elif (pos < 81) and (pos > 70):
				row = 8
				row_end = 80
			elif (pos < 91) and (pos > 80):
				row = 9
				row_end = 90
			elif pos >= 91:
				row = 10
				row_end = 100

			if row_end - pos > speed:
					new_pos = row_end
                   
          
	return new_pos



# when I move the sub moves, but sub can only move 1 space at a time
# I can move up to 9

my_pos = random.randrange(1,100,1)
sub_pos = random.randrange(2, 100,3 )
#my_new_pos = check_bearing(44,"S", 3)

new_dir = input("Compass direction ? (NSEW): ")
new_speed = int(input("Speed (1-9): "))
my_new_pos = check_bearing(my_pos,new_dir,new_speed)


if my_pos == sub_pos:
	sub_pos = random.randrange(sub_pos, 20, 3)

# print("Sub position ",sub_pos, "my position ",my_pos)

# get range to target
if (sub_pos > my_pos):
	sub_range = sub_pos - my_pos
elif (my_pos > sub_pos):
	sub_range = my_pos - sub_pos


# debug - remove when ready to play
print("Current position: ", my_pos)
print("Range to Target: ", sub_range)
print("New position: ", my_new_pos)

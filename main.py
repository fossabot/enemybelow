#!/usr/bin/env python3 

# enemy below - codename sector clone in python for fun

import random



###### SUBROUTINES ################################
# 
#
###################################################
#
#
# gotta be able to move the ships
# 

TOP=11
BOT=90
	
# move the ships around with this function.

def check_bearings(pos,course,speed):

	## NORTH MOVEMENT ##
	if course == "N":
		# if they're at the top of the map already
		while pos < TOP:
			print("You can't go any further NORTH.")
		


# def fire_on_sub()


def move_ship():

	# movement is based on current position (pos), heading (course) and (speed)


	####################
	## NORTH MOVEMENT ##
	####################

	# get their selected speed and heading, check against current position,
	# and move the ship.

	
	
	



# when I move the sub moves, but sub can only move 1 space at a time
# I can move up to 9

my_pos = random.randrange(1,20,1)
sub_pos = random.randrange(2, 20,3 )


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


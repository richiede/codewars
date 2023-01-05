# 7 Wonders
# 7 Wonders is a board game that consists of building your city, gathering resources and fighting your neighbors.
# One part of the game is also to research science in order to gain points at the end of the game. There are 3 types of science glyps you can gather:
# Compasses
# Gears
# Tablets
# The way points are added up works as described here:

# Step 1
# Each distinct set of three different glyphs is worth 7 points.
# 1 Compass, 1 Gear and 1 Tablet is 7 points.
# 2 Compasses, 1 Gear and 1 Tablet is still 7 points.
# Note that a distinct set of three different glyphs means 1 Compass, 1 Gear and 1 Tablet. No more, no less!

# Step 2
# The amount of each glyph you own is squared and then summed up.
# 1 Compass, 1 Gear and 1 Tablet is 3 points.
# 2 Compasses, 1 Gear and 1 Tablet is 6 points.

# Finally
# The total science points is equal to the sum of the two steps.
# 1 Compass, 1 Gear and 1 Tablet is finally 10 points.
# 2 Compasses, 1 Gear and 1 Tablet is finally 13 points.
# You will be given 3 inputs corresponding to the amount of each glyph you have acquired in the game. Your task is to output the final score. Take into account that you may have no glyphs at all!

# test.assert_equals(seven_wonders_science(0, 0, 0), 0)
# test.assert_equals(seven_wonders_science(1, 1, 1), 10)
# test.assert_equals(seven_wonders_science(2, 1, 1), 13)
# test.assert_equals(seven_wonders_science(4, 2, 2), 38)
# test.assert_equals( seven_wonders_science(7, 2, 2), 71)

def seven_wonders_science(compasses, gears, tablets):
	talley_list = sorted([compasses, gears, tablets])
	if 0 in talley_list:
	    dis_score = 0
	else:
	    dis_score = talley_list[0] * 7
	score = sum([x**2 for x in talley_list])
	final_score = dis_score + score
	return(final_score)

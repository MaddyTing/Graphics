# Grass
Rect(0, 0, 400, 400, fill='forestGreen')

# These Lines draw a fine soccer field but the autograder wants a Rect
### Fix Your Code Here ###
Rect(50, 100, 300, 200, fill=None, border='white')

# make the penalty box
Circle(85, 200, 25, fill=None, border='white')
Circle(315, 200, 25, fill=None, border='white')
Rect(50, 150, 50, 100, fill='forestGreen', border='white')
Rect(300, 150, 50, 100, fill='forestGreen', border='white')

# draw center field
Line(200, 100, 200, 300, fill='white')
Circle(200, 200, 25, fill=None, border='white')

# draw the goals
Rect(40, 180, 20, 40, fill='white')
Rect(340, 180, 20, 40, fill='white')

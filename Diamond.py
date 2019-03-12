# Create a sparkling diamond! It should be created using two Polygons,
# three Lines, and a Star to make it sparkle.

# draws a background
Rect(0, 0, 400, 400, fill=gradient('powderBlue', 'lightCyan', start='top'))

# Create the outer shape of the diamond using one Polygon.
### Place Your Code Here ###
Polygon(100, 100, 60, 150, 200, 300, 340, 150, 300, 100, fill=gradient('white', 'lightBlue'), border='black', borderWidth=4)

# Create the brighter inner part of the diamond using a Polygon.
### Place Your Code Here ###
Polygon(200, 100, 125, 150, 200, 300, 275, 150, fill='azure', border='black', borderWidth=2)

# Create the cut Lines.
### Place Your Code Here ###
Line(60, 150, 340, 150)
Line(300, 100, 275, 150)
Line(100, 100, 125, 150)

# Finish by adding a sparkle to the diamond!
### Place Your Code Here ###
Star(265, 120, 15, 6, roundness=15, fill='white')

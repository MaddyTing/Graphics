# The solution canvas contains the logos for four popular tech companies. You
# should draw each of them one by one.
# Four images at once, wow!

# Instagram
### Place Your Code Here ###
Rect(20, 20, 160, 160, fill=None, border=gradient('darkorchid', 'red', 'orange', start='right-top'), borderWidth=15)
Circle(100, 100, 40, fill=None, border=gradient('darkorchid', 'orange', start='right-top'), borderWidth=15)
Circle(150, 50, 10, fill='darkorchid')

# YouTube
### Place Your Code Here ###
Rect(205, 40, 185, 120, fill='red')
Polygon(270, 70, 270, 130, 330, 100, fill='white')

# Microsoft
### Place Your Code Here ###
x = 85

Rect(15, 210, x, x, fill=rgb(246, 83, 20))
Rect(110, 210, x, x, fill=rgb(124, 187, 0))
Rect(15, 305, x, x, fill=rgb(0, 161, 241))
Rect(110, 305, x, x, fill=rgb(255, 187, 0))

# Uber
### (HINT: Use a line to connect the outer and inner black sections through the
# circle!)
### Place Your Code Here ###
Rect(210, 210, 180, 180)
Circle(300, 300, 70, fill='white')
Rect(275, 275, 50, 50)
Line(210, 300, 300, 300, lineWidth=10)
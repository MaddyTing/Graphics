# Background
Rect(0, 0, 400, 400, fill=gradient('powderBlue', 'lightCyan', start='top'))

# Outer Shape
Polygon(100, 100, 60, 150, 200, 300, 340, 150, 300, 100, fill=gradient('white', 'lightBlue'), border='black', borderWidth=4)

# Inner Shape
Polygon(200, 100, 125, 150, 200, 300, 275, 150, fill='azure', border='black', borderWidth=2)

# Cut Lines
Line(60, 150, 340, 150)
Line(300, 100, 275, 150)
Line(100, 100, 125, 150)

# Sparkle
Star(265, 120, 15, 6, roundness=15, fill='white')

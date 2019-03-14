# Pixar's Mike Wazowski from Monster's Inc

# Background
Rect(0, 0, 400, 400, fill='crimson')
Line(0, 200, 400, 200, fill='darkRed', opacity=20, lineWidth=400, dashes=(5, 75))

# Horns
Polygon(135, 90, 130, 125, 150, 105, fill=gradient('whiteSmoke', 'khaki', start='top'))
Polygon(265, 90, 270, 125, 250, 105, fill=gradient('whiteSmoke', 'khaki', start='top'))

# Arms
Line(112, 240, 105, 265, lineWidth=8, fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
Line(293, 225, 290, 310, lineWidth=8, fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
Line(106, 260, 110, 310, lineWidth=8, fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
Line(110, 300, 120, 310, fill=gradient('mediumSeaGreen', 'greenYellow', start='left'), lineWidth=8)
Oval(110, 310, 15, 25, fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
Line(290, 300, 280, 310, fill=gradient('mediumSeaGreen', 'greenYellow', start='left'), lineWidth=8)
Oval(290, 310, 15, 25, fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))

# Legs
Line(170, 300, 170, 360, fill=gradient('mediumSeaGreen', 'greenYellow', start='left'), lineWidth=15)
Line(230, 300, 230, 360, fill=gradient('mediumSeaGreen', 'greenYellow', start='left'), lineWidth=15)
Oval(200, 333, 55, 110, fill='crimson')
Oval(170, 360, 30, 20, fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
Oval(230, 360, 30, 20, fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))

# Main Body
Oval(200, 200, 200, 220, fill=gradient('greenYellow', 'greenYellow', 'mediumSeaGreen'))

# Smile
Circle(155, 233, 10, fill='darkGreen')
Circle(155, 235, 10, fill='greenYellow')
Circle(245, 233, 10, fill='darkGreen')
Circle(245, 235, 10, fill='greenYellow')

Oval(200, 232, 100, 50, fill='darkGreen')
Oval(200, 230, 100, 50, fill='greenYellow')

# Eye
Circle(200, 160, 50, fill='white')
Circle(200, 160, 25, fill=gradient('mediumSeaGreen', 'seaGreen'))
Star(200, 160, 25, 25, roundness=50, fill=gradient('springGreen', 'mediumSeaGreen'))
Circle(200, 160, 15)
Circle(190, 150, 5, fill='white')
Circle(180, 150, 2, fill='white')

#Sky
Rect(0, 0, 400, 400)
Rect(0, 0, 400, 400, fill=gradient('cadetblue', 'blue', 'navy', start='bottom'), opacity=50)

#Stars
Star(50, 100, 5, 5, fill='white')
Star(200, 20, 6, 5, fill='white')
Star(350, 17, 3, 5, fill='white')
Star(380, 145, 5, 5, fill='white')
Star(300, 75, 8, 5, fill='white')
Star(161, 86, 5, 5, fill='white')
Star(82, 150, 5, 5, fill='white')
Star(28, 178, 7, 5, fill='white')
Star(317, 180, 6, 5, fill='white')
Star(386, 217, 5, 5, fill='white')
Star(321, 117, 4, 5, fill='white')
Star(225, 58, 5, 5, fill='white')
Star(74, 230, 3, 5, fill='white')
Star(376, 56, 5, 5, fill='white')
Star(270, 14, 5, 5, fill='white')

#Big Dipper
Star(30, 30, 5, 5, fill='white')
Star(82, 66, 5, 5, fill='white')
Star(121, 16, 5, 5, fill='white')
Star(46, 65, 5, 5, fill='white')
Star(101, 40, 5, 5, fill='white')
Star(151, 7, 5, 5, fill='white')

Line(121, 16, 151, 7, fill='white')
Line(121, 16, 82, 66, fill='white')
Line(46, 65, 82, 66, fill='white')
Line(30, 30, 46, 65, fill='white')
Line(30, 30, 101, 40, fill='white')

#Moon
Circle(200, 200, 100, fill=gradient('darkgray', 'gray'), border='black', borderWidth=1)
Circle(253, 217, 20, fill=gradient('white', 'lightgray', 'gray'))
Circle(158, 231, 30, fill=gradient('white', 'lightgray', 'gray'))
Circle(210, 132, 20, fill=gradient('white', 'lightgray', 'gray'))

#Mountains
Polygon(0, 200, 8, 222, 26, 215, 48, 233, 83, 261, 100, 254, 118, 266, 134, 251, 165, 262, 267, 273, 281, 264, 295, 261, 304, 244, 322, 241, 333, 228, 338, 232, 355, 225, 380, 253, 400, 255, 400, 400, 0, 400, fill='darkgreen')
Polygon(0, 200, 8, 222, 26, 215, 48, 233, 83, 261, 100, 254, 118, 266, 134, 251, 165, 262, 267, 273, 281, 264, 295, 261, 304, 244, 322, 241, 333, 228, 338, 232, 355, 225, 380, 253, 400, 255, 400, 400, 0, 400, fill=gradient('teal', 'green', 'seaGreen', start='top'), opacity=90)

#Bottom Legs
Oval(175, 380, 35, 50)
Oval(225, 380, 35, 50)

#Body
Oval(200, 300, 150, 160, fill='white')

#Words
Rect(30, 315, 340, 65, fill=rgb(30, 60, 90))
Label('Sweet dreams!', 200, 350, size=40, fill='lightblue', bold=True)

#Top Legs
Oval(150, 300, 35, 50)
Oval(250, 300, 35, 50)

#Ears
Circle(160, 160, 25)
Circle(240, 160, 25)

#Face
Circle(200, 200, 50, fill='white')

#Spots on Face
Polygon(177, 180, 165, 189, 163, 203, 172, 216, 182, 215, 193, 213, 197, 183)
Polygon(224, 180, 236, 189, 238, 203, 226, 216, 219, 215, 206, 213, 204, 183)

#Eyes
Circle(180, 200, 10, fill='white')
Circle(220, 200, 10, fill='white')
Circle(180, 200, 9)
Circle(220, 200, 9)
Star(220, 200, 8, 10, fill=rgb(50, 50, 60))
Star(180, 200, 8, 10, fill=rgb(50, 50, 60))

#Highlight in Eyes
Circle(185, 195, 3, fill='white')
Circle(225, 195, 3, fill='white')

#Nose
RegularPolygon(200, 210, 3, 3)

Circle(200, 221, 6)
Circle(200, 220, 6, fill='white')

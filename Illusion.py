# Illusion
x = 100
Line(0, 0, 100, 200)
Line(x, 200, 200, 400, fill='red')
Line(x, 185, 200, 385, fill='blue')
Rect(85, 0, 30, 400, fill='grey')

# Illusion Revealed
x = 300
Line(200, 0, x, 200)
Line(x, 200, 400, 400, fill='red')
Line(x, 185, 400, 385, fill='blue')
Rect(285, 0, 30, 400, fill='grey', opacity=50)

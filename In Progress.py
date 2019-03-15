# In this exercise, you'll draw The Aurora Borealis, also known as the Northern Lights


Rect(0, 0, 400, 400, fill=gradient('navy', 'darkCyan', start='top'))
Line(0, 400, 400, 0, fill='white', lineWidth=600, dashes=(1, 30))
Line(0, 200, 400, 200, fill=gradient('navy', 'darkCyan', start='top'), lineWidth=400, dashes=(25, 1))

Rect(0, 0, 400, 300, fill=gradient('whiteSmoke', 'darkMagenta', 'chartreuse', 'lightCyan', 'darkMagenta', 'royalBlue', start='right-bottom'), opacity=40)
Rect(0, 0, 400, 300, fill=gradient('black', 'darkCyan', start='top'), opacity=50)


#Mountains
Rect(0, 300, 400, 100, fill=gradient('black', 'midnightBlue', 'darkBlue', start='bottom'))

Polygon(400, 150, 395, 170, 380, 158, 343, 198, 305, 228, 279, 245, 265, 265, 244, 270, 220, 260, 189, 271, 178, 280, 157, 282, 140, 269, 126, 258, 116, 277, 96, 290, 74, 283, 59, 268, 39, 284, 24, 281, 0, 290, 0, 300, 0, 400, 400, 400, fill='black', opacity=50)
Polygon(400, 400, 376, 392, 354, 390, 344, 385, 313, 383, 295, 380, 262, 381, 243, 381, 229, 375, 211, 363, 199, 372, 185, 375, 118, 375, 93, 361, 82, 347, 60, 330, 55, 320, 70, 325, 92, 330, 127, 324, 159, 319, 210, 324, 246, 315, 280, 303, 304, 300, 325, 304, 342, 310, 359, 310, 386, 304, 400, 300, 400, 200, fill=gradient('black', 'midnightBlue', 'darkBlue', start='right'), opacity=50)

Polygon(400, 400, 376, 392, 354, 390, 344, 385, 313, 383, 295, 380, 262, 381, 243, 381, 229, 375, 211, 363, 199, 372, 185, 375, 118, 375, 93, 361, 82, 347, 60, 330, 55, 320, 70, 325, 92, 330, 127, 324, 159, 319, 210, 324, 246, 315, 280, 303, 304, 300, 325, 304, 342, 310, 359, 310, 386, 304, 400, 300, 400, 200, fill='midnightBlue', opacity=20)

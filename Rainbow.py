# Sky
Rect(0, 0, 400, 400, fill='lightSkyBlue')

# Rainbow
x = 200
y = 300
z = 200

Circle(x, y, z, fill=gradient('white', 'red', 'white', start='top'))
z = z - 30

Circle(x, y, z, fill=gradient('white', 'orange', 'white', start='top'))
z = z - 30

Circle(x, y, z, fill=gradient('white', 'yellow', 'white', start='top'))
z = z - 30

Circle(x, y, z, fill=gradient('white', 'green', 'white', start='top'))
z = z - 30

Circle(x, y, z, fill=gradient('white', 'blue', 'white', start='top'))
z = z - 30

Circle(x, y, z, fill=gradient('white', 'indigo', 'white', start='top'))
z = z - 30

Circle(x, y, z, fill=gradient('white', 'violet', 'white', start='top'))

#Grass
Rect(0, 300, 400, 100, fill=gradient('limeGreen', 'forestGreen', start='top') )

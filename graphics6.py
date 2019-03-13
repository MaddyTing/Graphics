# In this exercise, we look at an interesting optical illusion! Which Line is
# a continuation of the black one - the blue or the red Line? If you guess that
# it's the blue Line then you are wrong!
# Have fun!

# First, draw the actual illusion
### Place Your Code Here ###
x = 100
Line(0, 0, 100, 200)
Line(x, 200, 200, 400, fill='red')
Line(x, 185, 200, 385, fill='blue')
Rect(85, 0, 30, 400, fill='grey')

# Now, draw a repeat of the illusion, but making the rectangle partly
# transparent, so we can see what's really going on underneath.
### Place Your Code Here ###
x = 300
Line(200, 0, x, 200)
Line(x, 200, 400, 400, fill='red')
Line(x, 185, 400, 385, fill='blue')
Rect(285, 0, 30, 400, fill='grey', opacity=50)
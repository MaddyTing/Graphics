# Draw the solution.

x = 25
y = 150
z = 275

### Modify Your Code Here ###
Rect(x, x, 100, 100, fill=gradient('red', 'yellow', start='left-top'))
Rect(y, x, 100, 100, fill=gradient('red', 'yellow', start='top'))
Rect(z, x, 100, 100, fill=gradient('red', 'yellow', start='right-top'))

# Here is the first of the three rectangles in the middle row.
### Modify & Place Your Code Here ###
Rect(x, y, 100, 100, fill=gradient('red', 'yellow', start='left'))
Rect(y, y, 100, 100, fill=gradient('red', 'yellow'))
Rect(z, y, 100, 100, fill=gradient('red', 'yellow', start='right'))


# Bottom Row
Rect(x, z, 100, 100, fill=gradient('red', 'yellow', start='left-bottom'))
Rect(y, z, 100, 100, fill=gradient('red', 'yellow', start='bottom'))
Rect(z, z, 100, 100, fill=gradient('red', 'yellow', start='right-bottom'))

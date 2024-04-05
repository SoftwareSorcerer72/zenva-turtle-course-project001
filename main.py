from turtle import *

# Start
# Begin fill
# Set fill color and fill to orange
# Draw circle 80px
# Pen up and forward 100px
# Pen down
# Set fill color and fill to grey
# Draw circle 20 px
# Pen up and forward 80px
# Pen down
# Set fill color and fill to red
# Draw circle 40 px
# Pen up and forward 90px
# Pen down
# Set fill color and fill to green
# Draw circle 30 px
# End

speed(0)

bgcolor("black")


# Create the ORANGE planet
color("orange")
begin_fill()
circle(80)
end_fill()

# Move Forwards
penup()
forward(100)
pendown()

# Create the GREY planet
color("grey")
begin_fill()
circle(20)
end_fill()

# Move Forwards
penup()
forward(80)
pendown()

# Create the RED planet
color("red")
begin_fill()
circle(40)
end_fill()

# Move Forwards
penup()
forward(90)
pendown()

# Create the GREEN planet
color("green")
begin_fill()
circle(30)
end_fill()

done()


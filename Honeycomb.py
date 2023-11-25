import turtle
import math
import random

turtle.title('HONEYCOMB')

turtle.setup(600, 600)
hexagon_sides = 6
hexangon_angle = 60
hexagon_radius = 20
hexagon_outline_width = 4
hexagon_outline_color = '#FCE795'
gap_between_hexagons = 4
hexagon_width = math.sqrt(3) * (hexagon_radius + gap_between_hexagons)
hexagon_height = 2 * (hexagon_radius + gap_between_hexagons)
hexagon_fill_colors = ['#FFF201', '#FFDA01', '#F18800']
honeycomb_rows = 10
honeycomb_columns = 10
background_color = '#1E1E1E'
origin_x = -230
origin_y = -150


def draw_hexagon(a, b, sidelenght, outlinewidth, outlinecolor, fillcolor):
    turtle.penup()
    turtle.goto(a, b)
    turtle.pendown()
    turtle.pensize(outlinewidth)
    turtle.color(outlinecolor)
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.setheading(-30)

    for i in range(hexagon_sides):
        turtle.forward(sidelenght)
        turtle.right(hexangon_angle)
    turtle.end_fill()


turtle.bgcolor(background_color)
turtle.speed('fastest')
turtle.hideturtle()

hexagonIndices = []

for row in range(honeycomb_rows):
    for column in range(honeycomb_columns):
        hexagonIndices.append((row, column))

# Shuffle the indices so the hexagon are drawn in a random order
random.shuffle(hexagonIndices)

for hexagonIndex in hexagonIndices:
    row, column = hexagonIndex
    shouldOffsetHexagon = (row % 2) == 0
    horizaontalOffset = hexagon_width / 2 if shouldOffsetHexagon else 0
    verticalOffset = 0.75 * hexagon_height
    x = origin_x + (column * hexagon_height) + horizaontalOffset
    y = origin_y + (row * verticalOffset)

    draw_hexagon(x, y, hexagon_radius, hexagon_outline_width, hexagon_outline_color, random.choice(hexagon_fill_colors))

turtle.done()

import turtle

SQUARE_LENGTH = 100

N_QUEENS = 8

X_ORIGIN = (N_QUEENS * SQUARE_LENGTH) // 2
Y_ORIGIN = (N_QUEENS * SQUARE_LENGTH) // 2 - SQUARE_LENGTH

def c(x, y):
    return x - X_ORIGIN, y - Y_ORIGIN

def teleport(x, y, heading=0):
    was_drawing = turtle.isdown()
    turtle.up()
    # teleport only available on python3.12+
    turtle.setposition(*c(x, y))
    turtle.setheading(heading)
    if was_drawing:
        turtle.down()

def tele_home():
    teleport(X_ORIGIN, Y_ORIGIN)

def square(x, y, side_length, fillcolor=None):
    teleport(x, y)
    if fillcolor is not None:
        turtle.fillcolor(fillcolor)
        turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    if fillcolor is not None:
        turtle.end_fill()

def turtle_init():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.tracer(n=10)

def _debug_turtle_init():
    # draw a cross at turtle origin, useful for debugging
    for _ in range(4):
        turtle.forward(30)
        turtle.back(30)
        turtle.right(90)

    turtle.hideturtle()
    turtle.speed(9)
    turtle.tracer(n=2)

def _debug_turtle_end():
    turtle.up()
    turtle.setposition(0,0)
    turtle.down()
    turtle.color((1,0,0))
    for _ in range(4):
        turtle.forward(30)
        turtle.back(30)
        turtle.right(90)


def draw_board(n=N_QUEENS):
    for x_i in range(n):
        for y_i in range(n):
            # draw the (i, j)-th square
            # move to the lower left corner of (i, j)-th square

            #_fillrgb = max(x_i, y_i) * (1/n)
            if (x_i % 2 + y_i % 2) % 2 == 1:
                _fillrgb = 0.8
            else:
                _fillrgb = 0.4
            fillcolor = (_fillrgb,)*3
            square(x_i * SQUARE_LENGTH, y_i * SQUARE_LENGTH, SQUARE_LENGTH, fillcolor)


def queen_sees(board_x, board_y):
    pass

def place_queen(board_x, board_y):
    # ...
    # x = board_x * SQUARE_LENGTH
    fillcolor = (0, 1, 0)
    square(board_x * SQUARE_LENGTH, board_y * SQUARE_LENGTH, SQUARE_LENGTH, fillcolor)

    # now I need to put the squares the queen sees...
    # to do so I need to know the dimensions of the board :(
    pass



def main():
    _debug_turtle_init()
    draw_board()
    place_queen(3, 5)
    _debug_turtle_end()
    turtle.done()


if __name__ == "__main__":
    main()

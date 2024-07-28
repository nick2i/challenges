import turtle
import pprint

SQUARE_LENGTH = 100

N_QUEENS = 8

X_ORIGIN = (N_QUEENS * SQUARE_LENGTH) // 2
Y_ORIGIN = (N_QUEENS * SQUARE_LENGTH) // 2 - SQUARE_LENGTH


#board_colors = [[(1, 1, 1)] * N_QUEENS] * N_QUEENS
board_colors = []
for _i in range(N_QUEENS):
    board_colors.append([])
    for _j in range(N_QUEENS):
        board_colors[_i].append((1,1,1))


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

def _color_alpha(color, alpha):
    return tuple(x * alpha for x in color)


def _color_combine(c1, a1, c2):
    # color 1, alpha 1, etc (a2 derived)
    assert 0 <= a1 <= 1
    a2 = 1 - a1
    return tuple(map(sum, zip(_color_alpha(c1, a1), _color_alpha(c2, a2))))


def color_square(x, y, color, opacity=0.2):
    assert 0 <= y < len(board_colors)
    assert 0 <= x < len(board_colors[0])
    assert 0 <= opacity <= 1

    '''
    prior_color = board_colors[y][x]
    prior_opacity = 1 - opacity
    prior_color_alphad = _color_alpha(prior_color, prior_opacity)

    new_color_alphad = _color_alpha(color, opacity)
    '''
    prior_color = board_colors[y][x]
    board_colors[y][x] = _color_combine(color, opacity, prior_color)



def render_board():
    for y, row in enumerate(board_colors):
        for x, cell in enumerate(row):
            # turtle uses 1 for white and 0 for black, this is mathematically annoying
            # so I am using 0 for white and 1 for black
            #color = map(lambda c_rgb: 1 - c_rgb, cell)

            # OR AM I?
            color = cell
            square(x * SQUARE_LENGTH, y * SQUARE_LENGTH, SQUARE_LENGTH, cell)

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
    q_color = (0, 1, 0)
    seen_color = (1, 0, 0)
    #square(board_x * SQUARE_LENGTH, board_y * SQUARE_LENGTH, SQUARE_LENGTH, fillcolor)
    color_square(board_x, board_y, q_color)

    diag1 = lambda x: (x - board_x) + board_y
    diag2 = lambda x: -(x - board_x) + board_y
    # now I need to put the squares the queen sees...
    # to do so I need to know the dimensions of the board :(
    for x in range(N_QUEENS):
        if x == board_x:
            # on the queen col, skiparooni
            continue
        y1 = diag1(x)
        y2 = diag2(x)

        if 0 <= y1 < N_QUEENS:
            color_square(x, y1, seen_color, opacity=0.7)
        if 0 <= y2 < N_QUEENS:
            color_square(x, y2, seen_color, opacity=0.7)

    debug_print()

    pass


_STEP = 0
def debug_print():
    global _STEP
    _STEP += 1
    print(f"STEP {_STEP}")
    pprint.pprint(board_colors)

def main():
    _debug_turtle_init()
    #draw_board()
    render_board()
    debug_print()

    place_queen(3, 5)
    render_board()
    place_queen(3, 6)
    debug_print()
    render_board()
    place_queen(1, 2)
    render_board()
    place_queen(7, 7)
    render_board()
    _debug_turtle_end()
    turtle.done()


if __name__ == "__main__":
    main()

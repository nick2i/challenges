
'''
image format is like:

[
    [ a, b, c, ... ], # y = 0
      ^ x = 0
    [ ... ], # y = 1
    ...
]

'''

def generate_ppm_canvas(width, height):
    canvas = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append((0, 0, 0))
        canvas.append(row)
    return canvas

class PPMImage:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = generate_ppm_canvas(width, height)

    def __getitem__(self, key):
        return self.canvas[key]

    def __setitem__(self, key, value):
        self.canvas[key] = value

    def __str__(self):
        output = ["P3"]
        output.append(f"{self.width} {self.height}")
        output.append("255")
        for row in self.canvas:
            for pixel in row:
                output.append(" ".join(map(str, pixel)))
        return "\n".join(output)


def color_point(image, point, color=(0,0,0)):
    x, y = point
    print(f"coloring point ({x}, {y})")
    image[y][x] = color

def translate(point, translation):
    return tuple(map(sum, zip(point, translation)))

def add_rect(image, corner0, corner1, thickness=1, color=(0,0,0)):
    x0, y0 = corner0
    x1, y1 = corner1

    print("coloring horizontal sides")
    for x in range(x0, x1 + 1):
        # fill in (x0, y0 + i) to (x1, y0 + i) for i in range(thickness)
        # fill in (x0, y1 - i) to (x1, y1 - i) for i in range(thickness)
        #color_point(image, (x0, y0 + i), color)
        #color_point(image, (x0, y0 - i), color)
        color_point(image, (x, y0), color)
        color_point(image, (x, y1), color)

    print("coloring vertical sides")
    for y in range(y0, y1 + 1):
        # fill in (x0 + i, y0) to (x0 + i, y1) for i in range(thickness)
        # fill in (x1 - i, y0) to (x1 - i, y1) for i in range(thickness)
        color_point(image, (x0, y), color)
        color_point(image, (x1, y), color)


def add_circle(image, center, radius, color=(0,0,0), thickness=1):
    cx, cy = center
    def _color_point(x, y):
        color_point(image, translate((x, y), (cx, cy)), color=color)

    def _color_symmetrical(x, y):
        _color_point(x, y)
        _color_point(x, -y)
        _color_point(-x, y)
        _color_point(-x, -y)
        _color_point(y, x)
        _color_point(y, -x)
        _color_point(-y, x)
        _color_point(-y, -x)
    
    # Jesko's method (of a simpler midpoint circle algm): https://schwarzers.com/algorithms/
    y = 0
    t1 = radius >> 4
    x = radius
    while x >= y:
        # color (x, y) and symmetrical pixels (around the center)
        _color_symmetrical(x, y)

        y += 1
        t1 += y
        t2 = t1 - x
        if t2 >= 0:
            t1 = t2
            x -= 1


def main():
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 255, 0)
    GREEN = (0, 0, 255)

    img = PPMImage(256, 256)

    add_rect(img, (10,10), (245,245), color=WHITE)
    add_rect(img, (11,11), (244,244), color=GREEN)
    for i in range(25):
        color = (255 - 3 * i, 255 - 3 * i, 255 - 3 * i)
        add_rect(img, (5 + i, 5 + i), (250 - i, 250 - i), color=color)

    for i in range(40):
        color = (int(255 - i**1.5), 0, 0)
        add_circle(img, (127, 127), 30 + i, color=color)
    #add_circle(img, (127, 127), 60, color=GREEN)
    #add_circle(img, (127, 127), 90, color=BLUE)

    #print("output:")
    #print(img)

    TEST_NUMBER = 5
    TEST_OUTPUT = f"test-{TEST_NUMBER:03}.ppm"
    with open(TEST_OUTPUT, "w") as f:
        f.write(str(img))

    print(f"Wrote result to {TEST_OUTPUT}")


if __name__ == "__main__":
    main()


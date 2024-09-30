
'''
image format is like:

[
    [ a, b, c, ... ], # y = 0
      ^ x = 0
    [ ... ], # y = 1
    ...
]

'''

def generate_ppm_canvas(width, height, fillcolor=(0, 0, 0)):
    canvas = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(fillcolor)
        canvas.append(row)
    return canvas

class PPMImage:
    def __init__(self, width, height, fillcolor=(0, 0, 0)):
        self.width = width
        self.height = height
        self.canvas = generate_ppm_canvas(width, height, fillcolor)

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
    #print(f"coloring point ({x}, {y}) to color: {color}")
    image[y][x] = color

def translate(point, translation):
    return tuple(map(sum, zip(point, translation)))

def add_rect(image, corner0, corner1, thickness=1, color=(0,0,0)):
    x0, y0 = corner0
    x1, y1 = corner1

    #print("coloring horizontal sides")
    for x in range(x0, x1 + 1):
        # fill in (x0, y0 + i) to (x1, y0 + i) for i in range(thickness)
        # fill in (x0, y1 - i) to (x1, y1 - i) for i in range(thickness)
        #color_point(image, (x0, y0 + i), color)
        #color_point(image, (x0, y0 - i), color)
        color_point(image, (x, y0), color)
        color_point(image, (x, y1), color)

    #print("coloring vertical sides")
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


def random_circles(img, n, r):
    import random
    img.width, img.height
    for i in range(n):
        radius = random.randint(0, r)
        x = random.randint(radius, img.width - radius - 1)
        y = random.randint(radius, img.height - radius - 1)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        add_circle(img, (x, y), radius, color=color)


def main():
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 255, 0)
    GREEN = (0, 0, 255)

    img_dim = 1024
    fillcolor = (0, 0, 0)
    img = PPMImage(img_dim, img_dim, fillcolor)

    for i in range(50):
        color = (255 - 3 * i, 255 - 3 * i, 255 - 3 * i)
        color = (150 - 3 * i, 150 - 3 * i, 100 + 3 * i)
        add_rect(img, (5 + i, 5 + i), (img_dim - 6 - i, img_dim - 6 - i), color=color)

    for i in range(45):
        color = (int(255 - i**1.5), 0, 0)
        color = tuple(map(lambda x: min(255, x), color))
        color = tuple(map(lambda x: max(0, x), color))

        add_circle(img, (img_dim//2, img_dim//2), img_dim//9 + i, color=color)
    for i in range(10):
        color = (0, 255, 0)
        add_circle(img, (img_dim//2, img_dim//2), img_dim//9 - i, color=color)

    #add_circle(img, (127, 127), 60, color=GREEN)
    #add_circle(img, (127, 127), 90, color=BLUE)
    random_circles(img, 2000, img_dim//4)

    #print("output:")
    #print(img)

    TEST_NUMBER = 10
    TEST_OUTPUT = f"test-{TEST_NUMBER:03}.ppm"
    with open(TEST_OUTPUT, "w") as f:
        f.write(str(img))

    print(f"Wrote result to {TEST_OUTPUT}")


if __name__ == "__main__":
    main()


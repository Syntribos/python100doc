from turtle import Turtle, Screen
import random
import colorgram


def dashed(turt, total_len, dash_len, gap_len=-1):
    pen_state = turt.pen()

    gap_len = dash_len if gap_len == -1 else gap_len
    period_len = dash_len + gap_len
    count = total_len // period_len
    rem_dash = total_len % period_len
    rem_gap = max(0, rem_dash - dash_len)
    rem_dash = min(rem_dash, dash_len)

    for _ in range(count):
        turt.pd()
        turt.fd(dash_len)
        turt.pu()
        turt.fd(gap_len)

    turt.pd()
    turt.fd(rem_dash)
    turt.pu()
    turt.fd(rem_gap)

    turt.pen(pen_state)


def rand_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def random_turn():
    return 90 * random.randint(0, 3)


def random_walk(turt):
    turt.pd()
    turt.pensize(10)
    while True:
        turt.right(random_turn())
        turt.pencolor(rand_colour())
        turt.fd(20)


def draw_shapes(turt):
    for sides in range(3, 10):
        turt.pencolor((rand_colour()))

        for _ in range(sides):
            turt.fd(100)
            turt.rt(360/sides)


def draw_spiro(turt, count):
    angle_step = 360 / count

    for i in range(count):
        turt.setheading(angle_step * i)
        turt.color(rand_colour())
        turt.circle(100)


def from_colorgram(cg):
    rgb = cg.rgb
    return Color(rgb.r, rgb.g, rgb.b)


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def total_color(self):
        return self.r + self.g + self.b

    def val(self):
        return self.r, self.g, self.b


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screen = Screen()
    screen.setup(600, 600)
    screen.colormode(255)

    writer = Turtle(shape="turtle")

    writer.speed(1000)
    """
    writer.penup()
    writer.setpos(-50, 50)
    writer.pd()
    draw_spiro(writer, 500)
    """

    colors = [from_colorgram(x) for x in colorgram.extract('img.jpg', 25)]
    random.shuffle(colors)

    for i in range(5):
        for j in range(5):
            writer.pu()
            writer.setpos(-255 + 120 * i, -255 + 120 * j)
            color = colors[i * 5 + j].val()
            writer.color(color, color)

            writer.begin_fill()
            writer.pd()
            writer.circle(30)
            writer.pu()
            writer.end_fill()

    screen.exitonclick()


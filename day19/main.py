import random
from turtle import Turtle, Screen


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan']
x_start = -280
x_win = 285
y_start = -70
y_step = 30
min_step = 5
max_step = 15


class FancyTurtle(Turtle):
    def __init__(self, screen, shape='classic'):
        super().__init__(shape=shape)
        self.speed('fastest')
        self.is_running = True
        self.walking = False
        self.tl = False
        self.tr = False
        self.screen = screen

        screen.onkeypress(lambda: self.change_prop('w', True), "Up")
        screen.onkeypress(lambda: self.change_prop('l', True), "Left")
        screen.onkeypress(lambda: self.change_prop('r', True), "Right")

        screen.onkeyrelease(lambda: self.change_prop('w', False), "Up")
        screen.onkeyrelease(lambda: self.change_prop('l', False), "Left")
        screen.onkeyrelease(lambda: self.change_prop('r', False), "Right")

        screen.onkey(self.quit, "q")

    def quit(self):
        self.is_running = False

    def run(self):
        if self.walking:
            self.fd(1)

        if self.tr:
            self.right(2)
        elif self.tl:
            self.left(2)

        if self.is_running:
            self.screen.ontimer(self.run, 1)

    def change_prop(self, prop, new_val):
        if prop == "w":
            self.walking = new_val
        elif prop == "l":
            self.tl = new_val
        if prop == "r":
            self.tr = new_val


class Racer(Turtle):
    def __init__(self, color, turt_y_pos):
        super().__init__()
        self.pu()
        self.turt_color = color
        self.color(color)
        self.shape('turtle')
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.y_pos = turt_y_pos
        self.x_pos = x_start

    def go_to_start(self):
        self.goto(self.x_pos, self.y_pos)

    def proceed(self):
        step = random.randint(min_step, max_step)
        self.x_pos += step
        self.fd(step)
        return self.x_pos >= x_win


class TurtRace:
    def __init__(self, racers: list[Racer], screen):
        self.racers = racers
        self.screen: Screen = screen
        self.bet = ''

    def set_bet(self, bet):
        self.bet = bet.lower()

    def on_your_marks(self):
        for r in self.racers:
            r.go_to_start()

    def step(self):
        for r in self.racers:
            if r.proceed():
                self.race_end(r)
                return r

        return self.screen.ontimer(self.step, 25)

    def race_end(self, winner):
        print(f"You guessed {self.bet}, and the winner was {winner.turt_color}.")
        print("You win!" if winner.turt_color == self.bet else "You lose!")
        return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scn = Screen()
    scn.listen()
    scn.setup(width=600, height=600)

    """
    turt = FancyTurtle(scn, shape='turtle')
    turt.run()
    """

    turts = []
    y_pos = y_start
    for col in colors:
        racer = Racer(col, y_pos)
        turts.append(racer)
        y_pos += y_step

    race = TurtRace(turts, scn)
    race.on_your_marks()

    user_bet = scn.textinput(title="Who will win?", prompt="(red, orange, yellow, green, blue, cyan): ")
    race.set_bet(user_bet)
    race.step()

    scn.exitonclick()

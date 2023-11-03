from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as file:
            score_in_file = int(file.read())
        self.high_score = score_in_file
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score} High score: {self.high_score}", False, align=ALIGNMENT, font=FONT)
    #
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0

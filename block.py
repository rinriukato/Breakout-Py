from turtle import Turtle


class Block(Turtle):
    def __init__(self, color: str):
        super().__init__()
        self.color_name = color
        self.color(color)
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=0.5)

    # TODO: MOVE BLOCK INTO PLACE - METHOD
    def set_position(self, x_cord: int, y_cord: int):
        self.setposition(x_cord, y_cord)

    def get_color(self) -> str:
        return self.color_name

    # # TODO: DESTROY BLOCK WHEN COLLIDED WITH
    # def destroy_self(self):
    #     self.clear()
    #     self.ht()
    #     del self


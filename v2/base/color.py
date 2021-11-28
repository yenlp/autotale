
class Color:
    def __init__(self) -> None:
        self.r = 0
        self.g = 0
        self.b = 0

    def setColor(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

    def BLACK():
        color = Color()
        color.setColor(0,0,0)
        return color
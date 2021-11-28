

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def setColor(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b

    def red(self):
        return self.r

    def green(self):
        return self.g

    def blue(self):
        return self.b

    def BLACK():
        color = Color(0,0,0)
        return color

    def isEqual(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def isEqual(self, other, tolerance):
        if abs(self.r - other.r) > tolerance:
            return False
        if abs(self.g - other.g) > tolerance:
            return False
        if abs(self.b - other.b) > tolerance:
            return False
        return True
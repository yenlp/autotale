from hub.quick_potion import QuickPotion

class QuickMana(QuickPotion):
    def __init__(self, x, y, color):
        print('QuickMana')
        super().__init__(x, y, color)

    def onFrameUpdate(self, deltaTime, screenshot):
        color = screenshot.getpixel(self.position)
        self.isActionRequired = self.color.blue() > color[2]

    def doAction(self):
        print('QuickMana::doAction')
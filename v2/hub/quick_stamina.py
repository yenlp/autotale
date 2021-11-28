from hub.quick_potion import QuickPotion

class QuickStamina(QuickPotion):
    def __init__(self, x, y, color):
        print('QuickStamina')
        super().__init__(x, y, color)

    def onFrameUpdate(self, deltaTime, screenshot):
        color = screenshot.getpixel(self.position)
        self.isActionRequired = self.color.green() > color[1]

    def doAction(self):
        print('QuickStamina::doAction')
from hub.quick_potion import QuickPotion

class QuickMana(QuickPotion):
    def __init__(self, x, y, color):
        #print('QuickMana')
        super().__init__(x, y, color)
        self.name = 'Mana'

    def onFrameUpdate(self, deltaTime, screenshot):
        super().onFrameUpdate(deltaTime, screenshot)
        color = screenshot.getpixel(self.position)
        self.isActionRequired = self.color.blue() > color[2]

    def isPotionInventoryEmpty(self, screenshot):
        color = screenshot.getpixel(self.inventoryPosition)
        return self.color.blue() > color[2]

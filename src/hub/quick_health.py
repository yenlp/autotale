from hub.quick_potion import QuickPotion

class QuickHealth (QuickPotion):
    def __init__ (self, x, y, color):
        #print('QuickHealth')
        super().__init__(x, y, color)
        self.name = 'Health'

    def onFrameUpdate (self, deltaTime, screenshot):
        super().onFrameUpdate(deltaTime, screenshot)
        color = screenshot.getpixel(self.position)
        self.isActionRequired = self.color.red() > color[0]

    def isPotionInventoryEmpty(self, screenshot):
        color = screenshot.getpixel(self.inventoryPosition)
        return self.color.red() > color[0]

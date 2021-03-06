from hub.quick_potion import QuickPotion

class QuickStamina(QuickPotion):
    def __init__(self, x, y, color):
        #print('QuickStamina')
        super().__init__(x, y, color)
        self.name = 'Stamina'

    def onFrameUpdate(self, deltaTime, screenshot):
        super().onFrameUpdate(deltaTime, screenshot)
        color = screenshot.getpixel(self.position)
        self.isActionRequired = self.color.green() > color[1]

    def isPotionInventoryEmpty(self, screenshot):
        color = screenshot.getpixel(self.inventoryPosition)
        return self.color.green() > color[1]


from base.color import Color
from hub.health_bar import HealthBar
from hub.mana_bar import ManaBar
from hub.stamina_bar import StaminaBar
from hub.quick_potion import QuickPotion

class HubController:
    def __init__(self):
        print('HubController')

        healthbar = HealthBar(441, 695, 610)
        healthbar.setColor(Color(170, 10, 10))
        healthbar.setPercent(0.5)
        self.potionBars = []
        self.potionBars.append(healthbar)
        self.potionBars.append(StaminaBar(100, 50, 150))
        self.potionBars.append(ManaBar(300, 50, 150))

        self.quickPotions = []
        self.quickPotions.append(QuickPotion())
        self.quickPotions.append(QuickPotion())
        self.quickPotions.append(QuickPotion())

    def onFrameUpdate(self, deltaTime, screenshot):
        print('HubController::onFrameUpdate')
        for bar in self.potionBars:
            bar.onFrameUpdate(deltaTime, screenshot)

    def onFrameRender(self, screenshot):
        print('HubController::onFrameRender')
        for bar in self.potionBars:
            bar.onFrameRender(screenshot)
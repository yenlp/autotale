
from hub.health_bar import HealthBar
from hub.mana_bar import ManaBar
from hub.stamina_bar import StaminaBar
from hub.quick_potion import QuickPotion

class HubController:
    def __init__(self):
        print('HubController')

        self.potionBars = []
        self.potionBars.append(HealthBar(200, 50, 150))
        self.potionBars.append(StaminaBar(100, 50, 150))
        self.potionBars.append(ManaBar(300, 50, 150))

        self.quickPotions = []
        self.quickPotions.append(QuickPotion())
        self.quickPotions.append(QuickPotion())
        self.quickPotions.append(QuickPotion())

    def onFrameUpdate(self, deltaTime, screenshot):
        print('HubController::onFrameUpdate')

    def onFrameRender(self, screenshot):
        print('HubController::onFrameRender')
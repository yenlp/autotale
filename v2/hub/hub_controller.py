
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
        healthbar.setPercent(0.4)

        staminaBar = StaminaBar(420, 695, 625)
        staminaBar.setColor(Color(80, 210, 10))
        staminaBar.setPercent(0.2)

        manaBar = ManaBar(588, 695, 610)
        manaBar.setColor(Color(10, 10, 135))
        manaBar.setPercent(0.3)

        self.potionBars = []
        self.potionBars.append(healthbar)
        self.potionBars.append(staminaBar)
        self.potionBars.append(manaBar)

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
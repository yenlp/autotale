
from base.color import Color
from hub.health_bar import HealthBar
from hub.mana_bar import ManaBar
from hub.quick_health import QuickHealth
from hub.quick_mana import QuickMana
from hub.quick_stamina import QuickStamina
from hub.stamina_bar import StaminaBar
from hub.inventory import Inventory
import base.keyboard_helper

class HubController:
    def __init__(self):
        #print('HubController')

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
        self.quickPotions.append(QuickStamina(620, 688, Color(0, 30, 0)))
        self.quickPotions.append(QuickHealth(645, 688, Color(30, 0, 0)))
        self.quickPotions.append(QuickMana(670, 688, Color(0, 0, 30)))

        self.inventory = Inventory()

    def onFrameUpdate(self, deltaTime, screenshot):
        #print('HubController::onFrameUpdate')
        for bar in self.potionBars:
            bar.onFrameUpdate(deltaTime, screenshot)

        for potion in self.quickPotions:
            potion.onFrameUpdate(deltaTime, screenshot)

        self.inventory.onFrameUpdate(deltaTime, screenshot)

    def onFrameRender(self, screenshot):
        #print('HubController::onFrameRender')
        for bar in self.potionBars:
            bar.onFrameRender(screenshot)
        
        if not self.inventory.isOpen():
            for potion in self.quickPotions:
                if potion.isRequired():
                    self.inventory.open()
                    break
        for potion in self.quickPotions:
            potion.onFrameRender(screenshot)

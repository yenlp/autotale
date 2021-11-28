
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

        self.vm = None

        healthbar = HealthBar(441, 695, 610)
        healthbar.setColor(Color(170, 10, 10))
        healthbar.setPercent(0.5)

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

        quickStamina = QuickStamina(620, 688, Color(0, 30, 0))
        quickStamina.setKey('1')
        quickStamina.setInventoryPosition((146, 555))
        quickHealth = QuickHealth(645, 688, Color(30, 0, 0))
        quickHealth.setKey('2')
        quickHealth.setInventoryPosition((168, 555))
        quickMana = QuickMana(670, 688, Color(0, 0, 30))
        quickMana.setKey('3')
        quickMana.setInventoryPosition((190, 555))

        self.quickPotions = []
        self.quickPotions.append(quickHealth)
        self.quickPotions.append(quickStamina)
        self.quickPotions.append(quickMana)

        self.inventory = Inventory()

    def setVM(self, vm):
        self.vm = vm
        self.inventory.setVM(vm)
        for bar in self.potionBars:
            bar.setVM(vm)

        for potion in self.quickPotions:
            potion.setVM(vm)

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
        isRequired = False
        if not self.inventory.isOpen():
            for potion in self.quickPotions:
                if potion.isRequired():
                    isRequired = True
                    self.inventory.open()
                    break
        if self.inventory.isOpen():
            for potion in self.quickPotions:
                potion.onFrameRender(screenshot)

    def isPotting(self):
        for potion in self.quickPotions:
            if potion.isRequired():
                return True
        return False


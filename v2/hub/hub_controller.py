
from base.color import Color
from hub.health_bar import HealthBar
from hub.mana_bar import ManaBar
from hub.quick_health import QuickHealth
from hub.quick_mana import QuickMana
from hub.quick_stamina import QuickStamina
from hub.stamina_bar import StaminaBar
from hub.inventory import Inventory
from hub.potion_balancing import PotionBalancing
import base.keyboard_helper
import settings

class HubController:
    def __init__(self):
        #print('HubController')

        self.vm = None

        healthbar = HealthBar(441, 695, 610)
        healthbar.setColor(Color(170, 10, 10))
        healthbar.setPercent(settings.percentHP)
        healthbar.setAutoAdjust(0.5, 0.6)

        staminaBar = StaminaBar(420, 695, 625)
        staminaBar.setColor(Color(90, 210, 10))
        staminaBar.setPercent(settings.percentSP)

        manaBar = ManaBar(588, 695, 610)
        manaBar.setColor(Color(10, 10, 135))
        manaBar.setPercent(settings.percentMP)

        self.potionBars = []
        self.potionBars.append(healthbar)
        self.potionBars.append(staminaBar)
        self.potionBars.append(manaBar)

        self.balancing = PotionBalancing()
        self.balancing.add(healthbar)
        self.balancing.add(staminaBar)
        self.balancing.add(manaBar)

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

    def onPercentChanged(self):
        self.potionBars[0].setPercent(settings.percentHP)
        self.potionBars[1].setPercent(settings.percentSP)
        self.potionBars[2].setPercent(settings.percentMP)

    def onFrameUpdate(self, deltaTime, screenshot):
        #print('HubController::onFrameUpdate')
        self.inventory.onFrameUpdate(deltaTime, screenshot)
        for bar in self.potionBars:
            bar.onFrameUpdate(deltaTime, screenshot)

        for potion in self.quickPotions:
            potion.onFrameUpdate(deltaTime, screenshot)
        
        self.balancing.onFrameUpdate(deltaTime, screenshot)

    def onFrameRender(self, screenshot):
        actionCount = 0
        for bar in self.potionBars:
            if bar.isRequired():
                actionCount = actionCount + 1
                bar.onFrameRender(screenshot)
                break
        if not self.inventory.getInteractable():
            return
        if self.inventory.isOpen():
            for potion in self.quickPotions:
                if potion.isRequired():
                    actionCount = actionCount + 1
                    potion.onFrameRender(screenshot)
                    return
            isClosing = False
            for potion in self.quickPotions:
                if potion.isCompleted():
                    isClosing = True
                    self.inventory.close()
                    potion.reset()

            if isClosing:
                return
        else:
            for potion in self.quickPotions:
                if potion.isRequired():
                    print('HUB open inventory')
                    actionCount = actionCount + 1
                    self.inventory.open()
                    break
        if actionCount == 0:
            if self.balancing.onFrameRender(screenshot):
                return
        

    def isPotting(self):
        if not self.inventory.getInteractable():
            return True
        for potion in self.quickPotions:
            if potion.isRequired():
                return True
        return False


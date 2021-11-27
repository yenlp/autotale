
from hub.health_bar import HealthBar
from hub.mana_bar import ManaBar
from hub.stamina_bar import StaminaBar
from hub.quick_potion import QuickPotion

class HubController:
    def __init__(seft):
        print('HubController')

        seft.potionBars = []
        seft.potionBars.append(HealthBar())
        seft.potionBars.append(StaminaBar())
        seft.potionBars.append(ManaBar())

        seft.quickPotions = []
        seft.quickPotions.append(QuickPotion())
        seft.quickPotions.append(QuickPotion())
        seft.quickPotions.append(QuickPotion())

from hub.potion_bar import PotionBar
from hub.quick_potion import QuickPotion

class HubController:
    def __init__(seft):
        print('HubController')

        seft.potionBars = []
        seft.potionBars.append(PotionBar())
        seft.potionBars.append(PotionBar())
        seft.potionBars.append(PotionBar())

        seft.quickPotions = []
        seft.quickPotions.append(QuickPotion())
        seft.quickPotions.append(QuickPotion())
        seft.quickPotions.append(QuickPotion())
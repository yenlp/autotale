from hub.quick_potion import QuickPotion
import random

class PotionBalancing:
    def __init__(self) -> None:
        self.potions = []

    def add(self, quickPotion):
        self.potions.append(quickPotion)

    def onFrameUpdate(self, deltaTime, screenshot):
        pass

    def onFrameRender(self, screenshot):
        n = len(self.potions)
        for i in range(n):
            j = (i + 1) % n
            potion0 = self.potions[i]
            potion1 = self.potions[j]
            diff = potion0.getCount() - potion1.getCount()
            if diff > 3:
                if random.randint(0, 100) + diff > 50:
                    potion1.potting(screenshot)
                    return True
        return False
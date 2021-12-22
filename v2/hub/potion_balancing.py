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
            if abs(diff) > 0:
                potion = potion0
                if diff > 0:
                    potion = potion1
                if True or (random.randint(0, 10) < 2 and random.randint(0, 10) < diff):
                    potion.potting(screenshot, 'Balancing ' + potion.name)
                    return True
        return False
from base.color import Color
from hub.action_gui import ActionGui

class QuickPotion (ActionGui):
    def __init__(self, x, y, color):
        print('QuickPotion')
        super().__init__()
        self.position = x, y
        self.color = color

    def onFrameUpdate(self, deltaTime, screenshot):
        pass

    def onFrameRender(self, screenshot):
        #print('PotionBar::onFrameRender')
        if self.isActionRequired:
            self.doAction()

    def doAction(self):
        print('QuickPotion::doAction')

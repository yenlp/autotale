

class SubState:
    IDLE = 0
    FIND_ENEMY = 1
    COMBAT = 2
    LOOT = 3

    POS_TOP = 485, 650
    COLOR_TOP = 80, 64, 41

    POS_BOTTOM = 485, 688
    COLOR_BOTTOM= 32, 16, 3

    POS_LEFT = 465, 668
    COLOR_LEFT = 51, 35, 17

    POS_RIGHT = 503, 668
    COLOR_RIGHT = 55, 43, 35
    
    def __init__(self) -> None:
        self.nextState = None
        self.time = 0
        self.isRotateAllowed = True

    def onFrameUpdate(self, deltaTime, screenshot, vm):
        pass

    def onFrameRender(self, screenshot, vm):
        pass

    def isCompleted(self):
        return self.nextState != None

    def getNextStateId(self):
        return self.nextState

    def doNothing(self, deltaTime, screenshot, vm):
        pass

    def isOnEnemy(self, screenshot):
        pix = screenshot.getpixel(SubState.POS_TOP)
        for i in 0,1,2:
            if abs(pix[i] - SubState.COLOR_TOP[i]) > 50:
                return True
        
        pix = screenshot.getpixel(SubState.POS_BOTTOM)
        for i in 0,1,2:
            if abs(pix[i] - SubState.COLOR_BOTTOM[i]) > 50:
                return True

        pix = screenshot.getpixel(SubState.POS_LEFT)
        for i in 0,1,2:
            if abs(pix[i] - SubState.COLOR_LEFT[i]) > 50:
                return True

        pix = screenshot.getpixel(SubState.POS_RIGHT)
        for i in 0,1,2:
            if abs(pix[i] - SubState.COLOR_RIGHT[i]) > 50:
                return True

        return False
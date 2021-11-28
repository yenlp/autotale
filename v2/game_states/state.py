

class SubState:
    def __init__(self, nextState) -> None:
        self.nextState = nextState

    def onFrameUpdate(self, deltaTime, screenshot, vm):
        pass

    def onFrameRender(self, screenshot, vm):
        pass

    def isCompleted(self):
        return False

    def getNextStateId(self):
        return self.nextState
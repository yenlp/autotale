from hub.hub_controller import HubController

class GameState:
    def __init__(self):
        #print('GameState')
        self.isRunning = True
        self.vm = None
        self.hubController = HubController()

    def setVM(self, vm):
        self.vm = vm
        self.hubController.setVM(vm)

    def onPercentChanged(self):
        self.hubController.onPercentChanged()

    def onFrameUpdate(self, deltaTime, screenshot):
        #print('GameState::onFrameUpdate')
        self.hubController.onFrameUpdate(deltaTime, screenshot)

    def onFrameRender(self, screenshot):
        #print('GameState::onFrameRender')
        self.hubController.onFrameRender(screenshot)
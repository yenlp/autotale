from hub.hub_controller import HubController

class GameState:
    def __init__(self):
        print('GameState')
        self.isRunning = True
        self.hubController = HubController()

    def onFrameUpdate(self, deltaTime, screenshot):
        print('GameState::onFrameUpdate')
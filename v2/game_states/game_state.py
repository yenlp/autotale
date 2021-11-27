from hub.hub_controller import HubController

class GameState:
    def __init__(seft):
        print('GameState')
        seft.isRunning = True
        seft.hubController = HubController()
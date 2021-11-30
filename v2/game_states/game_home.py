from game_states.game_state import GameState

class GameHome(GameState):
    def __init__(self):
        print('GameHome')
        super().__init__()

    def onFrameUpdate(self, deltaTime, screenshot):
        pass

    def onFrameRender(self, screenshot):
        pass
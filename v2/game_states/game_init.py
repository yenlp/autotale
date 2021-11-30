from game_states.game_state import GameState

class GameInit(GameState):
    def __init__(self):
        print('GameInit')
        super().__init__()
        self.hubController = None
        self.time = 0

    def onFrameUpdate(self, deltaTime, screenshot):
        self.time += deltaTime
        if self.time > 1:
            self.vm.pause()
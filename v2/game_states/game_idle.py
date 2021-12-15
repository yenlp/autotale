from game_states.game_state import GameState
import settings
import base.keyboard_helper as keyboard_helper

class GameIdle(GameState):
    def __init__(self):
        print('GameIdle')
        super().__init__()
        self.name = 'GameIdle'

    def onFrameRender(self, screenshot):
        super().onFrameRender(screenshot)
        if settings.isAutoRotate:
            key = 'right'
            keyboard_helper.keyDown(key, 0.3)
            keyboard_helper.keyUp(key)
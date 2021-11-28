from game_states.game_state import GameState

class GameIdle(GameState):
    def __init__(self):
        print('GameIdle')
        super().__init__()
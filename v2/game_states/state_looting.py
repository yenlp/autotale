from game_states.state import SubState

class StateLooting (SubState):
    def __init__(self, nextState) -> None:
        super().__init__(nextState)
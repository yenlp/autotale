from game_states.game_state import GameState
from game_states.sub_state import SubState
from game_states.state_combat import StateCombat
from game_states.state_find_enemy import StateFindEnemy
from game_states.state_looting import StateLooting

class GameBattle(GameState):
    def __init__(self):
        print('GameBattle')
        super().__init__()
        self.state = self.createState(SubState.FIND_ENEMY)

    def setVM(self, vm):
        super().setVM(vm)

    def createState(self, stateId):
        if stateId == SubState.FIND_ENEMY:
            return StateFindEnemy()
        if stateId == SubState.COMBAT:
            return StateCombat()
        if stateId == SubState.LOOT:
            return StateLooting()

    def onFrameUpdate(self, deltaTime, screenshot):
        super().onFrameUpdate(deltaTime, screenshot)
        self.state.onFrameUpdate(deltaTime, screenshot, self.vm)
        if self.state.isCompleted():
            nextState = self.state.getNextStateId()
            self.state = self.createState(nextState)

    def onFrameRender(self, screenshot):
        super().onFrameRender(screenshot)
        self.state.onFrameRender(screenshot, self.vm)
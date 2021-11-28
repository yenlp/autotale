from game_states.game_state import GameState
from game_states.state_combat import StateCombat
from game_states.state_find_enemy import StateFindEnemy
from game_states.state_looting import StateLooting

class GameBattle(GameState):
    IDLE = 0
    FIND_ENEMY = 1
    COMBAT = 2
    LOOT = 3
    def __init__(self):
        print('GameBattle')
        super().__init__()
        self.state = self.createState(GameBattle.FIND_ENEMY)

    def setVM(self, vm):
        super().setVM(vm)

    def createState(self, stateId):
        if stateId == GameBattle.FIND_ENEMY:
            return StateFindEnemy(GameBattle.COMBAT)
        if stateId == GameBattle.COMBAT:
            return StateCombat(GameBattle.LOOT)
        if stateId == GameBattle.LOOT:
            return StateLooting(GameBattle.FIND_ENEMY)

    def onFrameUpdate(self, deltaTime, screenshot):
        super().onFrameUpdate(deltaTime, screenshot)
        self.state.onFrameUpdate(deltaTime, screenshot, self.vm)
        if self.state.isCompleted():
            nextState = self.state.getNextStateId()
            self.state = self.createState(nextState)

    def onFrameRender(self, screenshot):
        super().onFrameRender(screenshot)
        self.state.onFrameRender(screenshot, self.vm)
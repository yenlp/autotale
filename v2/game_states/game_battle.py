import settings
import base.keyboard_helper as keyboard_helper
from game_states.game_state import GameState
from game_states.sub_state import SubState
from game_states.state_combat import StateCombat
from game_states.state_find_enemy import StateFindEnemy
from game_states.state_looting import StateLooting

class GameBattle(GameState):
    def __init__(self):
        print('GameBattle')
        super().__init__()
        self.name = 'GameBattle'
        self.states = []

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
        if self.hubController.isPotting():
            return
        if not settings.isAutoCombat:
            return
        if len(self.states) > 1:
            self.states.remove(self.states[0])
        elif len(self.states) == 0:
            self.states.append(self.createState(SubState.FIND_ENEMY))
        state = self.states[0]
        state.onFrameUpdate(deltaTime, screenshot, self.vm)
        if state.isCompleted():
            nextState = state.getNextStateId()
            state = self.createState(nextState)
            self.states.append(state)

    def onFrameRender(self, screenshot):
        super().onFrameRender(screenshot)
        if self.hubController.isPotting():
            return
        if not settings.isAutoCombat:
            return
        state = self.states[0]
        if settings.isAutoRotate and state.isRotateAllowed:
            key = 'right'
            keyboard_helper.keyDown(key, 0.15)
            keyboard_helper.keyUp(key)
        state.onFrameRender(screenshot, self.vm)
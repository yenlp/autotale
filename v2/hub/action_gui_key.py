from hub.action_gui import ActionGui
import base.keyboard_helper

class ActionGuiKey (ActionGui):
    def __init__(self) -> None:
        super().__init__()
        self.key = 'none'

    def setActionKey(self, key):
        self.key = key

    def doAction(self):
        base.keyboard_helper.pressKey(self.key, 'ActionGuiKey::doAction')
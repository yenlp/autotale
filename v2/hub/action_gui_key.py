from hub.action_gui import ActionGui
import base.keyboard_helper as keyboard_helper

class ActionGuiKey (ActionGui):
    def __init__(self) -> None:
        super().__init__()
        self.key = 'none'
        self.name = None

    def setActionKey(self, key):
        self.key = key

    def doAction(self, screenshot, mess = None):
        keyboard_helper.pressKey(self.key, 0.1, mess)
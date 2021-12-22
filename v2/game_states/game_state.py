import time
import datetime
import base.keyboard_helper as keyboard_helper
from hub.hub_controller import HubController

class GameState:
    def __init__(self):
        #print('GameState')
        #keyboard_helper.pressKey('a')
        time.sleep(0.2)
        self.isRunning = True
        self.name = 'GameState'
        self.timeStart = time.time()
        self.vm = None
        self.hubController = HubController()

    def onStop(self):
        t = time.time()
        ltime = time.localtime(t)
        duration = datetime.timedelta(seconds=round( t - self.timeStart))
        print('{state} is stop at {year}/{month}/{day} - {hour}:{min}:{sec}'.format(state=self.name, year=ltime.tm_year, month=ltime.tm_mon, day=ltime.tm_mday, hour=ltime.tm_hour, min=ltime.tm_min, sec=ltime.tm_sec))
        print('{state} played in duration {duration}'.format(state=self.name, duration=str(duration)))

    def setVM(self, vm):
        self.vm = vm
        if self.hubController != None:
            self.hubController.setVM(vm)

    def onPercentChanged(self):
        if self.hubController != None:
            self.hubController.onPercentChanged()

    def onFrameUpdate(self, deltaTime, screenshot):
        if self.hubController != None:
            self.hubController.onFrameUpdate(deltaTime, screenshot)

    def onFrameRender(self, screenshot):
        if self.hubController != None:
            self.hubController.onFrameRender(screenshot)
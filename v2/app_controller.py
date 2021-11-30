import time
import queue
from vm_controller import VMController
import base.keyboard_helper as keyboard_helper

class AppController:
    COMMAND_PAUSE = 0
    COMMAND_BATTLE = 1
    def __init__(self):
        print('AppController')
        self.isAlive = True
        self.commands = queue.Queue()
        self.vms = []
        keyboard_helper.setupKeyboard(self)

    def addVM(self, vm_name):
        self.vms.append(VMController(vm_name))

    def onQuitCommand(self):
        self.isAlive = False

    def onPauseCommand(self):
        self.commands.put(AppController.COMMAND_PAUSE)

    def onBattleCommand(self):
        self.commands.put(AppController.COMMAND_BATTLE)

    # update virtual machines 
    # main update function
    def onFrameUpdate(self, deltaTime):
        if self.commands.qsize() > 0:
            comm = self.commands.get()
            if comm != None:
                if comm == AppController.COMMAND_PAUSE:
                    for vm in self.vms:
                        vm.pause()
                elif comm == AppController.COMMAND_BATTLE:
                    for vm in self.vms:
                        vm.battle()

        for vm in self.vms:
            vm.onFrameUpdate(deltaTime)

    # render function
    # do actions
    def onFrameRender(self):
        for vm in self.vms:
            vm.onFrameRender()

    def run(self):
        FPS = 10
        FRAME_RATE = 1.0 / FPS
        current_time = time.time()
        last_time = current_time
        frame_count = 0
        while self.isAlive:
            frame_count = frame_count + 1
            #print('frame', frame_count)
            current_time = time.time()
            dt = current_time - last_time            
            
            self.onFrameUpdate(dt)
            self.onFrameRender()
    
            last_time = current_time
            t = time.time()
            frame_time = t - last_time
            if frame_time < FRAME_RATE:
                time.sleep(FRAME_RATE - frame_time)
        print('Exit')
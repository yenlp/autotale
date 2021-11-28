from vm_controller import VMController
import time
import base.keyboard_helper

class AppController:
    def __init__(self):
        print('AppController')
        self.isAlive = True
        self.isPause = False
        self.vms = []
        base.keyboard_helper.setupKeyboard(self)

    def addVM(self, vm_name):
        self.vms.append(VMController(vm_name))

    def onQuitCommand(self):
        self.isAlive = False

    # update virtual machines 
    # main update function
    def onFrameUpdate(self, deltaTime):
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
            print('frame', frame_count)
            current_time = time.time()
            dt = current_time - last_time            
            if not self.isPause:
                self.onFrameUpdate(dt)
                self.onFrameRender()
    
            last_time = current_time
            t = time.time()
            frame_time = t - last_time
            if frame_time < FRAME_RATE:
                time.sleep(FRAME_RATE - frame_time)
        print('Exit')
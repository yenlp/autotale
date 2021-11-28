from vm_controller import VMController
import time

class AppController:
    def __init__(self):
        print('AppController')
        self.isAlive = True
        self.isPause = False
        self.vms = []

    def addVM(self, vm_name):
        self.vms.append(VMController(vm_name))

    # update virtual machines 
    # main update function
    def onFrameUpdate(self, deltaTime):
        for vm in self.vms:
            vm.onFrameUpdate(deltaTime)

    def run(self):
        FPS = 2
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
    
            last_time = current_time
            t = time.time()
            frame_time = t - last_time
            if frame_time < FRAME_RATE:
                time.sleep(FRAME_RATE - frame_time)
            if frame_count > 1:
                self.isAlive = False
        print('Exit')
from vm_controller import VMController
import time

class AppController:
    def __init__(seft):
        print('AppController')
        seft.isAlive = True
        seft.isPause = False
        seft.vms = []

    def addVM(seft, vm_name):
        seft.vms.append(VMController(vm_name))

    # update virtual machines 
    # main update function
    def update(seft, deltaTime):
        for vm in seft.vms:
            vm.update(deltaTime)

    def run(seft):
        FPS = 2
        FRAME_RATE = 1.0 / FPS
        current_time = time.time()
        last_time = current_time
        frame_count = 0
        while seft.isAlive:
            frame_count = frame_count + 1
            print('frame', frame_count)
            current_time = time.time()
            dt = current_time - last_time            
            if not seft.isPause:
                seft.update(dt)  
    
            last_time = current_time
            t = time.time()
            frame_time = t - last_time
            if frame_time < FRAME_RATE:
                time.sleep(FRAME_RATE - frame_time)
            if frame_count > 2:
                seft.isAlive = False
        print('Exit')
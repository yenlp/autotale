import auto_keyboard
import auto_mouse

def init():
    auto_keyboard.init()
    
def update(img):
    auto_keyboard.update(img)
    auto_mouse.update(img)
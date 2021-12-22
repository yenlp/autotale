import pyautogui

class ScreenUtils:
    def __init__(self):
        self.img = None

    def capture(self, region):
        self.img = pyautogui.screenshot(region=region)
        return self.img

    def captureAndSave(self, filepath, region):
        self.img = pyautogui.screenshot(filepath, region)
        return self.img
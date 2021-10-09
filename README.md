# autotale
Autotale is project to play priston tale automatically.

Requirements:
    1. Virtual machine:
        Install virtual machine run windows 10. Named VM as AutoBot
        Install Priston Tale on that VM.
    2. Environment:
        python3: https://www.python.org/downloads/
        pyautogui: https://pypi.org/project/PyAutoGUI/
        keyboard: https://pypi.org/project/keyboard/
        pygetwindow: https://pypi.org/project/PyGetWindow/

How to play:
    1. Remote desktop tp VM, set display 1024x 768
    2. Start Priston Tale, settings in game:
        Display mode: windowded
        Resolution: 800x600 (or anything smaller than 1024x768)
        Maximize Priston Tale window, you should be promted that resolution changed, choose YES.
        Now open game settings again, the resolution should be 1024x705, that's ok.
    3. Login to game
    4. Start auto tale:
        On host machine, cd to auto tale directory and run command:
            auto_play.bat
    5: Hot keys:
        Ctrl+B: start battle
        Ctrl+H: control at home
        Ctrl+P: pause
        Ctrl+0: exit




import sys
import time
import random
import datetime


platform = sys.platform
if platform == "darwin":
    import _pyautogui_osx as platformModule
elif platform == "win32":
    from Win_32 import Win_32 as platformModule
    # import Win_32 as platformModule
    # import _pyautogui_win as platformModule
elif platform == "linux":
    import _pyautogui_x11 as platformModule
else:
    raise NotImplementedError(f"Your platform ({platform}) is not supported by PyAutoGUI.")


if sys.version_info[0] == 2 or sys.version_info[0:2] in ((3, 1), (3, 2)):
    from collections import Sequence
else:
    from collections.abc import Sequence



class Autogui:
    
    def __init__(self) -> None:
        self.LEFT = "left"
        self.MIDDLE = "middle"
        self.RIGHT = "right"
        self.PRIMARY = "primary"
        self.SECONDARY = "secondary"
        self.__version__ = "0.1"
    
    # [+] Get size window
    def size(self):
        return platformModule._size()
    
    # [+] Get position
    def position(self):
        return platformModule._position()
    
    # [+] Move to coords
    def moveTo(self, x, y):
        platformModule._moveTo(x, y)
    
    # [+] Use hot keys
    def hotkey(interval = None, *args):
        
        if len(args) and isinstance(args[0], Sequence) and not isinstance(args[0], str):
            args = tuple(args[0])
            
        for c in args:
            print(c)
            platformModule._keyDown(c.lower() if len(c) > 1 else c )
            time.sleep(.1 if interval is None else random.randint(1, 3) / 10)
        
        for c in reversed(args):
            platformModule._keyUp(c.lower() if len(c) > 1 else c)
            time.sleep(.1 if interval is None else random.randint(1, 3) / 10)
    
    # [+] Get info
    def getInfo(self):
        return (sys.platform, sys.version, self.__version__, sys.executable, self.size(), datetime.datetime.now())
    
    # [+] Press on button type
    def press(self, keys):
        
        if type(keys) == str:
            
            keys = [keys.lower() if len(keys) > 1 else keys]
        
        else:
            lowerKeys = []
            for s in keys: lowerKeys.append(s.lower() if len(s) > 1 else s)
            keys = lowerKeys
        
        for k in keys:
            platformModule._keyDown(k)
            time.sleep(random.randint(1, 3) / 100)
            platformModule._keyUp(k)
    
    # [+] Write text
    def typewrite(self, message, interval=None):
        for c in message:
            self.press(c)
            time.sleep( random.randint(100, 300) / 1000 if interval is None else interval)
    
    # [+] Click
    def click(self, clicks=1, button=None, interval = None):
        
        button = self.LEFT if button is None else button
        
        interval = random.randint(100, 200) / 1000 if interval is None else interval
        
        if sys.platform == 'darwin':
            for i in range(clicks):
                if button in (LEFT, MIDDLE, RIGHT):
                    platformModule._multiClick(x, y, button, 1, interval)
        else:
            for _ in range(clicks):
                if button in [self.LEFT, self.MIDDLE, self.RIGHT]:
                    platformModule._click(button)
                
                time.sleep(interval)
    
    # [+] Press button dowm
    def mouseDown(self, button=None):
        
        button = self.LEFT if button is None else button
        platformModule._mouseDown(button)
    
    # [+] Press button up
    def mouseUp(self, button=None):
        
        button = self.LEFT if button is None else button
        platformModule._mouseUp(button)
    
    def scroll(self, clicks):
        platformModule._scroll(clicks)

if __name__ == '__main__':
    
    autogui = Autogui()

    # example

    # get size screen
    size = autogui.size()

    # get mouse position
    position = autogui.position()
    
    # time.sleep(2)
    
    autogui.typewrite("hellllo df")
    
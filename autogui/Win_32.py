import ctypes
import ctypes.wintypes

try:
   ctypes.windll.user32.SetProcessDPIAware()
except AttributeError:
    pass # Windows XP doesn't support this, so just do nothing.


class Win_32:
    
    LEFT = "left"
    MIDDLE = "middle"
    RIGHT = "right"
    
    MOUSEEVENTF_MOVE = 0x0001
    MOUSEEVENTF_LEFTDOWN = 0x0002
    MOUSEEVENTF_LEFTUP = 0x0004
    MOUSEEVENTF_LEFTCLICK = MOUSEEVENTF_LEFTDOWN + MOUSEEVENTF_LEFTUP
    MOUSEEVENTF_RIGHTDOWN = 0x0008
    MOUSEEVENTF_RIGHTUP = 0x0010
    MOUSEEVENTF_RIGHTCLICK = MOUSEEVENTF_RIGHTDOWN + MOUSEEVENTF_RIGHTUP
    MOUSEEVENTF_MIDDLEDOWN = 0x0020
    MOUSEEVENTF_MIDDLEUP = 0x0040
    MOUSEEVENTF_MIDDLECLICK = MOUSEEVENTF_MIDDLEDOWN + MOUSEEVENTF_MIDDLEUP
    MOUSEEVENTF_ABSOLUTE = 0x8000
    MOUSEEVENTF_WHEEL = 0x0800
    MOUSEEVENTF_HWHEEL = 0x01000
    KEYEVENTF_KEYDOWN = 0x0000
    KEYEVENTF_KEYUP = 0x0002
    INPUT_MOUSE = 0
    INPUT_KEYBOARD = 1
    
    KEY_NAMES = [
    "\t",
    "\n",
    "\r",
    " ",
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "\\",
    "]",
    "^",
    "_",
    "`",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "{",
    "|",
    "}",
    "~",
    "accept",
    "add",
    "alt",
    "altleft",
    "altright",
    "apps",
    "backspace",
    "browserback",
    "browserfavorites",
    "browserforward",
    "browserhome",
    "browserrefresh",
    "browsersearch",
    "browserstop",
    "capslock",
    "clear",
    "convert",
    "ctrl",
    "ctrlleft",
    "ctrlright",
    "decimal",
    "del",
    "delete",
    "divide",
    "down",
    "end",
    "enter",
    "esc",
    "escape",
    "execute",
    "f1",
    "f10",
    "f11",
    "f12",
    "f13",
    "f14",
    "f15",
    "f16",
    "f17",
    "f18",
    "f19",
    "f2",
    "f20",
    "f21",
    "f22",
    "f23",
    "f24",
    "f3",
    "f4",
    "f5",
    "f6",
    "f7",
    "f8",
    "f9",
    "final",
    "fn",
    "hanguel",
    "hangul",
    "hanja",
    "help",
    "home",
    "insert",
    "junja",
    "kana",
    "kanji",
    "launchapp1",
    "launchapp2",
    "launchmail",
    "launchmediaselect",
    "left",
    "modechange",
    "multiply",
    "nexttrack",
    "nonconvert",
    "num0",
    "num1",
    "num2",
    "num3",
    "num4",
    "num5",
    "num6",
    "num7",
    "num8",
    "num9",
    "numlock",
    "pagedown",
    "pageup",
    "pause",
    "pgdn",
    "pgup",
    "playpause",
    "prevtrack",
    "print",
    "printscreen",
    "prntscrn",
    "prtsc",
    "prtscr",
    "return",
    "right",
    "scrolllock",
    "select",
    "separator",
    "shift",
    "shiftleft",
    "shiftright",
    "sleep",
    "space",
    "stop",
    "subtract",
    "tab",
    "up",
    "volumedown",
    "volumemute",
    "volumeup",
    "win",
    "winleft",
    "winright",
    "yen",
    "command",
    "option",
    "optionleft",
    "optionright",
    ]
    KEYBOARD_KEYS = KEY_NAMES
    
    keyboardMapping = dict([(key, None) for key in KEY_NAMES])
    keyboardMapping.update({
    'backspace': 0x08,
    '\b': 0x08, 
    'super': 0x5B,
    'tab': 0x09, 
    '\t': 0x09, 
    'clear': 0x0c, 
    'enter': 0x0d, 
    '\n': 0x0d, 
    'return': 0x0d, 
    'shift': 0x10, 
    'ctrl': 0x11,
    'alt': 0x12, 
    'pause': 0x13, 
    'capslock': 0x14, 
    'kana': 0x15, 
    'hanguel': 0x15,
    'hangul': 0x15, 
    'junja': 0x17, 
    'final': 0x18, 
    'hanja': 0x19, 
    'kanji': 0x19, 
    'esc': 0x1b,
    'escape': 0x1b, 
    'convert': 0x1c, 
    'nonconvert': 0x1d, 
    'accept': 0x1e, 
    'modechange': 0x1f, 
    ' ': 0x20,
    'space': 0x20, 
    'pgup': 0x21,
    'pgdn': 0x22,
    'pageup': 0x21, 
    'pagedown': 0x22,
    'end': 0x23,
    'home': 0x24, 
    'left': 0x25, 
    'up': 0x26, 
    'right': 0x27, 
    'down': 0x28, 
    'select': 0x29,
    'print': 0x2a, 
    'execute': 0x2b, 
    'prtsc': 0x2c, 
    'prtscr': 0x2c, 
    'prntscrn': 0x2c, 
    'printscreen': 0x2c,
    'insert': 0x2d, 
    'del': 0x2e, 
    'delete': 0x2e, 
    'help': 0x2f, 
    'win': 0x5b, 
    'winleft': 0x5b, 
    'winright': 0x5c, 
    'apps': 0x5d, 
    'sleep': 0x5f,
    'num0': 0x60, 
    'num1': 0x61, 
    'num2': 0x62,
    'num3': 0x63, 
    'num4': 0x64,
    'num5': 0x65, 
    'num6': 0x66,
    'num7': 0x67, 
    'num8': 0x68,
    'num9': 0x69, 
    'multiply': 0x6a,
    'add': 0x6b,
    'separator': 0x6c, 
    'subtract': 0x6d, 
    'decimal': 0x6e, 
    'divide': 0x6f, 
    'f1': 0x70, 
    'f2': 0x71, 
    'f3': 0x72, 
    'f4': 0x73, 
    'f5': 0x74, 
    'f6': 0x75, 
    'f7': 0x76, 
    'f8': 0x77, 
    'f9': 0x78,
    'f10': 0x79, 
    'f11': 0x7a,
    'f12': 0x7b, 
    'f13': 0x7c, 
    'f14': 0x7d,
    'f15': 0x7e, 
    'f16': 0x7f, 
    'f17': 0x80, 
    'f18': 0x81, 
    'f19': 0x82,
    'f20': 0x83, 
    'f21': 0x84,
    'f22': 0x85, 
    'f23': 0x86, 
    'f24': 0x87,
    'numlock': 0x90,
    'scrolllock': 0x91, 
    'shiftleft': 0xa0, 
    'shiftright': 0xa1,
    'ctrlleft': 0xa2,
    'ctrlright': 0xa3,
    'altleft': 0xa4,
    'altright': 0xa5,
    'browserback': 0xa6, 
    'browserforward': 0xa7, 
    'browserrefresh': 0xa8, 
    'browserstop': 0xa9, 
    'browsersearch': 0xaa,
    'browserfavorites': 0xab, 
    'browserhome': 0xac,
    'volumemute': 0xad, 
    'volumedown': 0xae, 
    'volumeup': 0xaf, 
    'nexttrack': 0xb0,
    'prevtrack': 0xb1, 
    'stop': 0xb2, 
    'playpause': 0xb3,
    'launchmail': 0xb4,
    'launchmediaselect': 0xb5,
    'launchapp1': 0xb6, 
    'launchapp2': 0xb7, 
    })
    
    
    def isShiftCharacter(character): return character.isupper() or character in set('~!@#$%^&*()_+{}|:"<>?')
    
    
    def _position():
        cursor = ctypes.wintypes.POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
        return (cursor.x, cursor.y)
    
    
    def _key_Down_Up(type_b, key):
        
        if key not in Win_32.keyboardMapping or Win_32.keyboardMapping[key] is None: return
        needsShift = Win_32.isShiftCharacter(key)
        mods, vkCode = divmod(Win_32.keyboardMapping[key], 0x100)
        
        for apply_mod, vk_mod in [(mods & 4, 0x12), (mods & 2, 0x11), (mods & 1 or needsShift, 0x10)]:
            if apply_mod:
                ctypes.windll.user32.keybd_event(vk_mod, 0, type_b, 0) 
        
        ctypes.windll.user32.keybd_event(vkCode, 0, type_b, 0)
        
        for apply_mod, vk_mod in [(mods & 1 or needsShift, 0x10), (mods & 2, 0x11), (mods & 4, 0x12)]:
            if apply_mod:
                ctypes.windll.user32.keybd_event(vk_mod, 0, Win_32.KEYEVENTF_KEYUP, 0)
        
        
    def _keyDown(key): Win_32._key_Down_Up(Win_32.KEYEVENTF_KEYDOWN, key)
    
    
    def _keyUp(key): Win_32._key_Down_Up(Win_32.KEYEVENTF_KEYUP, key)
    
    
    def _moveTo(x, y): ctypes.windll.user32.SetCursorPos(x, y)
    
    
    def _size(): return (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
    
    
    def _click_down_up(button, LEFT, MIDDLE, RIGHT):
        if button not in (Win_32.LEFT, Win_32.MIDDLE, Win_32.RIGHT):
            raise ValueError('button arg to _click() must be one of "left", "middle", or "right", not %s' % button)
        
        if button == Win_32.LEFT:
            EV = LEFT
        if button == Win_32.MIDDLE:
            EV = MIDDLE
        if button == Win_32.RIGHT:
            EV = RIGHT
        
        try:
            ctypes.windll.user32.mouse_event(EV)
        except (PermissionError, OSError):
            pass
    
    
    def _click(button): Win_32._click_down_up(button, Win_32.MOUSEEVENTF_LEFTCLICK, Win_32.MOUSEEVENTF_MIDDLECLICK, Win_32.MOUSEEVENTF_RIGHTCLICK)
    
    
    def _mouseDown(button): Win_32._click_down_up(button, Win_32.MOUSEEVENTF_LEFTDOWN, Win_32.MOUSEEVENTF_MIDDLEDOWN, Win_32.MOUSEEVENTF_RIGHTDOWN)


    def _mouseUp(button): Win_32._click_down_up(button, Win_32.MOUSEEVENTF_LEFTUP, Win_32.MOUSEEVENTF_MIDDLEUP, Win_32.MOUSEEVENTF_RIGHTUP)
    
    
    def _scroll(clicks): ctypes.windll.user32.mouse_event(Win_32.MOUSEEVENTF_WHEEL, 0, 0, clicks, 0)
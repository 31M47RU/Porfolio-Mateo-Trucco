import pyautogui
import time, random

def slip(taim):
    time.sleep(taim)
    
def indetectable(taim, range=1):
    if taim >= 1:
        slip(random.randint(taim - range, taim + range))
    else: slip(random.randint(1 + range, taim + range))
    
def walk(key, value=17, range=1):
    if key is None or value is None:
        raise ValueError("key and value must not be None")
    else:
        pyautogui.keyDown(key)
        indetectable(value, range)
        pyautogui.keyUp(key)

def mani():
    walk('a', 10, 5)
    walk('d', 10, 5)

while True:
    mani()

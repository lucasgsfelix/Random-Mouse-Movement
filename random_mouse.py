import time
import random
import win32api, win32con



def click(x,y):
    
    win32api.SetCursorPos((random.randint(0, 100), random.randint(0, 100)))


while True:

    click(0, 0)

    time.sleep(5)
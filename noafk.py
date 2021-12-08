import pyautogui
import os
import time
import random
import pygetwindow as gw
from threading import Thread
global test, running
import keyboard


def threaded_function(arg):
    global test
    time.sleep(arg)
    test = True


def press_timer(min, max):
    time.sleep(random.randrange(min, max) / 1000)
    return


inputs = ['u', 'i', 'o', 'p']
afkTimer = 25
afkSeconds = afkTimer*60

print("FFXIV no afk")
input("Press ENTER to continue...")
win = gw.getWindowsWithTitle('FINAL FANTASY XIV')[0]
win2 = gw.getWindowsWithTitle('noafk.exe')[0]
win.activate()
os.system('cls')
print("FFXIV no afk")
print("Press ESCAPE to stop...")
now = time.time()
running = True
while running:
    test = False
    rand_key = inputs[random.randint(0, len(inputs)-1)]
    pyautogui.keyDown(rand_key)
    press_timer(250, 750)
    pyautogui.keyUp(rand_key)
    press_timer(500, 1000)
    pyautogui.keyDown(rand_key)
    press_timer(250, 750)
    pyautogui.keyUp(rand_key)

    noAfkTimer = random.randrange(0, afkSeconds*1000)/1000
    thread = Thread(target=threaded_function, daemon=True, args=(noAfkTimer, ))
    thread.start()
    endtime = time.time()+noAfkTimer
    win2.activate()
    while not test:
        delay = int(endtime-time.time())
        min = str(int(delay/60)).zfill(2)
        sec = str(int(delay % 60)).zfill(2)
        print("Pressing key in : \t "+min+":"+sec, end='\r')
        if keyboard.is_pressed('esc'):
            running = False
            exit()
    win.activate()
    thread.join()



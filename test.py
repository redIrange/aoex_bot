from functools import update_wrapper
import pyautogui
from PIL import Image, ImageFile
from PIL import ImageGrab
import time
import threading
import tkinter as tk
import sys

ImageFile.LOAD_TRUNCATED_IMAGES = True


def ready_up():
    im = ImageGrab.grab()
    im = ImageGrab.grab()
    im.save("test_image.png", "png")
    ima = Image.open(r"D:\2 school\screen capture test\test_image.png")
    px = ima.load()
    #print(px[66, 1238])
    check = open("state.txt","r")
    if str(px[66, 1238]) == "(83, 84, 88)":
        print("true")
        pyautogui.moveTo(40, 1238)
        pyautogui.click(button='left')
        pyautogui.moveTo(70, 1238)
        pyautogui.click(button='left')


def level_skip():
    time.sleep(1)
    im = ImageGrab.grab()
    im.save("test_image.png", "png")
    ima2 = Image.open(r"D:\2 school\screen capture test\test_image.png")
    px2 = ima2.load()
    print(px2[192, 22])
    if str(px2[192, 22]) == "(201, 29, 40)":
        print("true")
        pyautogui.moveTo(192, 22)
        pyautogui.click(button='left')
        pyautogui.moveTo(1190, 1300)
        pyautogui.click(button='left')


def main_loop():
    running = True
    while running == True:
        change_state = open("state.txt","r")
        for i in change_state:
            if i == "True":
                ready_up()
                level_skip()
        change_state.close()


def check_state():
    state = open("state.txt","r")
    for i in state:
        return i

def start_loop():
    label.config(text="running")
    print("starting")
    change_state = open("state.txt","w")
    change_state.write("True")
    change_state.close()

def stop_loop():
    label.config(text="stopped")
    print("stopping")
    change_state = open("state.txt","w")
    change_state.write("False")
    change_state.close()

def stop_program():
    global window
    window.quit()
    time.sleep(2)
    sys.exit()


change_state = open("state.txt","w")
change_state.write("False")
change_state.close()

loop = threading.Thread(target=main_loop)
loop.start()

global window
window = tk.Tk()
start_stop0 = tk.Button(text="Start", width=25, height=5, bg="blue", fg="yellow", command = start_loop)
start_stop0.pack()

start_stop1 = tk.Button(text="Stop", width=25, height=5, bg="blue", fg="yellow", command = stop_loop)
start_stop1.pack()

global label
label = tk.Label(text="stopped")
label.pack()

exit = tk.Button(text="Exit", width=25, height=3, bg="blue", fg="yellow", command = stop_program)
exit.pack()

window.mainloop()
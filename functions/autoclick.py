import pyautogui
import time
from threading import Event

enabled = Event()

def autoclick(button, delay, coordX, coordY):
    mousebutton = button
    enabled.clear()
    match mousebutton:
        case "Esquerdo":
            mousebutton = "left";
        case "Direito":
            mousebutton =  "right";
        case "Centro":
            mousebutton = "middle";
    time.sleep(delay)
    while not enabled.is_set():   
        pyautogui.click(x=coordX, y=coordY, button=mousebutton);
        time.sleep(delay);
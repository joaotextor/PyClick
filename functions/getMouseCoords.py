import dearpygui.dearpygui as dpg
import pyautogui

from functions.delayWithMessage import *
from functions.autoclick import *

def getMouseCoords():
    coordinateX, coordinateY = pyautogui.position();
    return coordinateX, coordinateY;
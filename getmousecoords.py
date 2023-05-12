import pyautogui


def getmousecoords():
    coordinateX, coordinateY = pyautogui.position();
    return coordinateX, coordinateY;
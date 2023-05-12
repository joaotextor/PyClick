import dearpygui.dearpygui as dpg

from pynput.mouse import Listener, Button
import pyautogui

global drag_coordX
global drag_coordY
global defaultDelay

drag_coordX = 0
drag_coordY = 0
defaultDelay = 3

from functions.delayWithMessage import *
from functions.getMouseCoords import *


def on_click(x, y, button, pressed):
    listglobals = globals()
    if pressed:
        if (button == Button.middle):
            oldX, oldY = getMouseCoords()
            pyautogui.dragTo(listglobals["drag_coordX"], listglobals["drag_coordY"], 0.135, pyautogui.easeInQuad)
            pyautogui.moveTo(oldX, oldY)

listener = Listener(on_click=on_click)

def toggleListener():
    if not listener.running:
        listener.start()
        dpg.configure_item("btnToggleListener", label="Parar")
    else:
        listener.stop()
        dpg.configure_item("btnToggleListener", label="Iniciar")

def handleCoordCaptureClick(message, delay, texttag, donemessage):
    listglobals = globals()
    dpg.configure_item(texttag, show=True)
    delayWithMessage(message, delay, texttag, donemessage)
    listglobals["drag_coordX"], listglobals["drag_coordY"] = getMouseCoords()
    dpg.set_value(texttag, f"Coordenadas: X: {listglobals['drag_coordX']}, Y: {listglobals['drag_coordY']}")


def wAutoDrag():
    wAutoDrag = dpg.window(label="Clique para Arrastar", no_move=True, no_close=True, pos=[275,0], autosize=True)
        
    with wAutoDrag:
        listglobals = globals()
        dpg.add_text("", tag="mymessage_drag", show=False)
        dpg.add_button(label="Capturar Coordenadas de Destino", callback=lambda: handleCoordCaptureClick("Posicione o Mouse no local desejado.\nCaptura em", listglobals["defaultDelay"], "mymessage_drag", "Coordenadas capturadas"))
        dpg.add_text("Clique com o botão médio (scroll) para arrastar.")
        dpg.add_button(label="Iniciar", callback=toggleListener, tag="btnToggleListener")
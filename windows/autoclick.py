import dearpygui.dearpygui as dpg
from threading import Thread

from functions.delayWithMessage import *
from functions.getMouseCoords import *
from functions.autoclick import *

global mouseButton
global defaultDelay
global clickDelay
global click_coordX
global click_coordY

click_coordX = 5
click_coordY = 5

mouseButton = "Esquerdo"

def setRadioValuetoVariable(sender, appdata, userdata, variable):
    listglobals = globals()
    listglobals[variable] = appdata

def handleAutoClickButton(mousebutton, coordx, coordy):
    listglobals = globals()
    listglobals["clickDelay"] = dpg.get_value("slider_delay")
    tStartAutoclick = Thread(target=autoclick, args=(mousebutton, listglobals["clickDelay"], coordx, coordy)).start()  

def handleCoordCaptureClick(message, delay, texttag, donemessage):
    listglobals = globals()
    dpg.configure_item(texttag, show=True)
    delayWithMessage(message, delay, texttag, donemessage)
    listglobals["click_coordX"], listglobals["click_coordY"] = getMouseCoords()
    dpg.set_value(texttag, f"Coordenadas: X: {listglobals['click_coordX']}, Y: {listglobals['click_coordY']}")

def wAutoClick():
    wAutoClick = dpg.window(label="Clique Automatico", width=275, height=260, no_move=True, no_close=True)

    with wAutoClick:
        listglobals = globals()
        listglobals["defaultDelay"] = 3
        dpg.add_text("", tag="mymessage", show=False)
        dpg.add_button(label="Capturar Coordenadas", callback=lambda: handleCoordCaptureClick("Posicione o Mouse no local desejado.\nCaptura em", listglobals["defaultDelay"], "mymessage", "Coordenadas capturadas"))
        dpg.add_text("Botão do mouse:")
        dpg.add_radio_button(("Esquerdo", "Direito", "Centro"), default_value="Esquerdo", tag="rd_mousebutton", callback=lambda v1,v2,v3: setRadioValuetoVariable(v1,v2,v3, "mouseButton"))
        dpg.add_text("Delay (segundos)\nCtrl+Click para entrada manual.")
        dpg.add_slider_float(min_value=0.1, max_value=10, default_value=5, width=100, tag="slider_delay")
        listglobals["clickDelay"] = dpg.get_value("slider_delay")
        
        with dpg.group(horizontal=True):
            dpg.add_button(label="Iniciar Auto Click", callback=lambda: handleAutoClickButton(listglobals["mouseButton"], listglobals["click_coordX"], listglobals["click_coordY"]), tag="btnstart")
            dpg.add_button(label="Parar Auto Click", callback=lambda: enabled.set(), tag="btnstop")

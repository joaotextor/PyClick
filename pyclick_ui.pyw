import dearpygui.dearpygui as dpg
from threading import Event, Thread

from delayWithMessage import delayWithMessage
from autoclick import *
from getmousecoords import getmousecoords

global mouseButton
global coordX
global coordY
global defaultDelay
global clickDelay

mouseButton = "Esquerdo"
coordX = 0
coordY = 0

def setRadioValuetoVariable(sender, appdata, userdata, variable):
    listglobals = globals()
    listglobals[variable] = appdata

def handleCoordCaptureClick(message, delay, texttag, donemessage):
    listglobals = globals()
    delayWithMessage(message, delay, texttag, donemessage)
    listglobals["coordX"], listglobals["coordY"] = getmousecoords()
    coordX = listglobals["coordX"]
    coordY = listglobals["coordY"]
    dpg.set_value(texttag, f"Coordenadas: X: {coordX}, Y: {coordY}")

def handleAutoClickButton(mousebutton, delay, coordx, coordy):
    tStartAutoclick = Thread(target=autoclick, args=(mousebutton, delay, coordx, coordy)).start()

def main():
    dpg.create_context()
    
    mainwindow = dpg.window(label="Auto Click", autosize=True)

    with mainwindow:
        listglobals = globals()
        listglobals["defaultDelay"] = 3
        dpg.add_text("", tag="mymessage")
        dpg.add_button(label="Capturar Coordenadas", callback=lambda s: handleCoordCaptureClick("Posicione o Mouse no local desejado.\nCaptura em", listglobals["defaultDelay"], "mymessage", "Coordenadas capturadas"))
        dpg.add_text("Botão")
        
        dpg.add_radio_button(("Esquerdo", "Direito", "Centro"), default_value="Esquerdo", tag="rd_mousebutton", callback=lambda v1,v2,v3, vname: setRadioValuetoVariable(v1,v2,v3, "mouseButton"))
        dpg.add_text("Delay (segundos)")
        dpg.add_input_float(default_value=0.1, width=100, tag="input_delay")
        listglobals["clickDelay"] = 3
        dpg.add_button(label="Iniciar Auto Click", callback=lambda: handleAutoClickButton(listglobals["mouseButton"], listglobals["clickDelay"], listglobals["coordX"], listglobals["coordY"]), tag="btnstart")
        dpg.add_button(label="Parar Auto Click", callback=lambda: enabled.set(), tag="btnstop")

    dpg.create_viewport(title='Autoclick v1.0', width=600, height=500)
    dpg.setup_dearpygui()    
    dpg.show_viewport()
    dpg.start_dearpygui()
        
    dpg.destroy_context()      
  
main()
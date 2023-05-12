import time
import dearpygui.dearpygui as dpg

def delayWithMessage(message, timeInSeconds, componentTag, doneMessage):
    for i in range(timeInSeconds):
        dpg.set_value(componentTag, f'{message} {timeInSeconds-i} segundos...')
        time.sleep(1)
    dpg.set_value(componentTag, doneMessage)
    

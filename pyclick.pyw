import dearpygui.dearpygui as dpg

# global click_coordX
# global click_coordY

# click_coordX = 0
# click_coordY = 0

from windows.autoclick import *
from windows.autodrag import *

def main():
    dpg.create_context()

    # Windows
    wAutoClick()
    wAutoDrag()
    
    dpg.create_viewport(title='Autoclick v1.0', width=700, height=500, small_icon="Autoclick.ico", large_icon="Autoclick.ico")
    dpg.setup_dearpygui()    
    dpg.show_viewport()
    dpg.start_dearpygui()
    
    dpg.destroy_context()  
        
  
main()
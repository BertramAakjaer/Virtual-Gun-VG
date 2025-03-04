import pystray, os, threading   
from PIL import Image, ImageDraw

from modules.vg_logic import run_program

def setup_tray():
    
    image = Image.open(os.path.join(os.path.dirname(__file__), 'assets', 'icon_tray.png'))
    menu = (pystray.MenuItem('Close Program', on_quit),)

    icon = pystray.Icon("virtual-gun", image, "Virtual-Gun-VG", menu)
    return icon

def on_quit(icon, item):
    icon.stop()
    exit()

def main():
    icon = setup_tray()
    background_thread = threading.Thread(target=run_program)
    background_thread.daemon = True
    background_thread.start()

    icon.run()

if __name__ == "__main__":
    main()
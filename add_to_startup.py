import os, winshell, sys

def add_bat_script(script, bat):
    path_to_py = sys.executable
    path_to_py = path_to_py[:-10] + 'pythonw.exe'

    with open(bat, 'w') as bat_file:
        bat_file.write(f'start {path_to_py} "{script}"\nexit')

def add_to_startup(script_path, icon_path):
    # Get the path to the startup folder
    startup_folder = winshell.startup()
    
    # Create a shortcut in the startup folder
    shortcut_path = os.path.join(startup_folder, 'Virtual Gun.lnk')
    
    with winshell.shortcut(shortcut_path) as shortcut:
        shortcut.path = script_path
        shortcut.icon_location = (icon_path, 0)

this_script_location = os.path.abspath(__file__)
bat_location = os.path.join(os.path.dirname(this_script_location), 'startup.bat')
script_location = os.path.join(os.path.dirname(this_script_location), 'tray_icon_setup.pyw')


icon_location = os.path.join(os.path.dirname(this_script_location), 'assets', 'icon_tray.ico')

add_bat_script(script_location, bat_location)
add_to_startup(bat_location, icon_location)
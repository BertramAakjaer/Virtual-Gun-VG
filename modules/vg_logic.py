import keyboard, mouse, time, pygame, os
import pygetwindow as gw

from modules.scope_overlay import ImageOverlay


def kill_pressed_program():
    time.sleep(0.1)

    try:
        active_window = gw.getActiveWindow()
    except:
        active_window = None


    if active_window:
        print(f"Killing: {active_window.title}")
        active_window.close()
        time.sleep(0.5)
    else:
        print("No active window found.")

def init_sounds():
    pygame.mixer.init()
    pygame.mixer.set_num_channels(2)  # Set up 2 channels
    
    # Load the sound files
    
    prep_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), '..', 'assets', 'prep_sfx.mp3'))
    shoot_sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), '..', 'assets', 'shoot_sfx.mp3'))
    return prep_sound, shoot_sound

def play_sound(sound):
    # Find first available channel and play
    channel = pygame.mixer.find_channel()
    if channel:
        channel.play(sound)

def run_program():
    prep_sound, shoot_sound = init_sounds()
    
    image_file = os.path.join(os.path.dirname(__file__), '..', 'assets', 'scope.png')
    overlay = ImageOverlay(image_file)
    overlay.running = False

    while True:
        if keyboard.is_pressed('alt+q'):
            overlay.prep_ui()
            play_sound(prep_sound)

        while overlay.running:
            overlay.root.update_idletasks()
            overlay.root.update()

            if keyboard.is_pressed('esc'):
                overlay.running = False
                overlay.stop_following()
            
            if mouse.is_pressed(button='left'):
                overlay.running = False
                overlay.stop_following()
                play_sound(shoot_sound)

                kill_pressed_program()
        

        time.sleep(0.1)  # Reduce CPU usage while waiting
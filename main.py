import tkinter as tk
import pyautogui
from PIL import Image, ImageTk
import keyboard

class ImageOverlay:
    def __init__(self, image_path):
        # Get screen dimensions
        screen_width, screen_height = pyautogui.size()
        target_size = int(screen_width * 0.10)  # 10% of screen width
        
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", "white")
        self.root.bind('<Escape>', self.stop_following)
        
        try:
            # Load and resize image
            original_img = Image.open(image_path)
            ratio = min(target_size / original_img.width, target_size / original_img.height)
            new_size = (int(original_img.width * ratio), int(original_img.height * ratio))
            self.img = original_img.resize(new_size, Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(self.img)
        except Exception as e:
            print(f"Error opening image: {e}")
            self.root.destroy()
            return
        
        self.image_width = self.img.width
        self.image_height = self.img.height

        self.label = tk.Label(self.root, image=self.photo, bg="white", bd=0, highlightthickness=0)
        self.label.pack()
        
        self.running = True
        self.update_position()

    def stop_following(self, event=None):
        print("Stopping overlay...")
        self.running = False
        self.root.destroy()

    def update_position(self):
        if self.running:
            x, y = pyautogui.position()
            self.root.geometry(f"+{x - self.image_width // 2}+{y - self.image_height // 2}")
            self.root.after(10, self.update_position)

def main():
    image_file = r"assets\scope.png"
    overlay = ImageOverlay(image_file)
    
    while overlay.running:
        overlay.root.update_idletasks()
        overlay.root.update()
        if keyboard.is_pressed('esc'):
            overlay.stop_following()

if __name__ == '__main__':
    main()
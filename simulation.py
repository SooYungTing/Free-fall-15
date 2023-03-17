import tkinter as tk
from PIL import Image, ImageTk
import platform


class simulation:
    def __init__(self, master) -> None:
        self.root = master
        self.root.attributes("-fullscreen", True)
        self.root.title("Free-Fall 15 Simulation")

    # Set background image
        bg_image = Image.open("Background.png")
        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

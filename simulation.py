import tkinter as tk

class simulation:
    def __init__(self, master) -> None:
        self.root = master
        self.root.attributes("-fullscreen", True)
        self.root.title("Free-Fall 15 Simulation")
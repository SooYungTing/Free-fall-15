import tkinter as tk
import platform
import sys


class simulation:
    def __init__(self, master) -> None:
        self.root = master
        self.root.attributes("-fullscreen", True)
        self.root.title("Free-Fall 15 Simulation")

os = platform.system()
print(os)


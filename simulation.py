import tkinter as tk
from PIL import Image, ImageTk

class SimulationGUI:
    def __init__(self, master):
        self.root = master
        self.root.attributes("-fullscreen", True)
        self.root.title("Freefall Object Simulation")

        # For centering purposes
        half_x = self.root.winfo_screenwidth() // 2
        half_y = self.root.winfo_screenheight() // 2
    
        inputFrame = tk.Frame(master, bg="#fdfdb7", highlightbackground='black', highlightthickness=1 )
        inputFrame.place(x=self.root.winfo_screenwidth() // 3 + half_x, y=0, width=self.root.winfo_screenwidth() // 3, height=self.root.winfo_screenheight(), bordermode="outside")

        inputlabel = tk.Label(inputFrame, bg="#fdfdb7")
        inputlabel.pack()

        

if __name__ == "__main__":
    root = tk.Tk()
    gui = SimulationGUI(root)
    root.mainloop()

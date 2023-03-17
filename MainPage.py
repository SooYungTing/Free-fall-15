import tkinter as tk
from PIL import Image, ImageTk
import sys

class MainPageGUI:
    def __init__(self, master):
        self.root = master
        self.root.attributes("-fullscreen", True)
        self.root.title("Free-Fall 15 Simulation")

        # Set background image
        bg_image = Image.open("Background.png")
        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        canvas = tk.Canvas(self.root, highlightthickness= 0)
        canvas.create_image(0, 0, image = self.bg_photo, anchor ='nw')
        canvas.pack(fill= "both", expand=True)


        #For centering purposes
        half_x = self.root.winfo_screenwidth() / 2
        half_y = self.root.winfo_screenheight() / 2

        # Create canvas to display welcome message with a transparent background
        welcome_message = "Welcome to the Free-Fall 15 simulation!"
        canvas.create_text(half_x, 50, text=welcome_message, fill="yellow", font=("Times New Roman", 40, "bold"))

        #BUTTON CREATION
        '''
        A dictionary for all the buttons that's involved in the homepage
        Meaning = {Text appearing on button, function button will use}
        Note: Order is bottom to top, hence why 'Quit' is the first since it will be at the bottom 
        '''

        button_function = {
            'Quit' : self.quit_program,
            'Quiz' : self.quit_program,
            'Simulation' : self.open_simulation,
            'Theory' : self.open_theory
        }

        for button, function in button_function.items():
            tk.Button(canvas, text = button, command= function, font=("Times New Roman", 16), width=16, height= 2).pack(pady=10, side= "bottom")

       


    def whatOS() -> str:
        os = sys.platform()

        if os == 'Darwin':
            return 'MacOS'
        elif os == 'Windows':
            return 'Windows'
        else:
            return 'Linux'

    def open_theory(self):
        import theory
        theory = theory.TheoryGUI(self.root)
        theory.mainloop()

    def open_simulation(self):
        import simulation

    def open_quiz(self):
        import quiz

    def quit_program(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    gui = MainPageGUI(root)
    root.mainloop()


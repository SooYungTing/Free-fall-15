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
        # bg_label = tk.Label(self.root, image=self.bg_photo)
        # bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        #For centering purposes
        half_x = self.root.winfo_screenwidth() / 2
        half_y = self.root.winfo_screenheight() / 2


        # Create canvas to display welcome message with a transparent background
        welcome_message = "Welcome to the Free-Fall 15 simulation!"
        canvas.create_text(half_x, 50, text=welcome_message, fill="yellow", font=("Times New Roman", 40, "bold"))
    

        # self.welcome_label = tk.Label(self.root, text=welcome_message, font=("Times New Roman", 40, "bold"), fg="Yellow", bg='transparent')
        # self.welcome_label.pack(pady=20)

    # BUTTON CREATION (Order is weird but it works???)

        button_function = {
            'Quit' : self.quit_program,
            'Quiz' : self.quit_program,
            'Simulation' : self.open_simulation,
            'Theory' : self.open_theory
        }

        for button, function in button_function.items():
            tk.Button(canvas, text = button, command= function, font=("Times New Roman", 16), width=16, height= 2).pack(pady=10, side= "bottom")


        # # Create button to quit program
        # quit_button = tk.Button(canvas, text="Quit", command=self.quit_program, font=("Times New Roman", 16), width=16, height=2)
        # quit_button.pack(pady=10, side= "bottom")

        # # Create button to open quiz file
        # quiz_button = tk.Button(canvas, text="Quiz", command=self.open_quiz, font=("Times New Roman", 16), width=16, height=2)
        # quiz_button.pack(pady=10, side= "bottom")

        # # Create button to open simulation file
        # simulation_button = tk.Button(canvas, text="Simulation", command=self.open_simulation, font=("Times New Roman", 16), width=16, height=2)
        # simulation_button.pack(pady=10, side= "bottom")

        # # Create button to open theory file
        # theory_button = tk.Button(canvas, text="Theory", command=self.open_theory, font=("Times New Roman", 16), width=16, height=2)
        # theory_button.pack(pady=10, side= "bottom")

       


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


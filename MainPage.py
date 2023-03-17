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
        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create label to display welcome message
        welcome_message = "Welcome to the Free-Fall 15 simulation!"
        canvas = tk.Canvas(self.root)
        canvas.create_image(0, 0, image = self.bg_photo, anchor ='nw')
        canvas.create_text(580, 130, text=welcome_message, fill="yellow", font=("Times New Roman", 40, "bold"))
        canvas.pack(fill="both", expand= True)
        # self.welcome_label = tk.Label(self.root, text=welcome_message, font=("Times New Roman", 40, "bold"), fg="Yellow", bg='transparent')
        # self.welcome_label.pack(pady=20)

        # Create button to open theory file
        theory_button = tk.Button(self.root, text="Theory", command=self.open_theory, font=("Times New Roman", 16), width=16, height=2)
        theory_button.pack(pady=10)

        # Create button to open simulation file
        simulation_button = tk.Button(self.root, text="Simulation", command=self.open_simulation, font=("Times New Roman", 16), width=16, height=2)
        simulation_button.pack(pady=10)

        # Create button to open quiz file
        quiz_button = tk.Button(self.root, text="Quiz", command=self.open_quiz, font=("Times New Roman", 16), width=16, height=2)
        quiz_button.pack(pady=10)

        # Create button to quit program
        quit_button = tk.Button(self.root, text="Quit", command=self.quit_program, font=("Times New Roman", 16), width=16, height=2)
        quit_button.pack(pady=10)


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


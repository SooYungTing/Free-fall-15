import tkinter as tk
from PIL import Image, ImageTk
import sys

class MainPageGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes("-fullscreen", True)
        self.title("Free-Fall 15 Simulation")

        # Set background image
        bg_image = Image.open("Background.png")
        bg_image = bg_image.resize((self.winfo_screenwidth(), self.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        canvas = tk.Canvas(self, highlightthickness= 0)
        canvas.create_image(0, 0, image = self.bg_photo, anchor ='nw')
        canvas.pack(fill= "both", expand=True)

        # For centering purposes
        half_x = self.winfo_screenwidth() // 2
        half_y = self.winfo_screenheight() // 2

        # Create canvas to display welcome message with a transparent background
        welcome_message = "Welcome to the Free-Fall 15 simulation!"
        canvas.create_text(half_x, 50, text=welcome_message, fill="yellow", font=("Times New Roman", 40, "bold"))

        # BUTTON CREATION
        '''
        A dictionary for all the buttons that's involved in the homepage
        Meaning = {Text appearing on button, function button will use}
        Note: Order is top to bottom
        Therefore: DO NOT CHANGE THE ORDER
        '''

        button_function = {
            'Theory' : self.open_theory,
            'Simulation' : self.open_simulation,
            'Quiz' : self.open_quiz,
            'Quit' : self.quit_program
        }


        for button, function in button_function.items():
            tk.Button(canvas, text = button, command= function, font=("Times New Roman", 16), width=16, height= 2).place \
                (x = half_x - 100, y = half_y- 100)
            half_y += 100

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
        self.closeCurrentOpenNew(theory.TheoryGUI)

    def open_simulation(self):
        import simulation
        self.closeCurrentOpenNew(simulation.Simulation)
        
    def open_quiz(self):
        import quiz
        self.closeCurrentOpenNew(quiz.FreefallQuiz)
        

    def quit_program(self):
        self.destroy()

    def closeCurrentOpenNew(self, window):
        '''
        Close the current window and open a new window of the specified type.

        Parameters: 
        window (python file) : The Python file containing the new window class to be executed.

        Returns:
        None
        '''

        self.withdraw() # Close the current window
        self.wait_window(window()) # Wait until window is destroyed 
        self.deiconify() # Show the sign in window again
        self.update() # Update the window to ensure it is displayed

if __name__ == "__main__":
    root = MainPageGUI()
    root.mainloop()
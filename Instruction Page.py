import tkinter as tk
from PIL import Image, ImageTk
import sys


class FreeFallGUI:
    def __init__(self, master):
        self.root = master
        self.root.attributes("-fullscreen", True)
        self.root.title("Free-Fall 15 Simulation")

        # Set background image
        bg_image = Image.open("Background.png")
        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        canvas = tk.Canvas(self.root, highlightthickness=0)
        canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')
        canvas.pack(fill="both", expand=True)

        # For centering purposes
        half_x = self.root.winfo_screenwidth() // 2
        half_y = self.root.winfo_screenheight() // 2

        # Create canvas to display welcome message with a transparent background
        welcome_message = "Welcome to the Free-Fall 15 simulation!"
        canvas.create_text(half_x, 50, text=welcome_message, fill="yellow", font=("Times New Roman", 40, "bold"))

        #For positioning the instruction  purposes
        position_x = self.root.winfo_screenwidth() // 10
        position_y = self.root.winfo_screenheight() // 5

        # Create canvas to display instruction title message with a transparent background
        instructions_title = "Instructions:"
        canvas.create_text(position_x, position_y, text=instructions_title, fill="white", font=("Times New Roman", 35, "bold"))

        # Create canvas to display instruction message with a transparent background
        instructions = "- Understand the Theory & Equation section after this page.\n" \
                       "- After understanding, select the temperature, height, object, planet, parachute size to see how it affects the impact of it falling.\n" \
                       "- Click next if you've understood it.\n" \
                       "- Try the quiz to test your knowledge.\n" \
                       "- Submit your answers once you are done and you will be directed to another page with your feedbacks."
        canvas.create_text(half_x, half_y/1.5, text=instructions, fill="white", font=("Times New Roman", 25))

        # Create button to advance to simulation
        self.next_button = tk.Button(self.root, text="Next", font=("Times New Roman", 15), command=self.open_MainPage, width=12, height=2)
        self.next_button.place(relx=0.95, rely=0.95, anchor='se')

    def whatOS() -> str:
        os = sys.platform()

        if os == 'Darwin':
            return 'MacOS'
        elif os == 'Windows':
            return 'Windows'
        else:
            return 'Linux'

    def open_MainPage(self):
        import MainPage
        self.root.destroy()
        root = tk.Tk()
        MainPage.MainPageGUI(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    gui = FreeFallGUI(root)
    root.mainloop()

import tkinter as tk
from PIL import Image, ImageTk
import sys

class Theory2GUI:
    def __init__(self, master):
        self.root = master
        self.root.attributes("-fullscreen", True)
        self.root.title("Theories And Equations")

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

        # Create label to display title message
        welcome_message = "Freefall Theories And Equations"
        canvas.create_text(half_x, 50, text=welcome_message, fill="yellow", font=("Times New Roman", 40, "bold"))

        # For positioning the instruction  purposes
        position_x = self.root.winfo_screenwidth() // 15
        position_y = self.root.winfo_screenheight() // 5

        # Create label for theory 4 title
        theory4_title = "\tTerminal velocity:"
        canvas.create_text(position_x/0.63, position_y, text=theory4_title, fill="white",
                           font=("Times New Roman", 35, "bold"))

        # Create label for theory 4
        theory4 = "- v_t = √((2mg)/(pCdA)) where,\n" \
                  "- v_t is the terminal velocity (m/s)\n" \
                  "- m is the mass (kg)\n" \
                  "- g is the acceleration due to gravity (m/s^2)\n" \
                  "- p is the density of the fluid (kg/m^3)\n" \
                  "- Cd is the drag coefficient\n" \
                  "- A is the cross-sectional area of the object (m^2)"
        canvas.create_text(half_x/2.5, half_y/1.5, text=theory4, fill="white", font=("Times New Roman", 25))

        # Create label for theory 5 title
        theory5_title = "\tAir pressure"
        canvas.create_text(position_x/0.9, position_y/0.42, text=theory5_title, fill="white",
                           font=("Times New Roman", 35, "bold"))

        # Create label for theory 5
        theory5 = "- P = P0 * exp(-h/H) where,\n" \
                  "- P is the air pressure at a certain height (atm)\n" \
                  "- P0 is the air pressure at sea level (atm)\n" \
                  "- h is the height (m)\n" \
                  "- H is the scale height of the atmosphere (m)"
        canvas.create_text(half_x/2.67, half_y/0.85, text=theory5, fill="white", font=("Times New Roman", 25))

        # Create label for theory 6 title
        theory6_title = "\tIdeal Gas Law:"
        canvas.create_text(position_x/0.75, position_y/0.29, text=theory6_title, fill="white",
                           font=("Times New Roman", 35, "bold"))

        # Create label for theory 6
        theory6 = "- P = rhoRT where,\n" \
                  "- rho is the density of the air (kg/m^3)\n" \
                  "- R is the specific gas constant (JK^(-1)mol^(-1)\n" \
                  "- T is the temperature (°C)\n" \
                  "- used to calculate air density"
        canvas.create_text(half_x/2.55, half_y/0.63, text=theory6, fill="white", font=("Times New Roman", 25))

        # Create button to advance to simulation
        self.back_button = tk.Button(self.root, text="Back", font=("Times New Roman", 15), command=self.open_theory,
                                     width=12, height=2)
        self.back_button.place(relx=0.95, rely=0.95, anchor='se')

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
        self.root.destroy()
        root = tk.Tk()
        theory.TheoryGUI(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    gui = Theory2GUI(root)
    root.mainloop()

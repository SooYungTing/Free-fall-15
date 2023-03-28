import tkinter as tk
from PIL import Image, ImageTk
import sys

class TheoryGUI:
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

        # Create label for theory 1 title
        theory1_title = "\tNewton's Second Law:"
        canvas.create_text(position_x/0.5, position_y, text=theory1_title, fill="white",
                           font=("Times New Roman", 35, "bold"))

        # Create label for theory 1
        theory1 = "- F = ma where, \n" \
                  "- F is the resultant force (N)\n" \
                  "- m is the mass of object (kg)\n" \
                  "- a is the acceleration (m/s^2)"
        canvas.create_text(half_x/3, half_y / 1.6, text=theory1, fill="white", font=("Times New Roman", 25))

        # Create label for theory 2 title
        theory2_title = "\tKinetic energy:"
        canvas.create_text(position_x/0.7, position_y/0.5, text=theory2_title, fill="white",
                           font=("Times New Roman", 35, "bold"))

        # Create label for theory 2
        theory2 = "- K.E.  = 1/2 * m * v^2 where,\n" \
                  "- KE is the kinetic energy (J)\n " \
                  "m is the mass (kg)\n " \
                  "v is the velocity (m/s)"
        canvas.create_text(half_x/3, half_y, text=theory2, fill="white", font=("Times New Roman", 25))

        # Create label for theory 3 title
        theory3_title = "\tGravitational potential energy: "
        canvas.create_text(position_x/0.38, position_y/0.34, text=theory3_title, fill="white",
                           font=("Times New Roman", 35, "bold"))

        # Create label for theory 3
        theory3 = "- GPE = mgh where, \n" \
                  "- GPE is the gravitational potential energy (J)\n" \
                  "- m is the mass (kg)\n" \
                  "- g is the acceleration due to gravity (m/s^2)\n" \
                  "- h is the height (m)"
        canvas.create_text(half_x/2.25, half_y/0.71, text=theory3, fill="white", font=("Times New Roman", 25))

        # Create label for theory 4 title
        theory4_title = "Terminal velocity:"
        canvas.create_text(position_x, position_y, text=theory4_title, fill="white",
                           font=("Times New Roman", 35, "bold"))

        # Create button to go back to MainPage
        self.back_button = tk.Button(self.root, text="Back", font=("Times New Roman", 15), command=self.open_MainPage,
                                     width=12, height=2)
        self.back_button.place(relx=0.95, rely=0.95, anchor='se')

        # Create button to go second page of theory
        self.more_button = tk.Button(self.root, text="More", font=("Times New Roman", 15), command=self.open_theory2,
                                     width=12, height=2)
        self.more_button.place(relx=0.85, rely=0.95, anchor='se')

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

    def open_theory2(self):
        import theory2
        self.root.destroy()
        root = tk.Tk()
        theory2.Theory2GUI(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    gui = TheoryGUI(root)
    root.mainloop()

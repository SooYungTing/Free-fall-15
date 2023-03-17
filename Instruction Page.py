import tkinter as tk
from PIL import Image, ImageTk


class FreeFallGUI:
    def __init__(self, master):
        self.root = master
        self.root.attributes("-fullscreen", True)
        self.root.title("Free-Fall 15 Simulation Instructions")

        # Set background image
        bg_image = Image.open("Background.png")
        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create label to display welcome message
        welcome_message = "Welcome to the Free-Fall 15 simulation!"
        self.welcome_label = tk.Label(self.root, text=welcome_message, font=("Times New Roman", 40, "bold"), fg="yellow", bg="#000001")
        self.welcome_label.pack(pady=10)

        # Create label for instructions
        instructions_title = "Instructions:"
        self.instructions_title_label = tk.Label(self.root, text=instructions_title, font=("Times New Roman", 35, "bold"), fg="white", bg="systemTransparent")
        self.instructions_title_label.pack(pady=50, anchor='w')

        # Create label for instructions
        instructions = "- Understand the Theory & Equation section after this page.\n" \
                       "- After understanding, select the temperature, height, object, planet, parachute size to see how it affects the impact of it falling.\n" \
                       "- Click next if you've understood it.\n" \
                       "- Try the quiz to test your knowledge.\n" \
                       "- Submit your answers once you are done and you will be directed to another page with your feedbacks."
        self.instructions_label = tk.Label(self.root, text=instructions, font=("Times New Roman", 25), fg="white", bg="systemTransparent", justify="left")
        self.instructions_label.pack(anchor='w')

        # Create button to advance to simulation
        self.next_button = tk.Button(self.root, text="Next", font=("Times New Roman", 15), command=self.open_MainPage, width=12, height=2)
        self.next_button.place(x=1270, y=self.root.winfo_screenheight()-100)


    def open_MainPage(self):
        import MainPage
        main_page = MainPage.MainPageGUI(self.root)
        main_page.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    gui = FreeFallGUI(root)
    root.mainloop()

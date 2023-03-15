import tkinter as tk
from PIL import Image, ImageTk

class TheoryGUI:
    def __init__(self, master):
        self.root = master
        self.root.attributes("-fullscreen", True)
        self.root.title("Theories And Equations")

        # Set background image
        bg_image = Image.open("Background.png")
        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create label to display welcome message
        welcome_message = "Freefall Theories And Equations"
        self.welcome_label = tk.Label(self.root, text=welcome_message, font=("Times New Roman", 40, "bold"),
                                      fg="Yellow", bg="SystemTransparent")
        self.welcome_label.pack(pady=20)

        # Create label for theory 1 title
        theory1_title = "**"
        self.theory1_title_label = tk.Label(self.root, text=theory1_title,
                                                 font=("Times New Roman", 35, "bold"), fg="white",
                                                 bg="SystemTransparent")
        self.theory1_title_label.pack(pady=50, anchor='w')

        # Create label for theory 1
        theory1 = " ~~ (write some theory)"
        self.theory1_label = tk.Label(self.root, text=theory1, font=("Times New Roman", 25), fg="white",
                                           bg="SystemTransparent", justify="left")
        self.theory1_label.pack(anchor='w')

        # Create button to go back
        self.back_button = tk.Button(self.root, text="Back", font=("Times New Roman", 15), command=self.open_MainPage,
                                     width=12, height=2)
        self.back_button.place(x=1270, y=self.root.winfo_screenheight() - 100)

    def open_MainPage(self):
        import MainPage
        main_page = MainPage.MainPageGUI(self.root)
        main_page.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    gui = TheoryGUI(root)
    root.mainloop()

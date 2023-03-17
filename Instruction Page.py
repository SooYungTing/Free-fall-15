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

        #For centering purposes
        half_x = self.root.winfo_screenwidth() // 2 - 100
        half_y = self.root.winfo_screenheight() // 2 - 100

        #Information about Tk widgets
        
        props = {

            "welcome_label" : {
                "text" : "Welcome to the Free-Fall 15 simulation!",
                "font" : ("Times New Roman", 40, "bold"),
                'fg' : 'yellow',
                "bg" : "#000001",
                "pady" : 10,
                "anchor" : "center",
                
            },
            
            "instructions_title_label" : { 
                "text" : "Instructions:",
                "font" : ("Times New Roman", 35, "bold"),
                "fg" : "yellow",
                "bg" : "black",
                "pady" : 50,
                "anchor" : "w",
            
            },

            "instructions_label" : {
                "text": "- Understand the Theory & Equation section after this page.\n" \
                        "-After understanding, select the temperature, height, object, planet, parachute size to see how it affects the impact of it falling.\n" \
                        "- Click next if you've understood it.\n- Try the quiz to test your knowledge.\n" \
                        "- Submit your answers once you are done and you will be directed to another page with your feedbacks.",
                "font": ("Times New Roman", 25),
                "fg": "white",
                "bg": "black",
                "justify": "left",
                "pady": 0,
                "anchor": "w",
            
            },

            "next_button": {
                "text": "Next",
                "font": ("Times New Roman", 15),
                "command": self.open_MainPage,
                "width": 16,
                "height": 2,
                "anchor": "center",
            }
        }

        # Iterate over the dictionary to create labels and buttons
        for name, attr in props.items():
        # Create a label or button based on the type of the element
            if name.endswith("label"):
                #Label Creation
                tk.Label(self.root, text= attr.get('text', None), font= attr.get('font', None), fg = attr.get('fg', None), bg = attr.get('bg', None), justify = attr.get("justify", None)).pack(pady= attr.get('pady', None), anchor= attr.get('anchor', "center"))
            elif name.endswith("button"):
                #Button Creation
                tk.Button(self.root, text= attr.get("text", None), font = attr.get("font", None), command= attr.get("command", None), width= attr.get("width", 0), height = attr.get("height", 0)).place(x = half_x + 5, y = self.root.winfo_screenheight() - 80)

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

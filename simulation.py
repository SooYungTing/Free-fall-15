import tkinter as tk
from PIL import Image, ImageTk

class SimulationGUI:

    

    def __init__(self, master):
        self.root = master
        self.root.attributes("-fullscreen", True)
        self.root.title("Freefall Object Simulation")

        # For centering purposes
        half_x = self.root.winfo_screenwidth() // 2
        half_y = self.root.winfo_screenheight() // 2

        
        # input frame background
        inputFrame_width = self.root.winfo_screenwidth() // 10
        inputFrame = tk.Frame(master, bg="#fdfdb7", highlightbackground='black', highlightthickness=1 )
        inputFrame.place(x=inputFrame_width + half_x, y=0, width=self.root.winfo_screenwidth() // 2, height=self.root.winfo_screenheight(), bordermode="outside")

        # output frame background (blue)
        outputFrame_blueheight = self.root.winfo_screenheight() // 1.5
        outputFrame_blue = tk.Frame(master, bg="#87cfea")
        outputFrame_blue.place(x=0, y=0, width=half_x + inputFrame_width, height=outputFrame_blueheight, bordermode="outside")

        # output frame background (green)
        outputFrame_green = tk.Frame(master, bg="#90ee90")
        outputFrame_green.place(x=0, y=outputFrame_blueheight, width= half_x + inputFrame_width, height=self.root.winfo_screenheight())

        inputlabel = tk.Label(inputFrame, bg="#fdfdb7", fg="#306f9d", anchor="center", font=("Times", "24", "bold"), text="Input")
        inputlabel.place(relx= 0.425, rely=0.04, anchor='center')

        #input frame widgets
        parachute_box = tk.Frame(inputFrame, bg="white", highlightbackground="black", highlightthickness=1)
        parachute_box.place(relx=0.10, rely= 0.10, relwidth= 0.612, relheight= 0.165)

        def testCommand():
            print("Hello world!")
            
        image = Image.open("parachute-hi.png")
        image1 = image.resize((100, 100))
        photo1 = ImageTk.PhotoImage(image1)
        sm_parachute = tk.Button(parachute_box, image=photo1, command=testCommand)
        sm_parachute.grid(row= 1, column= 0)

        

        image2 = image.resize((60, 60))
        photo2 = ImageTk.PhotoImage(image2)
        button = tk.Button(parachute_box, image=photo2)
        button.grid(row=1, column=1)

    
        



if __name__ == "__main__":
    root = tk.Tk()
    gui = SimulationGUI(root)
    root.mainloop()

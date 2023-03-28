import math
import tkinter as tk
from tkinter import LabelFrame
from PIL import Image, ImageTk

root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Freefall Object Simulation")

img = Image.open("C:\\Users\\Amily\\Downloads\\Picture1.png")
photo = ImageTk.PhotoImage(img)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

label = tk.Label(root, image=photo)

label.place(x=0, y=0, width=screen_width, height=screen_height)

# Define constants
g = {
    "Mercury": 3.7,
    "Venus": 8.87,
    "Earth": 9.81,
    "Mars": 3.71,
    "Moon": 1.62
}
R = 287.058  # Specific gas constant of dry air in J/(kg*K)

# Create the input fields
object_var = tk.StringVar(value="Marshmallow")
object_label = tk.Label(root, text="Object Type:")
object_label.grid(row=0, column=0)
object_menu = tk.OptionMenu(root, object_var, "Marshmallow", "Brick", "Car")
object_menu.grid(row=0, column=1)

image1 = Image.open("C:\\Users\\Amily\\Downloads\\Picture2.png")
image1 = image1.resize((100, 100))
photo1 = ImageTk.PhotoImage(image1)
button = tk.Button(root, image=photo1)
label1 = tk.Label()
label1.grid()
button.grid(row=1, column=0)

image2 = Image.open("C:\\Users\\Amily\\Downloads\\Picture2.png")
image2 = image2.resize((60, 60))
photo2 = ImageTk.PhotoImage(image2)
button = tk.Button(root, image=photo2)
button.grid(row=1, column=1)

height_slider = tk.Scale(root, from_=20, to=-20, orient='vertical', resolution=0.1, label="Height (m)")
height_slider.grid()
temp_slider = tk.Scale(root, from_=20, to=-20, orient='vertical', resolution=0.1, label="Temperature (°C)")
temp_slider.grid()

planet_var = tk.StringVar(value="Earth")
planet_label = tk.Label(root, text="Planet:")
planet_label.grid(row=4, column=0)
planet_menu = tk.OptionMenu(root, planet_var, "Mercury", "Venus", "Earth", "Mars", "Moon")
planet_menu.grid(row=4, column=1)

angle_var = tk.StringVar(value="Rotate 90")
angle_label = tk.Label(root, text="Angle:")
angle_label.grid(row=5, column=0)
angle_menu = tk.OptionMenu(root, angle_var, "Rotate 90", "Rotate 180")
angle_menu.grid(row=5, column=1)

# Create the output labels
velocity_label = tk.Label(root, text="Initial Velocity: ")
velocity_label.grid(row=6, column=0)
velocity_output = tk.Label(root, text="")
velocity_output.grid(row=6, column=1)

terminal_label = tk.Label(root, text="Terminal Velocity: ")
terminal_label.grid(row=7, column=0)
terminal_output = tk.Label(root, text="")
terminal_output.grid(row=7, column=1)

kinetic_label = tk.Label(root, text="Kinetic Energy: ")
kinetic_label.grid(row=8, column=0)
kinetic_output = tk.Label(root, text="")
kinetic_output.grid(row=8, column=1)

potential_label = tk.Label(root, text="Gravitational Potential Energy: ")
potential_label.grid(row=9, column=0)
potential_output = tk.Label(root, text="")
potential_output.grid(row=9, column=1)

impact_label = tk.Label(root, text="Impact Force: ")
impact_label.grid(row=10, column=0)
impact_output = tk.Label(root, text="")
impact_output.grid(row=10, column=1)

# Define a function to calculate and display the results
def calculate_results():
# Get user inputs
    obj = object_var.get()
    air_res = air_resistance_var.get()
    h = int(height_var.get())
    temp = int(temperature_var.get()) + 273.15
    pl = planet_var.get()

# Define air density based on temperature
    P = 101325 * math.exp(-0.00012 * h)  # Define air pressure based on location and altitude
    rho_air = P / (R * temp)

# Define object weight and diameter based on object type
    if obj == "Marshmallow":
        obj_weight = 0.02 * g[pl]
        obj_diameter = 0.05
    elif obj == "Brick":
        obj_weight = 2.07 * g[pl]
        obj_diameter = 0.2
    elif obj == "Car":
        obj_weight = 1200 * g[pl]
        obj_diameter = 1.5
    else:
        result_label.config(text="Invalid object type. Please choose Marshmallow, Brick, or Car.")
        return

    # Calculate initial velocity and gravitational potential energy
    v0 = math.sqrt(2 * g[pl] * h)
    m = obj_weight / g[pl]
    gpe = obj_weight * h

    # Calculate terminal velocity and kinetic energy
    if air_res == "Big":
        Cd = 1.0
    elif air_res == "Small":
        Cd = 0.5
    elif air_res == 'Disable':
        Cd = 1e-16

    # Calculate terminal velocity and kinetic energy
    A = math.pi * (obj_diameter / 2) ** 2
    terminal_v = math.sqrt((2 * m * g[pl]) / (Cd * rho_air * A))
    ke = 0.5 * m * terminal_v ** 2

    # Calculate impact force
    ang = angle_var.get()
    if ang == "Rotate 90":
        impact_time = v0 / g[pl] # Use initial velocity instead of terminal velocity
        impact_force = (m * g[pl] + ke / terminal_v) / impact_time
    else:
        impact_force = m * g[pl]

    # Update the result label with the calculated values
    result_label.config(text=f"Initial velocity: {v0:.2f} m/s\n"
                              f"Terminal velocity: {terminal_v:.2f} m/s\n"
                              f"Kinetic energy: {ke:.2f} J\n"
                              f"Gravitational potential energy: {gpe:.2f} J\n"
                              f"Impact force: {impact_force:.2f} N")
    window = Tk()
    window.title("Freefall Object Simulation")


    #Create input frames
    input_frame1 = LabelFrame(window, text="Object Type")
    input_frame1.pack(fill="both", expand="yes", padx=20, pady=10)

    input_frame2 = LabelFrame(window, text="Air Resistance")
    input_frame2.pack(fill="both", expand="yes", padx=20, pady=10)

    input_frame3 = LabelFrame(window, text="Height and Temperature")
    input_frame3.pack(fill="both", expand="yes", padx=20, pady=10)

    input_frame4 = LabelFrame(window, text="Planet")
    input_frame4.pack(fill="both", expand="yes", padx=20, pady=10)

    input_frame5 = LabelFrame(window, text="Angle")
    input_frame5.pack(fill="both", expand="yes", padx=20, pady=10)
    input_frame5.pack(side="top", fill="x", padx=10, pady=5)




    # Add a button to calculate the results
    calculate_button = tk.Button(root, text="Calculate", command=calculate_results)
    calculate_button.pack(side="top", pady=10)

    # Add a label to display the results
    result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
    result_label.pack(side="top", padx=10, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()


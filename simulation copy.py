import math
import tkinter as tk
from tkinter import LabelFrame, messagebox
import tkinter.messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("Freefall Object Simulation")

# img = Image.open("Simulation Background.png")
# photo = ImageTk.PhotoImage(img)

# Logic

# Logic 

# Define constants
global Cd, ang, temp, h, pl
Cd = 1.0
ang = 0
impact_time = 0
g = {
    "Mercury": 3.7,
    "Venus": 8.87,
    "Earth": 9.81,
    "Mars": 3.71,
    "Moon": 1.62
}
R = 287.058  # Specific gas constant of dry air in J/(kg*K)

#Get inputs
def calcImpact_time():
    global impact_time
    impact_time = v0 / g[pl]


def getInput():
    global obj, h, temp, pl, obj_weight
    obj = obj = object_var.get()
    h = int(height_slider.get())
    temp = int(temp_slider.get()) + 273.15
    pl = planet_var.get()
    object_validation()

#Object Validation
def object_validation():
    if obj not in ("Marshmallow", "Car", "Brick"):
        tkinter.messagebox.showerror(title='Object Error', message="No chosen object: Select the type of objects available before proceeding")
    else:
        global obj_weight, obj_diameter
        if obj == "Marshmallow":
            obj_weight = 0.02 * g[pl]
            obj_diameter = 0.05
        elif obj == "Brick":
            obj_weight = 2.07 * g[pl]
            obj_diameter = 0.2
        elif obj == "Car":
            obj_weight = 1200 * g[pl]
            obj_diameter = 1.5

# Define air density based on temperature
def getAirPressure():
    global rho_air
    P = 101325 * math.exp(-0.00012 * h)  # Define air pressure based on location and altitude
    rho_air = P / (R * temp)

def getGPE():
    # Calculate initial velocity and gravitational potential energy
    global v0, m, gpe
    v0 = math.sqrt(2 * g[pl] * h)
    m = obj_weight / g[pl]
    gpe = obj_weight * h


def getAcceleration():
    global acc
    if impact_time == 0:
        acc = 0
    else:
        acc = v0 / impact_time

def getKE():
    # Calculate terminal velocity and kinetic energy
    global terminal_v, ke
    A = math.pi * (obj_diameter / 2) ** 2
    terminal_v = math.sqrt((2 * m * g[pl]) / (Cd * rho_air * A))
    ke = 0.5 * m * terminal_v ** 2

def getImpactForce():
    global impact_force, impact_time
    # Calculate impact force
    if ang == 90:
        impact_time = v0 / g[pl] # Use initial velocity instead of terminal velocity
        impact_force = (m * g[pl] + ke / terminal_v) / impact_time
    else:
        impact_force = m * g[pl]

#Button Functions
def sm_parachute_command():
    Cd = 0.5
    tkinter.messagebox.showinfo(title="Parachute Choice", message="Small parachute has been selected")


def lg_parachute_command():
    Cd = 1.0
    tkinter.messagebox.showinfo(title="Parachute Choice", message="Large parachute has been selected")

def disable_air_resistance_command():
    Cd = 1e-16
    tkinter.messagebox.showinfo(title="Parachute Choice", message="Air resistance has been disabled")

def rotation_command():
    ang += 90
    if ang == 360:
        ang = 0

def reset_command():
    Cd = 0
    ang = 0
    temp = 0
    h = 100
    pl = 0
    height_slider.set(550)
    temp_slider.set(0.0)
    object_var.set("Object")
    planet_var.set("Earth")


def back_command():
    root.destroy()

def start_command():
    global v0
    getInput()
    getGPE()
    v0 = math.sqrt(2 * g[pl] * h)
    calcImpact_time()
    object_validation()
    getAirPressure()
    getAcceleration()
    getKE()
    getImpactForce()
    initial_velocity_value.config(text=f"{v0:.2f}")
    acc_value.config(text=f"{acc:.2f}")
    ke_value.config(text=f"{ke:.2f}")
    gpe_value.config(text=f"{gpe:.2f}")
    impact_force_value.config(text=f"{impact_force:.2f}")


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

inputFrame_bg = "#fdfdb7"
outputFrame_bg_sky = "#87cfea"
outputFrame_bg_land = "#90ee90"
textBg = "#306f9d"

inputFrame = tk.Frame(root, highlightbackground= "black", highlightthickness=1, bg=inputFrame_bg)
inputFrame.place(x=screen_width // 10 + screen_width // 2, y= 0 , width=screen_width, height=screen_height)

outputFrame_sky = tk.Frame(root, bg=outputFrame_bg_sky)
outputFrame_sky.place(x=0, y=0, width= screen_width // 10 + screen_width // 2, height= screen_height // 1.6)

outputFrame_land = tk.Frame(root, bg=outputFrame_bg_land)
outputFrame_land.place(x=0, y=screen_height // 1.6, width= screen_width // 10 + screen_width // 2, height= screen_height)

inputText = tk.Label(inputFrame, text="Input", font=("Times New Roman", "23", "bold"), bg=inputFrame_bg, fg=textBg)
inputText.place(relx= 0.185, rely= 0.010)

outputText = tk.Label(outputFrame_sky, text="Output", font=("Times New Roman", "23", "bold"), bg=outputFrame_bg_sky, fg=textBg)
outputText.place(relx= 0.43, rely= 0.020)

parachute_box = tk.Frame(inputFrame, highlightbackground="black", highlightthickness=1)
parachute_box.place(relx=0.0525, rely= 0.1, relwidth= 0.3, relheight= 0.14)

image = Image.open("parachute-hi.png")

#small parachute
image2 = image.resize((60, 60))
photo2 = ImageTk.PhotoImage(image2)
sm_parachute = tk.Button(parachute_box, relief='ridge')
sm_parachute.photo = photo2
sm_parachute.config(image=photo2)
sm_parachute.grid(row=2, column= 2, padx=50)

#large parachute
image1 = image.resize((100, 100))
photo1 = ImageTk.PhotoImage(image1)
lg_parachute = tk.Button(parachute_box, relief="ridge")
lg_parachute.photo = photo1
lg_parachute.config(image=photo1)
# lg_parachute.place(relx=0.1, rely=0.12)
# label1 = tk.Label(parachute_box)
# label1.place(relx=0.1)
lg_parachute.grid(row=2, column=1, padx=90, pady= 20)

#temperature scale
temp_slider = tk.Scale(inputFrame, from_=20, to=-20, orient='vertical', resolution=0.5, sliderlength=50, length=400, width= 50, bg=inputFrame_bg, bd=2, highlightthickness=0, highlightcolor="#d7d7d7")
temp_slider.set(0.0)
temp_label = tk.Label(inputFrame, text="Temperature (°C)", font=("Times New Roman", "14"), bg=inputFrame_bg, fg="black")

temp_slider.place(relx= 0.03, rely=0.35)
temp_label.place(relx=0.025, rely=0.32 )  


#height scale
height_slider = tk.Scale(inputFrame, from_=1000, to=100, orient='vertical', resolution=1,  sliderlength= 50, length=400, width=50, bg=inputFrame_bg, bd=2, highlightthickness=0, highlightcolor="#d7d7d7")
height_slider.set(550)
height_label = tk.Label(inputFrame, text="Height (m)", font=("Times New Roman", "14"), bg=inputFrame_bg, fg="black")
# label="Height (m)",
height_slider.place(relx=0.11, rely=0.35)
height_label.place(relx=0.12, rely=0.32 )  

# Object type
object_var = tk.StringVar(value="Object")
object_menu = tk.OptionMenu(inputFrame, object_var, "Marshmallow", "Brick", "Car")
object_menu.config(font=('Times New Roman', 18))
object_menu.place(relx=0.22, rely=0.36, relwidth=0.15)

# Planet Type
planet_var = tk.StringVar(value="Earth")
planet_menu = tk.OptionMenu(inputFrame, planet_var, "Mercury", "Venus", "Earth", "Mars", "Moon")
planet_menu.config(font=('Times New Roman', 18))
planet_menu.place(relx=0.22, rely=0.46, relwidth=0.15)

# Rotation Button
rotation_button = tk.Button(inputFrame, text="Rotate 90°", font=("Times New Roman", 18))
rotation_button.place(relx=0.22, rely=0.56, relwidth=0.15)

# Disable Air Resistance Button
no_air_res_button = tk.Button(inputFrame, text="Disable Air Resistance", font=("Times New Roman", 18))
no_air_res_button.place(relx=0.22, rely=0.66, relwidth=0.15)

#Reset Button
reset_button = tk.Button(inputFrame, text="Reset", font=("Times New Roman", 20), bg="#d7d7d7", command=reset_command)
reset_button.place(relx=0.02, rely= 0.94, relwidth=0.08)

#Back Button
back_button = tk.Button(inputFrame, text="Back", font=("Times New Roman", 20), bg="#d7d7d7", command=back_command)
back_button.place(relx=0.21, rely= 0.94, relwidth=0.08)

#Start Button
start_button = tk.Button(inputFrame, text="Start", font=("Times New Roman", 20), bg="#d7d7d7", command=start_command)
start_button.place(relx=0.3, rely= 0.94, relwidth=0.08)


#Outputs

#Initial Velocity 
initial_velocity_frame = tk.Frame(outputFrame_land, bg=outputFrame_bg_land)
text = tk.Label(initial_velocity_frame, text="Velocity:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
initial_velocity_value_frame = tk.Frame(initial_velocity_frame, highlightbackground= "black", highlightthickness=1, bg="white", width= 100, height=25)
initial_velocity_value = tk.Label(initial_velocity_value_frame, text="0.00", font=("Times New Roman", 18))
unit = tk.Label(initial_velocity_frame, text=" m/s", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
text.grid(row=1, column=0)
initial_velocity_value_frame.grid(row=1, column=1)
initial_velocity_value.pack()
unit.grid(row=1, column=2)
initial_velocity_frame.place(relx=0.03, rely= 0.25, relheight= 0.033, relwidth=0.23)

#Kinetic Energy 
ke_frame = tk.Frame(outputFrame_land, bg=outputFrame_bg_land)
text = tk.Label(ke_frame, text="Kinetic Energy:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
ke_value_frame = tk.Frame(ke_frame, highlightbackground= "black", highlightthickness=1, bg="white", width= 100, height=25)
ke_value = tk.Label(ke_value_frame, text="0.00", font=("Times New Roman", 18))
unit = tk.Label(ke_frame, text=" J", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
text.grid(row=1, column=0)
ke_value_frame.grid(row=1, column=1)
ke_value.pack()
unit.grid(row=1, column=2)
ke_frame.place(relx=0.35, rely= 0.25, relheight= 0.033, relwidth=0.268)

#Impact Force
impact_force_frame = tk.Frame(outputFrame_land, bg=outputFrame_bg_land)
text = tk.Label(impact_force_frame, text="Impact Force:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
impactforce_value_frame = tk.Frame(impact_force_frame, highlightbackground= "black", highlightthickness=1, bg="white", width= 100, height=25)
impact_force_value = tk.Label(impactforce_value_frame, text="0.00", font=("Times New Roman", 18))
unit = tk.Label(impact_force_frame, text=" N", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
text.grid(row=1, column=0)
impactforce_value_frame.grid(row=1, column=1)
impact_force_value.pack()
unit.grid(row=1, column=2)
impact_force_frame.place(relx=0.7, rely= 0.25, relheight= 0.033, relwidth=0.265)

#Gravitational Potential Energy
gpe_frame = tk.Frame(outputFrame_land, bg=outputFrame_bg_land)
text = tk.Label(gpe_frame, text="G.P.E:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
gpe_value_frame = tk.Frame(gpe_frame, highlightbackground= "black", highlightthickness=1, bg="white", width= 100, height=25)
gpe_value = tk.Label(gpe_value_frame, text="0.00", font=("Times New Roman", 18))
unit = tk.Label(gpe_frame, text=" J", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
text.grid(row=2, column=0)
gpe_value_frame.grid(row=2, column=1)
gpe_value.pack()
unit.grid(row=2, column=2)
gpe_frame.place(relx=0.434, rely= 0.3, relheight= 0.033, relwidth=0.139)

#Acceleration
acceleration_frame = tk.Frame(outputFrame_land, bg=outputFrame_bg_land)
text = tk.Label(acceleration_frame, text="Acceleration:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
acc_value_frame = tk.Frame(acceleration_frame, highlightbackground= "black", highlightthickness=1, bg="white", width= 100, height=25)
acc_value = tk.Label(acc_value_frame, text="0.00", font=("Times New Roman", 18))
unit = tk.Label(acceleration_frame, text=" m/s^2", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
text.grid(row=2, column=0)
acc_value_frame.grid(row=2, column=1)
acc_value.pack()
unit.grid(row=2, column=2)
acceleration_frame.place(relx=0.03, rely= 0.3, relheight= 0.033, relwidth=0.293)

root.mainloop()
gpe_value.config(text=f"{gpe:.2f} J")
impact_force_value.config(text=f"{impact_force:.2f} J")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

inputFrame_bg = "#fdfdb7"
outputFrame_bg_sky = "#87cfea"
outputFrame_bg_land = "#90ee90"
textBg = "#306f9d"

inputFrame = tk.Frame(root, highlightbackground= "black", highlightthickness=1, bg=inputFrame_bg)
inputFrame.place(x=screen_width // 10 + screen_width // 2, y= 0 , width=screen_width, height=screen_height)

outputFrame_sky = tk.Frame(root, bg=outputFrame_bg_sky)
outputFrame_sky.place(x=0, y=0, width= screen_width // 10 + screen_width // 2, height= screen_height // 1.6)

outputFrame_land = tk.Frame(root, bg=outputFrame_bg_land)
outputFrame_land.place(x=0, y=screen_height // 1.6, width= screen_width // 10 + screen_width // 2, height= screen_height)

inputText = tk.Label(inputFrame, text="Input", font=("Times New Roman", "23", "bold"), bg=inputFrame_bg, fg=textBg)
inputText.place(relx= 0.185, rely= 0.010)

outputText = tk.Label(outputFrame_sky, text="Output", font=("Times New Roman", "23", "bold"), bg=outputFrame_bg_sky, fg=textBg)
outputText.place(relx= 0.43, rely= 0.020)

parachute_box = tk.Frame(inputFrame, highlightbackground="black", highlightthickness=1)
parachute_box.place(relx=0.0525, rely= 0.1, relwidth= 0.3, relheight= 0.14)

image = Image.open("parachute-hi.png")

#small parachute
image2 = image.resize((60, 60))
photo2 = ImageTk.PhotoImage(image2)
sm_parachute = tk.Button(parachute_box, relief='ridge')
sm_parachute.photo = photo2
sm_parachute.config(image=photo2)
sm_parachute.grid(row=2, column= 2, padx=50)

#large parachute
image1 = image.resize((100, 100))
photo1 = ImageTk.PhotoImage(image1)
lg_parachute = tk.Button(parachute_box, relief="ridge")
lg_parachute.photo = photo1
lg_parachute.config(image=photo1)
# lg_parachute.place(relx=0.1, rely=0.12)
# label1 = tk.Label(parachute_box)
# label1.place(relx=0.1)
lg_parachute.grid(row=2, column=1, padx=90, pady= 20)

#temperature scale
temp_slider = tk.Scale(inputFrame, from_=20, to=-20, orient='vertical', resolution=0.5, sliderlength=50, length=400, width= 50, bg=inputFrame_bg, bd=2, highlightthickness=0, highlightcolor="#d7d7d7")
temp_slider.set(0.0)
temp_label = tk.Label(inputFrame, text="Temperature (°C)", font=("Times New Roman", "14"), bg=inputFrame_bg, fg="black")

temp_slider.place(relx= 0.03, rely=0.35)
temp_label.place(relx=0.025, rely=0.32 )


#height scale
height_slider = tk.Scale(inputFrame, from_=1000, to=100, orient='vertical', resolution=1,  sliderlength= 50, length=400, width=50, bg=inputFrame_bg, bd=2, highlightthickness=0, highlightcolor="#d7d7d7")
height_slider.set(550)
height_label = tk.Label(inputFrame, text="Height (m)", font=("Times New Roman", "14"), bg=inputFrame_bg, fg="black")
# label="Height (m)",
height_slider.place(relx=0.11, rely=0.35)
height_label.place(relx=0.12, rely=0.32 )

# Object type
object_var = tk.StringVar(value="Object")
object_menu = tk.OptionMenu(inputFrame, object_var, "Marshmallow", "Brick", "Car")
object_menu.config(font=('Times New Roman', 18))
object_menu.place(relx=0.22, rely=0.36, relwidth=0.15)

# Planet Type
planet_var = tk.StringVar(value="Earth")
planet_menu = tk.OptionMenu(inputFrame, planet_var, "Mercury", "Venus", "Earth", "Mars", "Moon")
planet_menu.config(font=('Times New Roman', 18))
planet_menu.place(relx=0.22, rely=0.46, relwidth=0.15)

# Rotation Button
rotation_button = tk.Button(inputFrame, text="Rotate 90°", font=("Times New Roman", 18))
rotation_button.place(relx=0.22, rely=0.56, relwidth=0.15)

# Disable Air Resistance Button
no_air_res_button = tk.Button(inputFrame, text="Disable Air Resistance", font=("Times New Roman", 18))
no_air_res_button.place(relx=0.22, rely=0.66, relwidth=0.15)

#Reset Button
reset_button = tk.Button(inputFrame, text="Reset", font=("Times New Roman", 20), bg="#d7d7d7", command=reset_command)
reset_button.place(relx=0.02, rely= 0.94, relwidth=0.08)

#Back Button
back_button = tk.Button(inputFrame, text="Back", font=("Times New Roman", 20), bg="#d7d7d7", command=back_command)
back_button.place(relx=0.21, rely= 0.94, relwidth=0.08)

#Start Button
start_button = tk.Button(inputFrame, text="Start", font=("Times New Roman", 20), bg="#d7d7d7", command=start_command)
start_button.place(relx=0.3, rely= 0.94, relwidth=0.08)

sm_parachute.config(command=sm_parachute_command)
lg_parachute.config(command=lg_parachute_command)
rotation_button.config(command=rotation_command)
no_air_res_button.config(command=disable_air_resistance_command)

#Outputs

#Initial Velocity
initial_velocity_frame = tk.Frame(outputFrame_land, bg=outputFrame_bg_land)
text = tk.Label(initial_velocity_frame, text="Velocity:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
initial_velocity_value_frame = tk.Frame(initial_velocity_frame, highlightbackground= "black", highlightthickness=1, bg="white", width= 100, height=25)
initial_velocity_value = tk.Label(initial_velocity_value_frame, text="0.00", font=("Times New Roman", 18))
unit = tk.Label(initial_velocity_frame, text=" m/s", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
text.grid(row=1, column=0)
initial_velocity_value_frame.grid(row=1, column=1)
initial_velocity_value.pack()
unit.grid(row=1, column=2)
initial_velocity_frame.place(relx=0.03, rely= 0.25, relheight= 0.033, relwidth=0.23)

#Kinetic Energy
ke_frame = tk.Frame(outputFrame_land, bg=outputFrame_bg_land)
text = tk.Label(ke_frame, text="Kinetic Energy:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
ke_value_frame = tk.Frame(ke_frame, highlightbackground= "black", highlightthickness=1, bg="white", width= 100, height=25)
ke_value = tk.Label(ke_value_frame, text="0.00", font=("Times New Roman", 18))
unit = tk.Label(ke_frame, text=" J", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
text.grid(row=1, column=0)
ke_value_frame.grid(row=1, column=1)
ke_value.pack()
unit.grid(row=1, column=2)
ke_frame.place(relx=0.35, rely= 0.25, relheight= 0.033, relwidth=0.268)

#Impact Force
impact_force_frame = tk.Frame(outputFrame_land, bg=outputFrame_bg_land)
text = tk.Label(impact_force_frame, text="Impact Force:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
impactforce_value_frame = tk.Frame(impact_force_frame, highlightbackground= "black", highlightthickness=1, bg="white", width= 100, height=25)
impact_force_value = tk.Label(impactforce_value_frame, text="0.00", font=("Times New Roman", 18))
unit = tk.Label(impact_force_frame, text=" N", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
text.grid(row=1, column=0)
impactforce_value_frame.grid(row=1, column=1)
impact_force_value.pack()
unit.grid(row=1, column=2)
impact_force_frame.place(relx=0.7, rely= 0.25, relheight= 0.033, relwidth=0.265)

#Gravitational Potential Energy
gpe_frame = tk.Frame(outputFrame_land, bg=outputFrame_bg_land)
text = tk.Label(gpe_frame, text="G.P.E:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
gpe_value_frame = tk.Frame(gpe_frame, highlightbackground= "black", highlightthickness=1, bg="white", width= 100, height=25)
gpe_value = tk.Label(gpe_value_frame, text="0.00", font=("Times New Roman", 18))
unit = tk.Label(gpe_frame, text=" J", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
text.grid(row=2, column=0)
gpe_value_frame.grid(row=2, column=1)
gpe_value.pack()
unit.grid(row=2, column=2)
gpe_frame.place(relx=0.434, rely= 0.3, relheight= 0.033, relwidth=0.139)

#Acceleration
acceleration_frame = tk.Frame(outputFrame_land, bg=outputFrame_bg_land)
text = tk.Label(acceleration_frame, text="Acceleration:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
acc_value_frame = tk.Frame(acceleration_frame, highlightbackground= "black", highlightthickness=1, bg="white", width= 100, height=25)
acc_value = tk.Label(acc_value_frame, text="0.00", font=("Times New Roman", 18))
unit = tk.Label(acceleration_frame, text=" m/s^2", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg="black")
text.grid(row=2, column=0)
acc_value_frame.grid(row=2, column=1)
acc_value.pack()
unit.grid(row=2, column=2)
acceleration_frame.place(relx=0.03, rely= 0.3, relheight= 0.033, relwidth=0.293)

root.mainloop()
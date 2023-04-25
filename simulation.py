import math, time
import tkinter as tk
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk

class Simulation(tk.Toplevel):
    def __init__(self) -> None:
        # configure the root window
        super().__init__()
        self.attributes('-fullscreen', True)
        self.title('Freefall Object Simulation')

        # Initialise Variables
        self.Cd = 1
        self.ang = 0
        self.temp = 0
        self.h = 0
        self.pl = 0
        self.impact_time = 0
        self.R = 287.058 # Specific gas constant of dry air in J/(kg*K)
        self.g = {
            "Mercury": 3.7,
            "Venus": 8.87,
            "Earth": 9.81,
            "Mars": 3.71,
            "Moon": 1.62
        }
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Background colors for each frame
        inputFrame_bg = '#13293d' 
        outputFrame_bg_sky = '#1f487e'
        outputFrame_bg_land = '#1d3461'
        textBg = '#3fc1c0'
        self.inputFrame = tk.Frame(self, highlightbackground= "black", highlightthickness=1, bg=inputFrame_bg)
        self.inputFrame.place(x=screen_width // 10 + screen_width // 2, y= 0 , width=screen_width, height=screen_height)

        self.outputFrame_sky = tk.Frame(self, bg=outputFrame_bg_sky)
        self.outputFrame_sky.place(x=0, y=0, width= screen_width // 10 + screen_width // 2, height= screen_height // 1.6)

        self.outputFrame_land = tk.Frame(self, bg=outputFrame_bg_land)
        self.outputFrame_land.place(x=0, y=screen_height // 1.6, width= screen_width // 10 + screen_width // 2, height= screen_height)

        self.inputText = tk.Label(self.inputFrame, text="Input", font=("Times New Roman", "23", "bold"), bg=inputFrame_bg, fg=textBg)
        self.inputText.place(relx= 0.185, rely= 0.010)

        self.outputText = tk.Label(self.outputFrame_sky, text="Output", font=("Times New Roman", "23", "bold"), bg=outputFrame_bg_sky, fg=textBg)
        self.outputText.place(relx= 0.43, rely= 0.020)

        self.parachute_box = tk.Frame(self.inputFrame, highlightbackground="black", highlightthickness=1)
        self.parachute_box.place(relx=0.0525, rely= 0.1, relwidth= 0.3, relheight= 0.14)

        image = Image.open("parachute-hi.png")

        #small parachute
        image2 = image.resize((60, 60))
        photo2 = ImageTk.PhotoImage(image2)
        sm_parachute = tk.Button(self.parachute_box, relief='ridge', command=self.sm_parachute_command)
        sm_parachute.photo = photo2
        sm_parachute.config(image=photo2)
        sm_parachute.grid(row=2, column= 2, padx=50)

        #large parachute
        image1 = image.resize((100, 100))
        photo1 = ImageTk.PhotoImage(image1)
        self.lg_parachute = tk.Button(self.parachute_box, relief="ridge", command=self.lg_parachute_command)
        self.lg_parachute.photo = photo1
        self.lg_parachute.config(image=photo1)
        self.lg_parachute.grid(row=2, column=1, padx=90, pady= 20)

        #temperature scale
        self.temp_slider = tk.Scale(self.inputFrame, from_=20, to=-20, orient='vertical', resolution=0.5, sliderlength=50, length=400, width= 50, bg=inputFrame_bg, bd=2, highlightthickness=0, highlightcolor="#d7d7d7", fg=textBg)
        self.temp_slider.set(0.0)
        self.temp_label = tk.Label(self.inputFrame, text="Temperature (°C)", font=("Times New Roman", "14"), bg=inputFrame_bg, fg=textBg)

        self.temp_slider.place(relx= 0.03, rely=0.35)
        self.temp_label.place(relx=0.025, rely=0.32 )


        #height scale
        self.height_slider = tk.Scale(self.inputFrame, from_=1000, to=100, orient='vertical', resolution=1,  sliderlength= 50, length=400, width=50, bg=inputFrame_bg, bd=2, highlightthickness=0, highlightcolor="#d7d7d7", fg= textBg)
        self.height_slider.set(550)
        height_label = tk.Label(self.inputFrame, text="Height (m)", font=("Times New Roman", "14"), bg=inputFrame_bg, fg=textBg)
        self.height_slider.place(relx=0.11, rely=0.35)
        height_label.place(relx=0.12, rely=0.32 )

        # Object type
        self.object_var = tk.StringVar(value="Object")
        self.object_menu = tk.OptionMenu(self.inputFrame, self.object_var, "Marshmallow", "Brick", "Car")
        self.object_menu.config(font=('Times New Roman', 18))
        self.object_menu.place(relx=0.22, rely=0.36, relwidth=0.15)

        # Planet Type
        self.planet_var = tk.StringVar(value="Earth")
        self.planet_menu = tk.OptionMenu(self.inputFrame, self.planet_var, "Mercury", "Venus", "Earth", "Mars", "Moon")
        self.planet_menu.config(font=('Times New Roman', 18))
        self.planet_menu.place(relx=0.22, rely=0.46, relwidth=0.15)

        # Input buttons
        all_input_buttons = [
            # Rotation button
            {'text' : 'Rotate 90°', 'font' : ('Times new Roman', 18), 'command' : self.rotation_command, 'relx' : 0.22, 'rely' : 0.56, 'relwidth' : 0.15}, 
            # Disable air resistance button
            {'text' : 'Disable Air Resistance', 'font' : ('Times new Roman', 18), 'command' : self.disable_air_resistance_command, 'relx' : 0.22, 'rely' : 0.66, 'relwidth' : 0.15},
            # Instruction guide button
            {'text' : 'Instruction Guide', 'font' : ('Times new Roman', 18), 'command' : self.open_instruction_page, 'relx' : 0.22, 'rely' : 0.76, 'relwidth' : 0.15},
            # Reset button
            {'text' : 'Reset', 'font' : ('Times new Roman', 20), 'command' : self.reset_command, 'relx' : 0.02, 'rely' : 0.94, 'relwidth' : 0.08},
            # Back button
            {'text' : 'Back', 'font' : ('Times new Roman', 20), 'command' : self.back_command, 'relx' : 0.21, 'rely' : 0.94, 'relwidth' : 0.08},
            # Start button
            {'text' : 'Start', 'font' : ('Times new Roman', 20), 'command' : self.start_command, 'relx' : 0.3, 'rely' : 0.94, 'relwidth' : 0.08},
        ]

        for properties in all_input_buttons:
            button = tk.Button(self.inputFrame, text=properties['text'], font=properties['font'], command=properties['command'])
            button.place(relx=properties['relx'], rely=properties['rely'], relwidth=properties['relwidth'])
            
        #Outputs

        #Initial Velocity
        self.initial_velocity_frame = tk.Frame(self.outputFrame_land, bg=outputFrame_bg_land)
        text = tk.Label(self.initial_velocity_frame, text="Velocity:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg=textBg)
        self.initial_velocity_value_frame = tk.Frame(self.initial_velocity_frame, highlightbackground= "#B0A3F5", highlightthickness=2, bg="gray", width= 100, height=25)
        self.initial_velocity_value = tk.Label(self.initial_velocity_value_frame, text="0.00", font=("Times New Roman", 18))
        unit = tk.Label(self.initial_velocity_frame, text=" m/s", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg=textBg)
        text.grid(row=1, column=0)
        self.initial_velocity_value_frame.grid(row=1, column=1)
        self.initial_velocity_value.pack()
        unit.grid(row=1, column=2)
        self.initial_velocity_frame.place(relx=0.03, rely= 0.25, relheight= 0.033, relwidth=0.23)

        #Kinetic Energy
        self.ke_frame = tk.Frame(self.outputFrame_land, bg=outputFrame_bg_land)
        text = tk.Label(self.ke_frame, text="Kinetic Energy:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg=textBg)
        self.ke_value_frame = tk.Frame(self.ke_frame, highlightbackground= "#B0A3F5", highlightthickness=2, bg="gray", width= 100, height=25)
        self.ke_value = tk.Label(self.ke_value_frame, text="0.00", font=("Times New Roman", 18))
        unit = tk.Label(self.ke_frame, text=" J", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg=textBg)
        text.grid(row=1, column=0)
        self.ke_value_frame.grid(row=1, column=1)
        self.ke_value.pack()
        unit.grid(row=1, column=2)
        self.ke_frame.place(relx=0.35, rely= 0.25, relheight= 0.033, relwidth=0.268)

        #Impact Force
        self.impact_force_frame = tk.Frame(self.outputFrame_land, bg=outputFrame_bg_land)
        text = tk.Label(self.impact_force_frame, text="Impact Force:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg=textBg)
        self.impactforce_value_frame = tk.Frame(self.impact_force_frame, highlightbackground= "#B0A3F5", highlightthickness=2, bg="gray", width= 100, height=25)
        self.impact_force_value = tk.Label(self.impactforce_value_frame, text="0.00", font=("Times New Roman", 18))
        unit = tk.Label(self.impact_force_frame, text=" N", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg=textBg)
        text.grid(row=1, column=0)
        self.impactforce_value_frame.grid(row=1, column=1)
        self.impact_force_value.pack()
        unit.grid(row=1, column=2)
        self.impact_force_frame.place(relx=0.7, rely= 0.25, relheight= 0.033, relwidth=0.265)

        #Gravitational Potential Energy
        self.gpe_frame = tk.Frame(self.outputFrame_land, bg=outputFrame_bg_land)
        text = tk.Label(self.gpe_frame, text="G.P.E:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg=textBg)
        self.gpe_value_frame = tk.Frame(self.gpe_frame, highlightbackground= "#B0A3F5", highlightthickness=2, bg="gray", width= 100, height=25)
        self.gpe_value = tk.Label(self.gpe_value_frame, text="0.00", font=("Times New Roman", 18))
        unit = tk.Label(self.gpe_frame, text=" J", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg=textBg)
        text.grid(row=2, column=0)
        self.gpe_value_frame.grid(row=2, column=1)
        self.gpe_value.pack()
        unit.grid(row=2, column=2)
        self.gpe_frame.place(relx=0.434, rely= 0.3, relheight= 0.033, relwidth=0.139)

        #Acceleration
        self.acceleration_frame = tk.Frame(self.outputFrame_land, bg=outputFrame_bg_land)
        text = tk.Label(self.acceleration_frame, text="Acceleration:", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg=textBg)
        self.acc_value_frame = tk.Frame(self.acceleration_frame, highlightbackground= "#B0A3F5", highlightthickness=2, bg="gray", width= 100, height=25)
        self.acc_value = tk.Label(self.acc_value_frame, text="0.00", font=("Times New Roman", 18))
        unit = tk.Label(self.acceleration_frame, text=" m/s^2", font=("Times New Roman", 18), bg=outputFrame_bg_land, fg=textBg)
        text.grid(row=2, column=0)
        self.acc_value_frame.grid(row=2, column=1)
        self.acc_value.pack()
        unit.grid(row=2, column=2)
        self.acceleration_frame.place(relx=0.03, rely= 0.3, relheight= 0.033, relwidth=0.293)

        # Animation
        self.frame = tk.Frame(self, background=outputFrame_bg_sky)
        self.frame.place(x=50, y=50)
        self.canvas = tk.Canvas(self.frame, width=500, height=690, bg=outputFrame_bg_sky, highlightthickness=0)
        self.canvas.pack()

        self.canvas.create_rectangle(0, 489, 500, 700, fill='light green', outline='')
        self.canvas.pack()
                

    # Logic Functions 

    def calcImpact_time(self, v0, pl) -> None:
        self.impact_time = v0 / self.g[pl]

    def getInput(self):
        self.obj = self.object_var.get()
        self.h = int(self.height_slider.get())
        self.temp = int(self.temp_slider.get()) + 273.15
        self.pl = self.planet_var.get()
        self.object_validation(self.obj)

    def object_validation(self, obj) -> None:
        if obj not in ('Marshmallow', 'Car', 'Brick'):
            msgbox.showerror(title='Object Error', message='No chosen object: Select the type of objects available before proceeding')
        else:
            if obj == 'Marshmallow':
                mass = 0.02
                diameter = 0.05
            elif obj == 'Brick': 
                mass = 2.07
                diameter = 0.2
            elif obj == 'Car':
                mass = 1200
                diameter = 1.5
            
            self.obj_weight = mass * self.g[self.pl]
            self.obj_diameter = diameter
        
    # Define air density based on temperature
    def getAirPressure(self, h, R, temp) -> None:
        P = 101325 * math.exp(-0.00012 * h) # Define air pressure based on location and altitude
        self.rho_air = P / (R * temp)
    
    def getGPE(self, obj_weight, pl, h):
        # Calculate initial velocity and gravitational potential energy
        self.v0 = (2 * self.g[pl] * h) ** 1/2
        self.m = obj_weight / self.g[pl]
        self.gpe = obj_weight * h
    
    def getAcceleration(self):
        self.acc = 0 if self.impact_time == 0 else self.v0 / self.impact_time
    
    def getKE(self, obj_diameter, pl, Cd, rho_air, m):
        A = math.pi * (obj_diameter / 2) ** 2
        self.terminal_v = (2 * m * self.g[pl]) / (Cd * rho_air * A)
        self.ke = 0.5 * m * self.terminal_v ** 2
    
    def getImpactForce(self, ang, v0, pl, m, ke, terminal_v):
        if ang == 90:
            self.impact_time = v0 / self.g[pl] # Use initial velocity instead of terminal velocity
            self.impact_force = (m * self.g[pl] + ke / terminal_v) / self.impact_time
        else:
            self.impact_force = m * self.g[pl]

    # Button Functions
    def sm_parachute_command(self):
        self.Cd = 0.5
        msgbox.showinfo(title='Parachute Choice', message='Small parachute has been selected')
    
    def lg_parachute_command(self):
        self.Cd = 1.0
        msgbox.showinfo(title="Parachute Choice", message="Large parachute has been selected")
    
    def disable_air_resistance_command(self):
        self.Cd = 1e-16
        msgbox.showinfo(title="Parachute Choice", message="Air resistance has been disabled")

    def open_instruction_page(self):
        instruction_window = tk.Toplevel(self)
        instruction_window.title("Instruction Guide")
        instruction_window.geometry("550x150")

        instruction_label = tk.Label(instruction_window, text=
                            "1. Pick an air resistance by clicking onto either parachutes.\n" \
                            "2. Adjust slider to change the temperature of air and distance of height the object falls.\n"                                  
                            "3. Select an Object.\n" \
                            "4. Select a Planet to change the gravitational acceleration of the object.\n" \
                            "5. Click on the 'Rotate 90° button to rotate the object 90°.\n" \
                            "6. Click on the 'Disable Air Resistance' button to disable air resistance.\n" \
                            "7. Click on the 'Start' button to view the animation.", font= ("Calibri", 11))

        instruction_label.pack()

    def rotation_command(self):
        self.ang += 90
        if self.ang == 360:
            self.ang = 0
    
    def back_command(self):
        self.destroy()
    
    def reset_command(self):
        # Reset variable values
        self.Cd = 1
        self.ang = 0
        self.temp = 0
        self.h = 100
        self.pl = 0

        # Reset input values
        self.height_slider.set(550)
        self.temp_slider.set(0.0)
        self.object_var.set("Object")
        self.planet_var.set("Earth")

        # Reset Output Values
        self.initial_velocity_value.config(text='0.00')
        self.acc_value.config(text='0.00')
        self.ke_value.config(text='0.00')
        self.gpe_value.config(text='0.00')
        self.impact_force_value.config(text='0.00')
    
    def start_command(self):
        self.getInput() 
        self.v0 = math.sqrt(2 * self.g[self.pl] * self.h)
        self.getGPE(obj_weight=self.obj_weight, pl=self.pl, h=self.h)
        self.calcImpact_time(self.v0, pl=self.pl)
        self.object_validation(self.obj)
        self.getAirPressure(self.h, self.R, self.temp)
        self.getAcceleration()
        self.getKE(self.obj_diameter, self.pl, self.Cd, self.rho_air, self.m)
        self.getImpactForce(self.ang, self.v0, self.pl, self.m, self.ke, self.terminal_v)

        self.initial_velocity_value.config(text=f"{self.v0:.2f}")
        self.acc_value.config(text=f"{self.acc:.2f}")
        self.ke_value.config(text=f"{self.ke:.2f}")
        self.gpe_value.config(text=f"{self.gpe:.2f}")
        self.impact_force_value.config(text=f"{self.impact_force:.2f}")
    
    def start_animation(self):
        self.canvas.delete('all')

        self.canvas.create_rectangle(0, 489, 500, 700, fill='light green', outline='')
        self.canvas.pack()


        obj_mass_dict = {"Marshmallow": 0.02, "Brick": 2.07, "Car": 5}
        obj_mass = obj_mass_dict[self.object_var.get()] 

        obj_diamemetr_dict={"Marshmallow" : 0.05,"Brick":0.2,"Car":1.5}
        obj_diameter_animation = obj_diamemetr_dict[self.object_var.get()]
        height = self.height_slider.get()
        x_pos = 380
        y_pos = -(height/6)
        x_vel = 0
        y_vel = 0 
        dt = 0.06


        obj_speed = math.sqrt((2 * (obj_mass)* ((self.g[self.planet_var.get()]))) / (0.5 * self.rho_air * obj_diameter_animation ** 2 * self.Cd))
        
        #Air resistance for each object
        if self.object_var.get() == "Marshmallow":
            obj_diameter_animation = 0.05
            drag_force = 0.5 * self.rho_air * obj_speed ** 2 * obj_diameter_animation ** 2 * self.Cd
            marsh = ImageTk.PhotoImage(Image.open("marshmallow.png").resize((20,20)))
            object_display = self.canvas.create_image(x_pos, y_pos, anchor="center",image=marsh)
        elif self.object_var.get() == "Brick":
            obj_diameter_animation = 0.2
            drag_force = 0.5 * self.rho_air * obj_speed ** 2 * obj_diameter_animation ** 2 * self.Cd
            brick = ImageTk.PhotoImage(Image.open("brick.png").resize((20,20)))  
            object_display = self.canvas.create_image(x_pos,y_pos, anchor="center",image=brick)
        elif self.object_var.get() == "Car":
            obj_diameter_animation = 1.5
            drag_force = 0.5 * self.rho_air * obj_speed ** 2 * obj_diameter_animation ** 2 * self.Cd
            car = ImageTk.PhotoImage(Image.open("car.jpg").resize((20,20)))  
            object_display = self.canvas.create_image(x_pos,y_pos, anchor="center",image=car)  

        print(self.ang)        
        #Rotation

        if self.ang == 90:
            self.canvas.itemconfig(object_display, angle=90)
            
        if self.ang == 270:
            self.canvas.itemconfig(object_display, angle=270)
            


        while True:
            self.canvas.move(object_display, x_vel,y_vel)
            self.canvas.update()
            time.sleep(0.03)
            get_coords = self.canvas.coords(object_display)
            print(get_coords)
            x_pos , y_pos = get_coords
            acceleration = self.g[self.planet_var.get()]
            y_vel -= -drag_force*dt
            y_vel += acceleration*dt

            if y_pos >= 470:
                y_vel 

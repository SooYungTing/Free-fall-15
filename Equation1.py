import math

# Define constants
g = {
    "Mercury": 3.7,
    "Venus": 8.87,
    "Earth": 9.81,
    "Mars": 3.71,
    "Moon": 1.62
}
R = 287.058  # Specific gas constant of dry air in J/(kg*K)

# Get user inputs
object = input("Choose an object: Marshmallow, Brick, Car ")
air_resistance = input("Choose a size of the parachute: Big, Small, Disable ")
height = int(input("Input a height between ( ) - ( ): "))
temperature = int(input("Input a temperature between ( ) - ( ): ")) + 273.15
planet = input("Choose a planet: Mercury, Venus, Earth, Mars, Moon ")
angle = input("Choose one: Rotate 90, Rotate 180 ")

# Define air density based on temperature
P = 101325 * math.exp(-0.00012 * height)  # Define air pressure based on location and altitude
rho_air = P / (R * temperature)

# Define object weight and diameter based on object type
if object == "Marshmallow":
    object_weight = 0.02 * g[planet]
    object_diameter = 0.05
elif object == "Brick":
    object_weight = 2.07 * g[planet]
    object_diameter = 0.2
elif object == "Car":
    object_weight = 1200 * g[planet]
    object_diameter = 1.5
else:
    print("Invalid object type. Please choose Marshmallow, Brick, or Car.")
    exit()

# Calculate initial velocity and gravitational potential energy
v0 = math.sqrt(2 * g[planet] * height)
m = object_weight / g[planet]
gpe = object_weight * height

# Calculate terminal velocity and kinetic energy
if air_resistance == "Big":
    Cd = 1.0
elif air_resistance == "Small":
    Cd = 0.5
elif air_resistance == 'Disable':
    Cd = 1e-16  

A = math.pi * (object_diameter / 2) ** 2
terminal_v = math.sqrt((2 * m * g[planet]) / (Cd * rho_air * A))
ke = 0.5 * m * terminal_v ** 2

# Calculate impact force
if angle == "Rotate 90":
    impact_time = terminal_v / g[planet]
    impact_force = (m * g[planet] + ke / terminal_v) / impact_time
else:
    impact_force = m * g[planet]

# Print results
print("Initial velocity:", v0, "m/s")
print("Terminal velocity:", terminal_v, "m/s")
print("Kinetic energy:", ke, "J")
print("Gravitational potential energy:", gpe, "J")
print("Impact force:", impact_force, "N")

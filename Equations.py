object = input("Choose an object: Marshmallow, Brick, Car ")
air_resistance = input("Choose a size of the parachute: Big, Small, Disable ")
height = int(input("Input a height between ( ) - ( ): "))
temperature = int(input("Input a temperature between ( ) - ( ): "))
planet = input("Choose a planet: Mercury, Venus, Earth, Mars, Moon ")
angle = input("Choose one: Rotate 90, Rotate 180 ")

if object == "Marshmallow":
    mass = 0.0072
elif object == "Brick":
    mass = 3.5
elif object == "Car":
    mass = 1302
else:
    print("Invalid input")

if air_resistance == "Big":
    drag_coefficient = 1.0
elif air_resistance == "Small":
    drag_coefficient = 0.5
elif air_resistance == "Disable":
    drag_coefficient = 0.0
else:
    print("Invalid input")

if planet == "Mercury":
    gravity = 3.7
elif planet == "Venus":
    gravity = 8.87
elif planet == "Earth":
    gravity = 9.81
elif planet == "Mars":
    gravity = 3.71
elif planet == "Moon":
    gravity = 1.62
else:
    print("Invalid input")

if angle == "Rotate 90":
    rotation = 90
elif angle == "Rotate 180":
    rotation = 180
else:
    print("Invalid input")

t = (2 * height / gravity) ** 0.5
velocity = height / t
acceleration = gravity
gpe = mass * gravity * height
kinetic_energy = 0.5 * mass * velocity ** 2
impact_force = mass * acceleration

print("Time taken to fall: ", round(t, 2), "s")
print("Final velocity: ", round(velocity, 2), "m/s")
print("Acceleration: ", round(acceleration, 2), "m/s^2")
print("Gravitational potential energy: ", round(gpe, 2), "J")
print("Kinetic energy: ", round(kinetic_energy, 2), "J")
print("Impact force: ", round(impact_force, 2), "N")
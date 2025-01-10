# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M_earth = 5.972e24  # Mass of Earth (kg)
c = 3.0e8  # Speed of light (m/s)
R_earth = 6.371e6  # Radius of Earth (m)

# Altitudes for perigee and apogee (in meters)
altitude_perigee = 23222e3  # Perigee altitude (m)
altitude_apogee = 25000e3  # Apogee altitude (m)

# Distances from the center of Earth
R_perigee = R_earth + altitude_perigee  # Distance at perigee (m)
R_apogee = R_earth + altitude_apogee  # Distance at apogee (m)

# Gravitational redshift formula: z = GM / (Rc^2)
z_perigee = G * M_earth / (R_perigee * c**2)  # Redshift at perigee
z_apogee = G * M_earth / (R_apogee * c**2)  # Redshift at apogee

# Print results
print(f"Gravitational redshift at perigee: {z_perigee:.12e}")
print(f"Gravitational redshift at apogee: {z_apogee:.12e}")

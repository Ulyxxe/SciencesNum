import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M_earth = 5.972e24  # Mass of Earth, kg
M_sagittarius_A = 4.154e6 * 1.989e30  # Mass of Sagittarius A* in kg (solar mass equivalent)
c = 3.0e8  # Speed of light, m/s

# Function to calculate gravitational potential
# U = -GM/r
def gravitational_potential(M, r):
    return -G * M / r

# Function to calculate gravitational redshift (Einstein effect)
# Delta f / f = Delta U / c^2
def gravitational_redshift(M, r1, r2):
    delta_U = gravitational_potential(M, r2) - gravitational_potential(M, r1)
    return delta_U / c**2

# Simulation for Galileo satellites
# Orbital parameters (example values, real data should be used)
a = 29600e3  # Semi-major axis in meters (correct orbit)
e = 0.16  # Eccentricity
r_perigee = a * (1 - e)  # Closest approach (perigee)
r_apogee = a * (1 + e)  # Farthest point (apogee)

# Calculate redshift at perigee and apogee
redshift_perigee = gravitational_redshift(M_earth, r_perigee, np.inf)
redshift_apogee = gravitational_redshift(M_earth, r_apogee, np.inf)

print("Galileo Satellites Simulation")
print(f"Gravitational redshift at perigee: {redshift_perigee:.2e}")
print(f"Gravitational redshift at apogee: {redshift_apogee:.2e}")

# Simulation for S2 star
# Orbital parameters of S2 (example values)
a_s2 = 1000 * 1.496e11  # Semi-major axis in meters (1000 AU)
e_s2 = 0.88  # Eccentricity
r_peri_s2 = a_s2 * (1 - e_s2)  # Closest approach (peribothron)
r_apo_s2 = a_s2 * (1 + e_s2)  # Farthest point

# Calculate redshift at peribothron and apobothron
redshift_peri_s2 = gravitational_redshift(M_sagittarius_A, r_peri_s2, np.inf)
redshift_apo_s2 = gravitational_redshift(M_sagittarius_A, r_apo_s2, np.inf)

print("\nS2 Star Simulation")
print(f"Gravitational redshift at peribothron: {redshift_peri_s2:.2e}")
print(f"Gravitational redshift at apobothron: {redshift_apo_s2:.2e}")

# Plotting results
orbits = np.linspace(0, 2 * np.pi, 100)

def radius(theta, a, e):
    return a * (1 - e**2) / (1 + e * np.cos(theta))

r_galileo = radius(orbits, a, e)
r_s2 = radius(orbits, a_s2, e_s2)

plt.figure()
plt.polar(orbits, r_galileo / 1e3, label="Galileo Orbit (km)")
plt.polar(orbits, r_s2 / 1e11, label="S2 Orbit (100 AU)")
plt.legend()
plt.savefig("v1.jpg")
plt.title("Orbital Paths of Galileo and S2")
plt.show()

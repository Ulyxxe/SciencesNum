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

# --- Simulation 1: Galileo Satellites ---
print("Galileo Satellites Simulation")

# Orbital parameters (example values, real data should be used)
a_galileo = 29600e3  # Semi-major axis in meters (correct orbit)
e_galileo = 0.16  # Eccentricity
r_perigee_galileo = a_galileo * (1 - e_galileo)  # Closest approach (perigee)
r_apogee_galileo = a_galileo * (1 + e_galileo)  # Farthest point (apogee)

# Calculate redshift at perigee and apogee
redshift_perigee_galileo = gravitational_redshift(M_earth, r_perigee_galileo, 1e12)
redshift_apogee_galileo = gravitational_redshift(M_earth, r_apogee_galileo, 1e12)

print(f"Gravitational redshift at perigee: {redshift_perigee_galileo:.2e}")
print(f"Gravitational redshift at apogee: {redshift_apogee_galileo:.2e}")

# Plotting Galileo results
orbits_galileo = np.linspace(0, 2 * np.pi, 100)

def radius_galileo(theta):
    return a_galileo * (1 - e_galileo**2) / (1 + e_galileo * np.cos(theta))

r_galileo = radius_galileo(orbits_galileo)
plt.figure()
plt.polar(orbits_galileo, r_galileo / 1e3, label="Galileo Orbit (km)")
plt.legend()
plt.title("Orbital Path of Galileo")
plt.show()
plt.close()

# --- Simulation 2: S2 Star ---
print("\nS2 Star Simulation")

# Orbital parameters of S2 (example values)
a_s2 = 1000 * 1.496e11  # Semi-major axis in meters (1000 AU)
e_s2 = 0.88  # Eccentricity
r_peri_s2 = a_s2 * (1 - e_s2)  # Closest approach (peribothron)
r_apo_s2 = a_s2 * (1 + e_s2)  # Farthest point

# Calculate redshift at peribothron and apobothron
redshift_peri_s2 = gravitational_redshift(M_sagittarius_A, r_peri_s2, 1e12)
redshift_apo_s2 = gravitational_redshift(M_sagittarius_A, r_apo_s2, 1e12)

print(f"Gravitational redshift at peribothron: {redshift_peri_s2:.2e}")
print(f"Gravitational redshift at apobothron: {redshift_apo_s2:.2e}")

# Plotting S2 results
orbits_s2 = np.linspace(0, 2 * np.pi, 100)

def radius_s2(theta):
    return a_s2 * (1 - e_s2**2) / (1 + e_s2 * np.cos(theta))

r_s2 = radius_s2(orbits_s2)
plt.figure()
plt.polar(orbits_s2, r_s2 / 1e11, label="S2 Orbit (100 AU)")
plt.legend()
plt.title("Orbital Path of S2")
plt.show()
plt.close()

# --- Comparison of Theoretical Predictions with Measurements ---
print("\nComparison of Theoretical Predictions with Measurements")

# Example measured values (replace with real data)
measured_redshift_perigee_galileo = 4.5e-10  # Example value
measured_redshift_apogee_galileo = 3.2e-10  # Example value
measured_redshift_peri_s2 = 2.1e-4  # Example value
measured_redshift_apo_s2 = 1.0e-4  # Example value

print("Galileo Satellites:")
print(f"Measured redshift at perigee: {measured_redshift_perigee_galileo:.2e}")
print(f"Measured redshift at apogee: {measured_redshift_apogee_galileo:.2e}")
print(f"Theoretical redshift at perigee: {redshift_perigee_galileo:.2e}")
print(f"Theoretical redshift at apogee: {redshift_apogee_galileo:.2e}")

print("\nS2 Star:")
print(f"Measured redshift at peribothron: {measured_redshift_peri_s2:.2e}")
print(f"Measured redshift at apobothron: {measured_redshift_apo_s2:.2e}")
print(f"Theoretical redshift at peribothron: {redshift_peri_s2:.2e}")
print(f"Theoretical redshift at apobothron: {redshift_apo_s2:.2e}")

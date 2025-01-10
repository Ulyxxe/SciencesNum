import numpy as np
import matplotlib.pyplot as plt

# Constants (your constants are correct)
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3.0e8        # Speed of light (m/s)
M = 4.1e6 * 1.989e30  # Mass of Sgr A* (kg) (4.1 million solar masses)
AU = 1.496e11    # Astronomical Unit in meters

# Orbital parameters for Star S2
a = 120 * AU     # Semi-major axis (m), 120 AU
e = 0.88         # Eccentricity
T = 16 * 365 * 24 * 3600  # Orbital period (s) (16 years)
pericenter = a * (1 - e)  # Closest approach distance (m)

# Time array
time = np.linspace(0, T, 1000)  # Time points over one orbital period

# Your orbit_position function is correct
def orbit_position(a, e, T, t):
    n = 2 * np.pi / T
    M = n * t
    E = M
    for _ in range(10):
        E = M + e * np.sin(E)
    theta = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))
    r = a * (1 - e**2) / (1 + e * np.cos(theta))
    return r, theta

# Corrected gravitational redshift function
def gravitational_redshift(r):
    # Complete formula: z = 1/sqrt(1 - 2GM/rc^2) - 1
    return 1/np.sqrt(1 - 2 * G * M / (r * c**2)) - 1

# Correcting the semi-major axis
pericenter_desired = 120 * AU
a_corrected = pericenter_desired / (1 - e)

# Calculate positions and redshift
r_values_corrected = []
redshift_values_corrected = []
for t in time:
    r, _ = orbit_position(a_corrected, e, T, t)
    r_values_corrected.append(r)
    redshift_values_corrected.append(gravitational_redshift(r))

# Convert to AU for plotting
r_values_corrected_au = np.array(r_values_corrected) / AU

# Plotting
plt.figure(figsize=(12, 6))

# Orbital distance plot
plt.subplot(1, 2, 1)
plt.plot(time / (365 * 24 * 3600), r_values_corrected_au, label="Orbital Distance (AU)")
plt.axhline(pericenter_desired / AU, color='red', linestyle='--', label="Pericenter Distance")
plt.xlabel("Time (years)")
plt.ylabel("Distance (AU)")
plt.title("Star S2 Orbital Distance from Sagittarius A*")
plt.legend()
plt.grid()

# Gravitational redshift plot
plt.subplot(1, 2, 2)
plt.plot(time / (365 * 24 * 3600), redshift_values_corrected, label="Gravitational Redshift Factor", color='orange')
plt.xlabel("Time (years)")
plt.ylabel("Redshift Factor (z)")
plt.title("Gravitational Redshift of Star S2")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

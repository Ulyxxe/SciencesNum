import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M_earth = 5.972e24  # Mass of Earth (kg)
c = 3.0e8  # Speed of light (m/s)
R_earth = 6.371e6  # Radius of Earth (m)
T_orbit = 14 * 3600  # Orbital period of satellites in seconds (14 hours)

# Parameters for elliptical orbits (incorrect orbits)
altitude_perigee = 23222e3  # Perigee altitude (m)
altitude_apogee = 25000e3  # Apogee altitude (m)
eccentricity = (altitude_apogee - altitude_perigee) / (altitude_apogee + altitude_perigee + 2 * R_earth)

# Calculate semi-major axis and semi-minor axis
a = (altitude_perigee + altitude_apogee + 2 * R_earth) / 2  # Semi-major axis (m)
b = a * np.sqrt(1 - eccentricity**2)  # Semi-minor axis (m)

# Theoretical prediction for circular orbit (altitude = average of perigee and apogee)
altitude_circular = (altitude_perigee + altitude_apogee) / 2
R_circular = R_earth + altitude_circular
z_circular = G * M_earth / (R_circular * c**2)

# Define positions along the elliptical orbit using parametric equations
num_points = 1000
theta = np.linspace(0, 2 * np.pi, num_points)  # Angle in radians
R_elliptical = a * (1 - eccentricity**2) / (1 + eccentricity * np.cos(theta))  # Radius for each angle

# Calculate gravitational redshift along the elliptical orbit
z_elliptical = G * M_earth / (R_elliptical * c**2)

# Simulate clock drift over time
time = np.linspace(0, 10 * T_orbit, num_points)  # Time over 10 orbits
clock_drift_circular = z_circular * time  # Cumulative drift for circular orbit
clock_drift_elliptical = np.cumsum(z_elliptical) * (time[1] - time[0])  # Cumulative drift for elliptical orbit

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(time / 3600, clock_drift_circular * 1e9, label="Circular Orbit (Prediction)", linestyle='--')
plt.plot(time / 3600, clock_drift_elliptical * 1e9, label="Elliptical Orbit (Incorrect)", linestyle='-')
plt.xlabel("Time (hours)")
plt.ylabel("Clock Drift (ns)")
plt.title("Clock Drift Due to Gravitational Redshift in Galileo Satellites")
plt.legend()
plt.grid(True)
plt.show()

# Plotting additional graphs for detailed analysis

# 1. Gravitational redshift over one orbit (elliptical vs circular)
plt.figure(figsize=(12, 6))
plt.plot(theta * 180 / np.pi, z_elliptical * 1e12, label="Elliptical Orbit", linestyle='-')
plt.axhline(y=z_circular * 1e12, color='r', linestyle='--', label="Circular Orbit (Prediction)")
plt.xlabel("Orbital Position (degrees)")
plt.ylabel("Gravitational Redshift (10^-12)")
plt.title("Gravitational Redshift Over One Orbit")
plt.legend()
plt.grid(True)
plt.show()

# 2. Radius variation over one orbit (elliptical vs circular)
plt.figure(figsize=(12, 6))
plt.plot(theta * 180 / np.pi, R_elliptical / 1e6, label="Elliptical Orbit", linestyle='-')
plt.axhline(y=R_circular / 1e6, color='r', linestyle='--', label="Circular Orbit (Prediction)")
plt.xlabel("Orbital Position (degrees)")
plt.ylabel("Distance from Earth's Center (10^6 m)")
plt.title("Radius Variation Over One Orbit")
plt.legend()
plt.grid(True)
plt.show()

# 3. Clock drift rate over time (elliptical vs circular)
clock_drift_rate_elliptical = np.gradient(clock_drift_elliptical, time)
clock_drift_rate_circular = np.full_like(clock_drift_rate_elliptical, z_circular)

plt.figure(figsize=(12, 6))
plt.plot(time / 3600, clock_drift_rate_elliptical * 1e9, label="Elliptical Orbit (Incorrect)", linestyle='-')
plt.plot(time / 3600, clock_drift_rate_circular * 1e9, label="Circular Orbit (Prediction)", linestyle='--')
plt.xlabel("Time (hours)")
plt.ylabel("Clock Drift Rate (ns/s)")
plt.title("Clock Drift Rate Over Time Due to Gravitational Redshift")
plt.legend()
plt.grid(True)
plt.show()

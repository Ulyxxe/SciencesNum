import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class GalileoRedshiftSimulation:
    """
    Simulates the gravitational redshift effect for Galileo satellites in both
    elliptical (actual) and circular (intended) orbits.
    """
    
    def __init__(self):
        # Constants
        self.G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-1)
        self.M = 5.972e24     # Earth's mass (kg)
        self.c = 299792458    # Speed of light (m/s)
        
        # Galileo satellite orbital parameters (GSAT0201)
        # Elliptical orbit (actual)
        self.semi_major_elliptical = 29600e3  # Semi-major axis (m)
        self.eccentricity_elliptical = 0.1616  # Orbital eccentricity
        self.period_elliptical = 12.94 * 3600  # Orbital period (s)
        
        # Circular orbit (intended)
        self.radius_circular = 23222e3  # Intended orbital radius (m)
        self.period_circular = 12 * 3600  # Intended orbital period (s)
    
    def orbital_position_elliptical(self, t):
        """Calculate satellite position in elliptical orbit at time t."""
        n = 2 * np.pi / self.period_elliptical
        M = n * t
        
        # Solve Kepler's equation iteratively
        E = M
        for _ in range(10):
            E = M + self.eccentricity_elliptical * np.sin(E)
        
        v = 2 * np.arctan(np.sqrt((1 + self.eccentricity_elliptical)/(1 - self.eccentricity_elliptical)) * np.tan(E/2))
        r = self.semi_major_elliptical * (1 - self.eccentricity_elliptical**2)/(1 + self.eccentricity_elliptical * np.cos(v))
        
        return r
    
    def orbital_position_circular(self, t):
        """Calculate satellite position in circular orbit at time t."""
        return self.radius_circular
    
    def gravitational_potential(self, r):
        """Calculate gravitational potential at radius r."""
        return -self.G * self.M / r
    
    def frequency_shift(self, r):
        """Calculate fractional frequency shift due to gravitational redshift."""
        Φ = self.gravitational_potential(r)
        return Φ / self.c**2
    
    def simulate(self, duration_days=10, time_steps=1000):
        """
        Run simulation for both orbits for specified duration.
        Returns times, radii, and frequency shifts for both orbits.
        """
        times = np.linspace(0, duration_days*24*3600, time_steps)
        
        # Elliptical orbit
        radii_elliptical = np.array([self.orbital_position_elliptical(t) for t in times])
        shifts_elliptical = np.array([self.frequency_shift(r) for r in radii_elliptical])
        
        # Circular orbit
        radii_circular = np.array([self.orbital_position_circular(t) for t in times])
        shifts_circular = np.array([self.frequency_shift(r) for r in radii_circular])
        
        return times, radii_elliptical, shifts_elliptical, radii_circular, shifts_circular

    def plot_results(self, times, radii_elliptical, shifts_elliptical, radii_circular, shifts_circular):
        """Plot simulation results comparing both orbits."""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Convert times to days for plotting
        times_days = times / (24*3600)
        
        # Plot orbital radii
        ax1.plot(times_days, (radii_elliptical-np.mean(radii_elliptical))/1000, 'b-', 
                label='Elliptical (Actual)')
        ax1.plot(times_days, (radii_circular-np.mean(radii_circular))/1000, 'g--', 
                label='Circular (Intended)')
        ax1.set_xlabel('Time (days)')
        ax1.set_ylabel('Radius variation (km)')
        ax1.set_title('Orbital Radius Variation')
        ax1.grid(True)
        ax1.legend()
        
        # Plot frequency shifts
        ax2.plot(times_days, shifts_elliptical*1e12, 'r-', 
                label='Elliptical (Actual)')
        ax2.plot(times_days, shifts_circular*1e12, 'm--', 
                label='Circular (Intended)')
        ax2.set_xlabel('Time (days)')
        ax2.set_ylabel('Frequency shift (parts per trillion)')
        ax2.set_title('Gravitational Frequency Shift')
        ax2.grid(True)
        ax2.legend()
        
        plt.tight_layout()
        return fig

def main():
    # Create simulation instance
    sim = GalileoRedshiftSimulation()
    
    # Run simulation for 10 days
    times, radii_elliptical, shifts_elliptical, radii_circular, shifts_circular = sim.simulate(duration_days=10)
    
    # Plot results
    fig = sim.plot_results(times, radii_elliptical, shifts_elliptical, radii_circular, shifts_circular)
    
    # Calculate key statistics
    shift_amplitude_elliptical = (np.max(shifts_elliptical) - np.min(shifts_elliptical)) * 1e12
    shift_amplitude_circular = (np.max(shifts_circular) - np.min(shifts_circular)) * 1e12
    
    print("Frequency shift comparison:")
    print(f"Elliptical orbit peak-to-peak shift: {shift_amplitude_elliptical:.2f} parts per trillion")
    print(f"Circular orbit peak-to-peak shift: {shift_amplitude_circular:.2f} parts per trillion")
    
    # Compare with experimental results
    experimental_uncertainty = 0.19  # parts per trillion (from 2018 paper)
    theoretical_prediction = 4.72    # parts per trillion (peak-to-peak)
    
    print("\nComparison with experimental results:")
    print(f"Theoretical prediction: {theoretical_prediction:.2f} parts per trillion")
    print(f"Experimental uncertainty: ±{experimental_uncertainty:.2f} parts per trillion")
    
    plt.show()

if __name__ == "__main__":
    main()
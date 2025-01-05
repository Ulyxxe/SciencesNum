import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ---------------------------------------------------------
# Constants
# ---------------------------------------------------------
G = 6.67430e-11           # gravitational constant (m^3 / kg / s^2)
c = 299792458             # speed of light (m/s)
M_earth = 5.97219e24      # mass of Earth (kg)
R_earth = 6371000         # mean radius of Earth (m)

# For the black hole at the Galactic center:
# It's approximately 4.3e6 solar masses.
M_sun = 1.98847e30
M_SMBH = 4.3e6 * M_sun  # mass of the supermassive black hole at the center

# ---------------------------------------------------------
# Gravitational potential
# ---------------------------------------------------------
def gravitational_potential(r, M):
    """
    Return the gravitational potential at distance r from mass M
    in the Newtonian approximation: Phi(r) = -GM / r.
    """
    return -G * M / r

def freq_shift_ratio(r_em, r_obs, M):
    """
    Return the approximate fractional frequency shift Delta f / f
    between emitter at r_em and observer at r_obs,
    for mass M (Newtonian potential).
    """
    phi_em = gravitational_potential(r_em, M)
    phi_obs = gravitational_potential(r_obs, M)
    return (phi_em - phi_obs) / c**2

# ---------------------------------------------------------
# ODE for two-body (central force) in 2D plane
#   y = [x, vx, y, vy]
#   r = sqrt(x^2 + y^2)
#   dv/dt = -GM / r^3 * r_vector
# ---------------------------------------------------------
def kepler_eq(t, y, GM):
    x, vx, y_, vy = y
    r = np.sqrt(x**2 + y_**2)
    ax = -GM * x / r**3
    ay = -GM * y_ / r**3
    return [vx, ax, vy, ay]

def solve_orbit(r0, v0, M, t_span, steps=1000):
    """
    Solve an orbit in the XY-plane.
      r0  : initial radius (m)
      v0  : initial tangential velocity or velocity vector magnitude (m/s)
      M   : central mass
      t_span : (t0, t1) times
      steps : number of time steps
    """
    GM = G * M
    
    # We'll assume a purely circular or elliptical initial condition:
    #   position = (r0, 0), velocity = (0, v0) in XY-plane
    #   for elliptical orbits, you might set v0 < circular velocity, etc.
    y0 = [r0, 0.0, 0.0, v0]  # x, vx, y, vy
    
    t_eval = np.linspace(t_span[0], t_span[1], steps)
    sol = solve_ivp(kepler_eq, t_span, y0, args=(GM,), t_eval=t_eval, rtol=1e-9, atol=1e-12)
    
    x_vals = sol.y[0]
    vx_vals = sol.y[1]
    y_vals = sol.y[2]
    vy_vals = sol.y[3]
    t_vals = sol.t
    
    return t_vals, x_vals, y_vals, vx_vals, vy_vals

# ---------------------------------------------------------
# 1. GALILEO SATELLITES: EXAMPLE SIMULATION
# ---------------------------------------------------------
def simulate_galileo():
    """
    Simulate two Galileo satellites that ended up
    in incorrect elliptical orbits.
    
    This is a simplified version: we create elliptical orbits
    by choosing r0 and v0 that don't match a perfect circular orbit.
    We'll compute a typical observation from Earth surface
    (r_obs = Earth's radius) up to orbit radius.
    """
    # Typical orbital data (roughly):
    # Let's say the final orbit is around 17000 km altitude (not correct, but for illustration).
    # Let's just pick a big "incorrect" elliptical orbit by setting a slightly smaller velocity
    # than circular velocity, so the orbit remains elliptical.
    
    # Starting radius = R_earth + 17000e3 = 23710000 m
    # We'll create two different orbits for the two satellites:
    r0_sat1 = R_earth + 17000e3
    r0_sat2 = R_earth + 16000e3  # slight difference
    
    # Circular velocity at r0 would be v_circ = sqrt(GM_earth / r0).
    # We reduce it a bit for elliptical orbit.
    def v_circ(r): return np.sqrt(G*M_earth / r)
    v0_sat1 = 0.95 * v_circ(r0_sat1)
    v0_sat2 = 0.90 * v_circ(r0_sat2)
    
    # Integrate for, say, 14 hours:
    t_end = 14 * 3600  # seconds
    t_span = (0, t_end)
    
    # Solve orbits
    t1, x1, y1, vx1, vy1 = solve_orbit(r0_sat1, v0_sat1, M_earth, t_span, steps=2000)
    t2, x2, y2, vx2, vy2 = solve_orbit(r0_sat2, v0_sat2, M_earth, t_span, steps=2000)
    
    # Distances from Earth's center
    r_sat1 = np.sqrt(x1**2 + y1**2)
    r_sat2 = np.sqrt(x2**2 + y2**2)
    
    # We measure the frequency shift between the satellite orbit and Earth’s surface
    r_obs = R_earth  # assume receiving station on surface
    
    df_over_f_sat1 = freq_shift_ratio(r_sat1, r_obs, M_earth)
    df_over_f_sat2 = freq_shift_ratio(r_sat2, r_obs, M_earth)
    
    # Plot results
    plt.figure(figsize=(8,6))
    plt.plot(t1/3600, df_over_f_sat1, label='Satellite 1')
    plt.plot(t2/3600, df_over_f_sat2, label='Satellite 2')
    plt.xlabel('Time (hours)')
    plt.ylabel('Δf / f')
    plt.title('Gravitational Redshift - Two Galileo Satellites (Simplified)')
    plt.legend()
    plt.grid(True)
    plt.show(block=False)

# ---------------------------------------------------------
# 2. STAR S2 AROUND SMBH
# ---------------------------------------------------------
def simulate_star_S2():
    """
    Simulate star S2 orbiting around the supermassive black hole (SMBH)
    at the center of the Galaxy in a simplified Newtonian approach.
    
    Real orbit is ~16 years period, highly elliptical (~0.88 eccentricity).
    We do a simplistic approach here just to illustrate frequency shift.
    """
    # Roughly, the semi-major axis is ~1000 AU (very approximate).
    # 1 AU ~ 1.496e11 m
    # For a real elliptical orbit, we'd do a more advanced param setup.
    # Here let's do an approximate elliptical orbit by picking an initial distance ~1000 AU
    # and a velocity < circular velocity to mimic elliptical orbit.
    AU = 1.496e11
    r0_S2 = 1000 * AU  # initial distance from SMBH center
    # Circular velocity at r0:
    v_circ = np.sqrt(G * M_SMBH / r0_S2)
    # Choose something to give elliptical orbit:
    v0_S2 = 0.7 * v_circ
    
    # Period ~ 16 years => ~ 5.05e8 seconds
    # Let's integrate for, say, 1 full orbit:
    T_orbit = 16 * 365 * 24 * 3600  # ~ 16 years in seconds
    t_span = (0, T_orbit)
    
    # Solve orbit
    steps = 5000
    t_vals, x_vals, y_vals, vx_vals, vy_vals = solve_orbit(r0_S2, v0_S2, M_SMBH, t_span, steps)
    
    r_S2 = np.sqrt(x_vals**2 + y_vals**2)
    
    # Suppose the observer is "infinitely far away" for practical purposes,
    # i.e. r_obs -> ∞ => Phi(obs) ~ 0 in Newtonian sense
    # So the gravitational redshift ratio ~ Phi(r_em) / c^2
    df_over_f_S2 = gravitational_potential(r_S2, M_SMBH) / c**2  # negative values
    
    # Plot
    plt.figure(figsize=(8,6))
    plt.plot(t_vals/(3600*24*365), df_over_f_S2)
    plt.xlabel('Time (years)')
    plt.ylabel('Δf / f')
    plt.title('Gravitational Redshift - Star S2 (Simplified Newtonian Orbit)')
    plt.grid(True)
    plt.show(plt.show())

# ---------------------------------------------------------
# MAIN DEMO
# ---------------------------------------------------------
if __name__ == "__main__":
    # 1) Galileo satellites
    simulate_galileo()
    
    # 2) Star S2
    simulate_star_S2()


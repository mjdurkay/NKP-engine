import numpy as np

# ================================================================
# NKP Tesla-Vibration Early-Universe Toy Model (V4)
# 2D overdamped gradient-flow with oscillatory primordial jolt
# ================================================================

N = 64                  # grid size
L = 20.0                # domain size
dx = L / N
x = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, x)
r = np.sqrt(X**2 + Y**2)

alpha = 0.3
kappa = 0.5             # diffusion strength
epsilon = 1e-4
lambda_ = 1.0
beta = 5.0

# Initial vacuum
rho_vac = 1.0
rho = rho_vac * np.ones((N, N))

# Static Gaussian matter defect (original J from your toy model)
matter_defect = 2.0 * np.exp(-r**2 / (2 * 2.0**2))

# === Tesla-style oscillatory source (primordial frequency jolt) ===
A = 0.8                 # amplitude of vibration
omega = 2.0 * np.pi     # frequency (Tesla "energy, frequency and vibration")
sigma_osc = 3.0         # width of oscillating seed
t = 0.0                 # simulation time
osc_duration = 1000     # steps the jolt is active (early-universe phase only)

# Overdamped relaxation
dt = 0.005
for step in range(5000):
    # Laplacian
    lap = (np.roll(rho, 1, 0) + np.roll(rho, -1, 0) +
           np.roll(rho, 1, 1) + np.roll(rho, -1, 1) - 4*rho) / dx**2
    
    nonlinear = -rho / np.sqrt(rho**2 + epsilon**2) + lambda_ * beta / np.cosh(beta * rho)**2
    
    # Time-dependent oscillatory source J(t,x) — the frequency jolt
    if step < osc_duration:
        J_osc = A * np.sin(omega * t) * np.exp(-r**2 / (2 * sigma_osc**2))
    else:
        J_osc = 0.0
    J_total = matter_defect + J_osc
    
    drho_dt = kappa * lap + nonlinear + J_total
    rho += dt * drho_dt
    
    t += dt   # advance time for the oscillation

# Emergent gravitational potential Φ = -rho
Phi = -rho

# Test particles (same as your original emergent Newtonian test)
np.random.seed(42)
num_particles = 10
positions = np.random.uniform(-L/2 * 0.8, L/2 * 0.8, (num_particles, 2))
velocities = np.zeros_like(positions)

dt_part = 0.02
for _ in range(800):
    ix = np.clip(((positions[:, 0] + L/2) / dx).astype(int), 0, N-1)
    iy = np.clip(((positions[:, 1] + L/2) / dx).astype(int), 0, N-1)
    grad_x = (Phi[iy, (ix+1)%N] - Phi[iy, (ix-1)%N]) / (2*dx)
    grad_y = (Phi[(iy+1)%N, ix] - Phi[(iy-1)%N, ix]) / (2*dx)
    accel = np.stack([-grad_x, -grad_y], axis=1)
    velocities += dt_part * accel
    positions += dt_part * velocities

# Results
mean_initial = np.mean(np.sqrt(np.sum(np.random.uniform(-L/2 * 0.8, L/2 * 0.8, (num_particles, 2))**2, axis=1)))
mean_final = np.mean(np.sqrt(np.sum(positions**2, axis=1)))
print("Initial mean radial distance from center:", mean_initial)
print("Final mean radial distance from center:", mean_final)
print("Inward movement factor:", round(mean_initial / mean_final, 2))
print("Oscillatory source injected — multiple breathing defects expected!")

# Save for visualization / further analysis
np.savez('nkp_oscillatory_early_universe_toy.npz', rho=rho, Phi=Phi, positions=positions)

import numpy as np

# ================================================================
# NKP Emergent Newtonian Gravity — Wave Equation with Minimal Damping
# ================================================================
# Purpose:
#   - Pure wave equation gives outward motion (radiation pressure)
#   - Strong damping gives clean Newtonian inward motion
#   - This script tests the *intermediate* regime:
#         minimal damping → does attraction still emerge?
# ================================================================

N = 64
L = 20.0
dx = L / N
dt = 0.008

c = 6.0            # wave speed
gamma = 0.15       # ***minimal damping*** (smaller than the 0.8 version)
alpha = 0.3

x = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, x)
r = np.sqrt(X**2 + Y**2)

# Substrate field
rho = np.ones((N, N)) * 0.1
sigma = 2.0
defect = 2.0 * np.exp(-r**2 / (2*sigma**2))
rho += defect

rho_prev = rho.copy()

# Test particles
np.random.seed(42)
num_particles = 10
positions = np.random.uniform(-L/2 * 0.8, L/2 * 0.8, (num_particles, 2))
velocities = np.zeros_like(positions)

print("Running NKP Minimal-Damping Wave Equation Simulation...")

steps = 1500

for step in range(steps):
    # Laplacian
    lap = (np.roll(rho, 1, 0) + np.roll(rho, -1, 0) +
           np.roll(rho, 1, 1) + np.roll(rho, -1, 1) - 4*rho) / dx**2

    # Minimal-damping wave equation
    rho_next = (2*rho - rho_prev +
                (c*dt)**2 * lap -
                gamma * dt * (rho - rho_prev) +
                defect * 0.01)

    rho_prev = rho.copy()
    rho = rho_next.copy()

    # Particle update
    if step % 4 == 0:
        ix = np.clip(((positions[:, 0] + L/2) / dx).astype(int), 1, N-2)
        iy = np.clip(((positions[:, 1] + L/2) / dx).astype(int), 1, N-2)

        grad_x = (rho[iy, ix+1] - rho[iy, ix-1]) / (2*dx)
        grad_y = (rho[iy+1, ix] - rho[iy-1, ix]) / (2*dx)

        accel = np.stack([grad_x, grad_y], axis=1)
        velocities += dt * 6.0 * accel
        positions += dt * velocities

# Compute inward/outward movement
np.random.seed(42)
initial_positions = np.random.uniform(-L/2 * 0.8, L/2 * 0.8, (num_particles, 2))
mean_initial = np.mean(np.sqrt(np.sum(initial_positions**2, axis=1)))
mean_final = np.mean(np.sqrt(np.sum(positions**2, axis=1)))

print("\nMinimal-Damping Wave Equation Results:")
print(f"Initial mean radius: {mean_initial:.2f}")
print(f"Final mean radius:   {mean_final:.2f}")
print(f"Movement factor:     {mean_initial/mean_final:.2f}×")

if mean_final < mean_initial:
    print("\nRESULT: Attraction emerges even with minimal damping.")
else:
    print("\nRESULT: Still repulsive — damping too small for Newtonian limit.")

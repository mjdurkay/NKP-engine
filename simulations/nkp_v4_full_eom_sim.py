import numpy as np
import matplotlib.pyplot as plt

# ================================================================
# NKP V4 Full EOM Simulation
# Demonstrates the complete equation of motion (with nonlinear gradient term)
# vs the simplified gradient-flow approximation used in previous scripts.
# ================================================================

print("NKP V4 Full EOM Simulation")
print("=" * 60)

N = 256
L = 100.0
dx = L / N
x = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, x)
r = np.sqrt(X**2 + Y**2) + 0.1

# Matter defect
M = 10.0
sigma = 1.5
J = M * np.exp(-r**2 / (2 * sigma**2))

# Parameters
kappa = 0.6
alpha0 = 0.05
lambda_val = 0.1
beta = 0.5
dtau = 0.005          # smaller timestep for stability with full EOM
n_steps = 6000

rho = np.ones((N, N)) + 1e-6

print("Running full EOM (with nonlinear gradient term)...")

for step in range(n_steps):
    # Full nonlinear gradient term from exact EOM
    lap = (np.roll(rho, 1, 0) + np.roll(rho, -1, 0) +
           np.roll(rho, 1, 1) + np.roll(rho, -1, 1) - 4*rho) / dx**2
    
    grad2 = (np.gradient(rho, dx)[0]**2 + np.gradient(rho, dx)[1]**2)
    
    # Full left-hand side of EOM (simplified for 2D flat space)
    lhs = lap / rho**2 - 2 * grad2 / rho**3
    
    phi = np.log(rho)
    alpha_eff = alpha0 * (1.0 + lambda_val * np.tanh(beta * np.abs(phi)))
    
    # Right-hand side
    rhs = (1.0) * (alpha_eff * (rho - 1.0) - J)   # scaled for numerical convenience
    
    drho_dt = kappa * (lhs - rhs)
    rho += dtau * drho_dt
    rho = np.maximum(rho, 0.01)

print("Full EOM simulation complete.\n")

# Analysis - radial slice
slice_idx = N // 2
r_axis = x[slice_idx:]
Phi = 1.0 - rho[slice_idx, :]
force = -np.gradient(Phi, dx)
force_pos = np.abs(force[slice_idx:])

print("Force at key distances (V4 full EOM):")
for d in [5.0, 15.0, 30.0, 45.0]:
    idx = np.argmin(np.abs(r_axis - d))
    print(f"r ≈ {d:5.1f} | Force ≈ {force_pos[idx]:.6f}")

print("\nNote: This uses the full nonlinear gradient term from the exact EOM.")
print("The simplified gradient-flow version (used in V3 scripts) drops the -2(∇ρ)²/ρ³ term.")
print("github.com/mjdurkay/NKP-engine")

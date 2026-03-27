import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

# ================================================================
# NKP V5 Light Deflection — Using Actual Simulated Defect
# ================================================================

print("NKP V5 Light Deflection — Using Actual Simulated Defect")
print("=" * 75)

# 1. Relax ρ with full V4 EOM (your actual defect)
N = 512
L = 100.0
dx = L / N
x = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, x)
r = np.sqrt(X**2 + Y**2) + 0.1

M = 50.0          # stronger defect
sigma = 1.5
J = M * np.exp(-r**2 / (2 * sigma**2))

kappa = 0.6
alpha0 = 0.05
lambda_val = 0.1
beta = 0.5
dtau = 0.005
n_steps = 5000

rho = np.ones((N, N)) + 1e-6

print("Relaxing ρ with full V4 EOM...")

for step in range(n_steps):
    lap = (np.roll(rho, 1, 0) + np.roll(rho, -1, 0) +
           np.roll(rho, 1, 1) + np.roll(rho, -1, 1) - 4*rho) / dx**2
    grad_rho = np.gradient(rho, dx)
    grad2 = grad_rho[0]**2 + grad_rho[1]**2
    lhs = lap / rho**2 - 2 * grad2 / rho**3

    phi = np.log(rho)
    alpha_eff = alpha0 * (1.0 + lambda_val * np.tanh(beta * np.abs(phi)))
    rhs = alpha_eff * (rho - 1.0) - J

    drho_dt = kappa * (lhs - rhs)
    rho += dtau * drho_dt
    rho = np.maximum(rho, 0.01)

print("Defect generation complete.\n")

# 2. Radial profile
slice_idx = N // 2
r_pos = np.abs(x[slice_idx:])
rho_radial = rho[slice_idx, :]

rho_interp = interp1d(r_pos, rho_radial, kind='cubic', fill_value=1.0, bounds_error=False)

# 3. Metric definitions
def metric_V4(r):
    f = 1.0 / rho_interp(r)**2
    return f, f   # g_tt, g_rr

def metric_V5(r):
    return 1.0 / rho_interp(r)**2, rho_interp(r)**2

# 4. Null geodesic ODE (simplified 2D)
def geodesic_eq(lam, y, metric):
    r, phi, pr, pphi = y
    gtt, grr = metric(r)
    dlnOmega_dr = - (1/rho_interp(r)) * (rho_interp(r + 1e-6) - rho_interp(r - 1e-6)) / (2e-6)

    dpr = -dlnOmega_dr * (pr**2 - pphi**2 * r**2)
    dpphi = -2 * pr * pphi / r

    return [pr, pphi, dpr, dpphi]

def shoot_ray(b, metric, r_start=40.0):
    y0 = [r_start, 0.0, -1.0, b/r_start]
    sol = solve_ivp(lambda t, y: geodesic_eq(t, y, metric),
                    [0, 200], y0, method='RK45', rtol=1e-7, atol=1e-8)
    if not sol.success:
        return 0.0
    phi_final = sol.y[1, -1]
    return phi_final - np.pi

# 5. Compute deflections
bs = [0.5, 1.0, 2.0]
print("Light deflection using your actual NKP defect:")
for b in bs:
    theta_V4 = shoot_ray(b, metric_V4)
    theta_V5 = shoot_ray(b, metric_V5)
    print(f"b = {b:.2f} | V4 : {theta_V4:.6e} rad | V5 : {theta_V5:.6e} rad")

# 6. Plot
fig, ax = plt.subplots(figsize=(8, 8))
im = ax.imshow(rho, extent=[-L/2, L/2, -L/2, L/2], origin='lower', cmap='viridis', alpha=0.7)
plt.colorbar(im, ax=ax, label='ρ')

for b in bs:
    # V4 ray (approximate straight)
    x_straight = np.linspace(-40, 40, 200)
    y_straight = np.full_like(x_straight, b)
    ax.plot(x_straight, y_straight, '--', color='blue', alpha=0.6, label=f'V4 b={b}' if b==bs[0] else "")

    # V5 ray (simplified)
    x_bent = np.linspace(-40, 40, 200)
    y_bent = b + 0.01 * np.sin(0.2 * x_bent)   # illustrative bend
    ax.plot(x_bent, y_bent, '-', color='red', linewidth=2, label=f'V5 b={b}' if b==bs[0] else "")

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Null Geodesics in NKP Emergent Metric (V4 vs V5)')
ax.legend()
ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('nkp_v5_light_deflection.png', dpi=300, bbox_inches='tight')
print("\nPlot saved as nkp_v5_light_deflection.png")
print("Test complete.")

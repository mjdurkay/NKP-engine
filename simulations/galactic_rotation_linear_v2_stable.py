import numpy as np

# ================================================================
# NKP Galactic Rotation — Linear α (Stable Version)
# ================================================================

N = 256
L = 100.0
dx = L / N
x = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, x)
r = np.sqrt(X**2 + Y**2)

kappa = 0.5
alpha_near_zero = 0.0001
alpha_stiff = 0.05

def solve_for_alpha(a_val, n_steps=4000, dtau=0.01):
    rho = np.ones((N, N))
    defect = 5.0 * np.exp(-r**2 / (2 * 1.5**2))
    rho += defect

    for _ in range(n_steps):
        lap = (np.roll(rho, 1, 0) + np.roll(rho, -1, 0) +
               np.roll(rho, 1, 1) + np.roll(rho, -1, 1) - 4*rho) / dx**2

        drho_dt = kappa * lap - a_val * (rho - 1.0) + defect * 0.1
        rho += dtau * drho_dt

    return -rho

phi_newton = solve_for_alpha(alpha_near_zero)
phi_nkp = solve_for_alpha(alpha_stiff)

slice_idx = N // 2
force_newton = np.gradient(phi_newton[slice_idx, :], dx)
force_nkp = np.gradient(phi_nkp[slice_idx, :], dx)

r_axis = x[N//2:]
f_n = np.abs(force_newton[N//2:])
f_k = np.abs(force_nkp[N//2:])

print("Comparison of Gravitational Grip:")
print("Distance | Newton Force | NKP Force | Ratio (NKP/Newton)")
print("-" * 55)

for d in [5, 15, 30, 45]:
    idx = np.argmin(np.abs(r_axis - d))
    ratio = f_k[idx] / f_n[idx]
    print(f"{d:8} | {f_n[idx]:.6f}    | {f_k[idx]:.6f} | {ratio:.2f}x")

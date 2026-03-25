import numpy as np

# ================================================================
# NKP Lorentz Invariance Check: Moving Defect (Wave Equation)
# ================================================================

N = 128
L = 40.0
dx = L / N
dt = 0.005
c = 10.0
v = 8.0  # 0.8c

x = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, x)

# Initial vacuum + defect
rho = np.ones((N, N)) * 0.1
sigma = 2.0
center_x0 = -L/2 * 0.6
defect = 2.0 * np.exp(-((X - center_x0)**2 + Y**2) / (2*sigma**2))
rho += defect

rho_prev = rho.copy()
rho_next = rho.copy()

phi_history = []
clock_rate = []

t_max = 4.0
steps = int(t_max / dt)
for step in range(steps):
    t = step * dt
    center_x = center_x0 + v * t
    defect = 2.0 * np.exp(-((X - center_x)**2 + Y**2) / (2*sigma**2))
    
    lap = (np.roll(rho, 1, 0) + np.roll(rho, -1, 0) +
           np.roll(rho, 1, 1) + np.roll(rho, -1, 1) - 4*rho) / dx**2
    rho_next = 2*rho - rho_prev + (c*dt)**2 * lap + defect * 0.01
    
    rho_prev = rho.copy()
    rho = rho_next.copy()
    
    Phi = -rho
    phi_history.append(Phi.copy())
    
    ix = int((center_x + L/2) / dx)
    if 0 <= ix < N:
        local_amp = np.std(rho[:, ix])
        clock_rate.append(local_amp)

# Final measurements
final_Phi = Phi
max_Phi = np.max(np.abs(final_Phi))

slice_x = final_Phi[N//2, :]
fwhm_x = np.sum(np.abs(slice_x) > 0.5 * max_Phi) * dx
slice_y = final_Phi[:, N//2]
fwhm_y = np.sum(np.abs(slice_y) > 0.5 * max_Phi) * dx

background_amp = np.mean(clock_rate[:10])
center_amp = clock_rate[-1]
slowdown_factor = background_amp / center_amp if center_amp > 0 else 1.0

print("Max |Φ|:", round(max_Phi, 3))
print("Width along motion (x):", round(fwhm_x, 2))
print("Width perpendicular (y):", round(fwhm_y, 2))
print("Contraction ratio (x/y):", round(fwhm_x / fwhm_y, 2))
print("Clock slowdown factor at defect:", round(slowdown_factor, 2))

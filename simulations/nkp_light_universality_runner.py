import numpy as np

# ================================================================
# NKP Light Universality Runner (Mechanism 1)
# Runs high-frequency wave packets through static / stochastic / quench defects
# Saves nkp_light_universality_results.npz for plotting
# ================================================================

# Load the three defect backgrounds from the seeding suite
data = np.load('nkp_emergence_seeding_suite.npz')
rho_static = data['rho_static']
rho_stochastic = data['rho_stochastic']
rho_quench = data['rho_quench']

X = np.linspace(-50, 50, rho_static.shape[0])
Y = X.copy()
X, Y = np.meshgrid(X, Y)

def run_wave_packet(rho0, b_values=np.array([6,12,18,24,30,36,42,48,54,60]), k0=24*np.pi):
    c2 = 1.0 / rho0**2
    dx = X[0,1] - X[0,0]
    dt = 0.003
    steps = 4200
    thetas = []
    psi_example = None
    
    for b in b_values:
        xc0 = -40.0
        yc0 = b
        psi = np.exp(-((X - xc0)**2 + (Y - yc0)**2) / (2*3.0**2)) * np.cos(k0 * (X - xc0))
        psi_old = psi.copy()
        
        for _ in range(steps):
            lap_xx = (np.roll(psi, 1, axis=1) - 2*psi + np.roll(psi, -1, axis=1)) / dx**2
            lap_yy = (np.roll(psi, 1, axis=0) - 2*psi + np.roll(psi, -1, axis=0)) / dx**2
            lap = lap_xx + lap_yy
            psi_new = 2*psi - psi_old + (dt**2) * c2 * lap
            psi_old = psi.copy()
            psi = psi_new.copy()
        
        final_x_idx = np.argmin(np.abs(X[0, :] - 40.0))
        peak_y_idx = np.argmax(np.abs(psi[:, final_x_idx]))
        peak_y = Y[peak_y_idx, final_x_idx]
        delta_theta = np.degrees(np.arctan((peak_y - b) / 80.0))
        thetas.append(delta_theta)
        
        if psi_example is None:
            psi_example = psi.copy()
    
    return np.array(b_values), np.array(thetas), psi_example

print("Running static defect...")
b_static, theta_static, psi_static = run_wave_packet(rho_static)

print("Running stochastic defect...")
b_stochastic, theta_stochastic, psi_stochastic = run_wave_packet(rho_stochastic)

print("Running quench defect...")
b_quench, theta_quench, psi_quench = run_wave_packet(rho_quench)

np.savez('nkp_light_universality_results.npz',
         b_static=b_static, theta_static=theta_static, psi_static_example=psi_static,
         b_stochastic=b_stochastic, theta_stochastic=theta_stochastic, psi_stochastic_example=psi_stochastic,
         b_quench=b_quench, theta_quench=theta_quench, psi_quench_example=psi_quench,
         X=X, Y=Y)

print("✅ Saved nkp_light_universality_results.npz")

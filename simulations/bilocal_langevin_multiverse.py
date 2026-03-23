import numpy as np
import matplotlib.pyplot as plt

# ====================== PARAMETERS ======================
N = 128
eps = 1e-6
g_crit = 0.67
alpha = 25.0          # sigmoid steepness
lambda_0 = 1.0        # max friction strength

# ====================== INITIAL FIELD ======================
def init_rho(N, scale=0.1):
    rho = np.random.uniform(-scale, scale, (N, N))
    np.fill_diagonal(rho, 0.0)
    return rho

# ====================== COHERENCE & FRICTION ======================
def C(rho):
    return np.sum(np.sqrt(rho**2 + eps**2))

def grad_C(rho):
    return rho / np.sqrt(rho**2 + eps**2)

def lambda_eff(gC):
    return lambda_0 / (1 + np.exp(-alpha * (gC - g_crit)))

def L(rho, gC):
    lam = lambda_eff(gC)
    return lam * np.sum(np.tanh(5 * rho))

def grad_L(rho, gC):
    lam = lambda_eff(gC)
    return lam * (5 * (1 - np.tanh(5 * rho)**2))

def E(rho, gC):
    return -C(rho) + L(rho, gC)

def grad_E(rho, gC):
    return -grad_C(rho) + grad_L(rho, gC)

# ====================== LANGEVIN DYNAMICS ======================
def langevin_step(rho, gC, dt=0.01, noise_scale=0.02):
    grad = grad_E(rho, gC)
    drift = -dt * grad
    noise = noise_scale * np.sqrt(2 * dt) * np.random.randn(*rho.shape)
    rho_new = rho + drift + noise
    np.fill_diagonal(rho_new, 0.0)
    rho_new = np.clip(rho_new, -1.0, 1.0)
    return rho_new

def run_relaxation(rho, gC, steps=2000, dt=0.01, noise_scale=0.02):
    C_hist, E_hist = [], []
    for step in range(steps):
        rho = langevin_step(rho, gC, dt, noise_scale)
        if step % 50 == 0:
            C_hist.append(C(rho))
            E_hist.append(E(rho, gC))
    return rho, np.array(C_hist), np.array(E_hist)

# ====================== ANALYSIS ======================
def correlation_length(rho, max_r=None):
    N = rho.shape[0]
    if max_r is None: max_r = N // 2
    dist = np.abs(np.subtract.outer(np.arange(N), np.arange(N)))
    mean_r = np.zeros(max_r)
    for r in range(max_r):
        mask = (dist == r)
        mean_r[r] = np.mean(np.abs(rho[mask])) if np.any(mask) else 0.0
    if mean_r[0] == 0: return 1.0
    norm = mean_r / mean_r[0]
    below = np.where(norm < 1/np.e)[0]
    return below[0] if len(below) > 0 else max_r

def classify_stability(C_hist, E_hist, tol_rel=0.01):
    if len(C_hist) < 5 or len(E_hist) < 5: return False
    C_tail, E_tail = C_hist[-5:], E_hist[-5:]
    C_rel = (np.max(C_tail) - np.min(C_tail)) / (np.mean(C_tail) + 1e-9)
    E_rel = (np.max(E_tail) - np.min(E_tail)) / (np.mean(np.abs(E_tail)) + 1e-9)
    return (C_rel < tol_rel) and (E_rel < tol_rel)

# ====================== MONTE CARLO SWEEP ======================
def monte_carlo_sweep(n_gC=30, n_inits=20, g_min=0.3, g_max=1.0, steps=2000):
    g_values = np.linspace(g_min, g_max, n_gC)
    survival_frac, avg_xi = [], []
    for gC in g_values:
        stable_count = 0
        xi_list = []
        for _ in range(n_inits):
            rho = init_rho(N)
            rho_final, C_hist, E_hist = run_relaxation(rho, gC, steps=steps)
            if classify_stability(C_hist, E_hist):
                stable_count += 1
                xi_list.append(correlation_length(rho_final))
        survival_frac.append(stable_count / n_inits)
        avg_xi.append(np.mean(xi_list) if xi_list else 0.0)
        print(f"g_C = {gC:.3f} | stable: {stable_count}/{n_inits}")
    return np.array(g_values), np.array(survival_frac), np.array(avg_xi)

# ====================== RUN & PLOT ======================
g_values, survival_frac, avg_xi = monte_carlo_sweep()

fig, ax = plt.subplots(1, 2, figsize=(13, 5))
ax[0].plot(g_values, survival_frac, 'o-', color='lime', linewidth=2, label='Stable fraction')
ax[0].axvline(g_crit, color='red', linestyle='--', linewidth=2, label=f'g_crit = {g_crit}')
ax[0].set_xlabel('Coupling Strength g_C')
ax[0].set_ylabel('Fraction of stable runs')
ax[0].set_title('Stability Filter — Sharp Transition at g_crit')
ax[0].legend()
ax[0].grid(alpha=0.3)

ax[1].plot(g_values, avg_xi, 'o-', color='blue', linewidth=2, label='Avg ξ (stable runs only)')
ax[1].axvline(g_crit, color='red', linestyle='--', linewidth=2)
ax[1].set_xlabel('g_C')
ax[1].set_ylabel('Coherence Length ξ (sites)')
ax[1].set_title('Coherence Scale in Stable Universes')
ax[1].legend()
ax[1].grid(alpha=0.3)

plt.suptitle('Bilocal Langevin Substrate — Multiverse Selection via Friction Threshold')
plt.tight_layout()
plt.show()

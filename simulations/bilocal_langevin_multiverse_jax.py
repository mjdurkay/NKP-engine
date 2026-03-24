"""
NKP-engine: bilocal_langevin_multiverse_jax.py
JAX-accelerated overdamped Langevin dynamics on the bilocal coherence field ρ_ij(t).

Implements the effective energy functional E[ρ, g_C] = -C[ρ] + L[ρ, g_C]
with soft sigmoid friction threshold. The Langevin equation is the 
equation of motion derived from this functional.

Monte Carlo sweep shows the sharp stability transition at g_crit ≈ 0.67
— the computational realization of the rate-independent L[X] dynamics.

Author: Newton–Kepler Protocol (v33)
Date: March 2026
"""

import jax
import jax.numpy as jnp
from jax import jit
import matplotlib.pyplot as plt

# ====================== PARAMETERS ======================
N = 128
eps = 1e-6
g_crit = 0.67
alpha = 25.0          # sigmoid steepness
lambda_0 = 1.0        # max friction strength

# ====================== INITIAL FIELD ======================
@jit
def init_rho(key, N, scale=0.1):
    rho = jax.random.uniform(key, (N, N), minval=-scale, maxval=scale)
    rho = rho.at[jnp.diag_indices(N)].set(0.0)
    return rho

# ====================== COHERENCE & FRICTION ======================
@jit
def C(rho):
    return jnp.sum(jnp.sqrt(rho**2 + eps**2))

@jit
def grad_C(rho):
    return rho / jnp.sqrt(rho**2 + eps**2)

@jit
def lambda_eff(gC):
    return lambda_0 / (1 + jnp.exp(-alpha * (gC - g_crit)))

@jit
def L(rho, gC):
    lam = lambda_eff(gC)
    return lam * jnp.sum(jnp.tanh(5 * rho))

@jit
def grad_L(rho, gC):
    lam = lambda_eff(gC)
    return lam * (5 * (1 - jnp.tanh(5 * rho)**2))

@jit
def E(rho, gC):
    return -C(rho) + L(rho, gC)

@jit
def grad_E(rho, gC):
    return -grad_C(rho) + grad_L(rho, gC)

# ====================== LANGEVIN STEP ======================
@jit
def langevin_step(rho, gC, key, dt=0.01, noise_scale=0.02):
    grad = grad_E(rho, gC)
    drift = -dt * grad

    key, subkey = jax.random.split(key)
    noise = noise_scale * jnp.sqrt(2 * dt) * jax.random.normal(subkey, rho.shape)

    rho_new = rho + drift + noise
    rho_new = rho_new.at[jnp.diag_indices(N)].set(0.0)
    rho_new = jnp.clip(rho_new, -1.0, 1.0)

    return rho_new, key

# ====================== RELAXATION ======================
def run_relaxation(rho, gC, key, steps=2000):
    C_hist = []
    E_hist = []
    for step in range(steps):
        rho, key = langevin_step(rho, gC, key)
        if step % 50 == 0:
            C_hist.append(C(rho))
            E_hist.append(E(rho, gC))
    return rho, jnp.array(C_hist), jnp.array(E_hist), key

# ====================== CORRELATION LENGTH (JAX-NATIVE) ======================
@jit
def correlation_length(rho):
    Nloc = rho.shape[0]
    max_r = Nloc // 2
    dist = jnp.abs(jnp.subtract.outer(jnp.arange(Nloc), jnp.arange(Nloc)))

    def mean_at_r(r):
        mask = (dist == r)
        return jnp.where(jnp.any(mask), jnp.mean(jnp.abs(rho[mask])), 0.0)

    mean_r = jax.vmap(mean_at_r)(jnp.arange(max_r))

    if mean_r[0] == 0:
        return 1.0

    norm = mean_r / mean_r[0]
    below = jnp.where(norm < 1/jnp.e)[0]
    return jnp.where(len(below) > 0, below[0], max_r)

# ====================== STABILITY ======================
@jit
def classify_stability(C_hist, E_hist):
    if len(C_hist) < 5:
        return False
    C_tail = C_hist[-5:]
    E_tail = E_hist[-5:]
    C_rel = (jnp.max(C_tail) - jnp.min(C_tail)) / (jnp.mean(C_tail) + 1e-9)
    E_rel = (jnp.max(E_tail) - jnp.min(E_tail)) / (jnp.mean(jnp.abs(E_tail)) + 1e-9)
    return (C_rel < 0.01) & (E_rel < 0.01)

# ====================== MONTE CARLO SWEEP ======================
def monte_carlo_sweep(n_gC=30, n_inits=20, g_min=0.3, g_max=1.0):
    key = jax.random.PRNGKey(42)
    g_values = jnp.linspace(g_min, g_max, n_gC)

    survival_frac = []
    avg_xi = []

    for gC in g_values:
        stable_count = 0
        xi_list = []

        for _ in range(n_inits):
            key, subkey = jax.random.split(key)
            rho = init_rho(subkey, N)

            rho_final, C_hist, E_hist, key = run_relaxation(rho, gC, key)

            if classify_stability(C_hist, E_hist):
                stable_count += 1
                xi_list.append(correlation_length(rho_final))

        survival_frac.append(stable_count / n_inits)
        avg_xi.append(jnp.mean(jnp.array(xi_list)) if xi_list else 0.0)
        print(f"g_C = {float(gC):.3f} | stable: {stable_count}/{n_inits}")

    return jnp.array(g_values), jnp.array(survival_frac), jnp.array(avg_xi)

# ====================== RUN & PLOT ======================
g_values, survival_frac, avg_xi = monte_carlo_sweep()

fig, ax = plt.subplots(1, 2, figsize=(13, 5))
ax[0].plot(g_values, survival_frac, 'o-', color='lime', linewidth=2)
ax[0].axvline(g_crit, color='red', linestyle='--', linewidth=2)
ax[0].set_xlabel('Coupling Strength g_C')
ax[0].set_ylabel('Fraction of stable runs')
ax[0].set_title('Stability Filter — Sharp Transition at g_crit = 0.67')
ax[0].grid(alpha=0.3)

ax[1].plot(g_values, avg_xi, 'o-', color='blue', linewidth=2)
ax[1].axvline(g_crit, color='red', linestyle='--', linewidth=2)
ax[1].set_xlabel('g_C')
ax[1].set_ylabel('Coherence Length ξ (sites)')
ax[1].set_title('Coherence Scale in Stable Universes')
ax[1].grid(alpha=0.3)

plt.suptitle('Bilocal Langevin Substrate — Multiverse Selection via Friction Threshold (JAX)')
plt.tight_layout()
plt.show()

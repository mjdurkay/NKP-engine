# phase2_active.py
"""
Phase 2: Full active dynamics of the 3D coherence substrate.

This module evolves:
    - sigma (complex)
    - alpha (real)
    - nu (real)
    - J  (real)

All couplings are active in this phase.

Exports:
    run_phase2(alpha, sigma, nu, J, lap3, count_vortices_3d, params)
"""

import numpy as np


def run_phase2(alpha,
               sigma,
               nu,
               J,
               lap3,
               count_vortices_3d,
               params,
               max_steps=20000,
               log_interval=5000):
    """
    Run Phase 2: full active dynamics with all couplings enabled.

    Parameters
    ----------
    alpha, sigma, nu, J : np.ndarray
        Fields from Phase 1 output
    lap3 : function
        3D Laplacian operator
    count_vortices_3d : function
        Vortex counter
    params : object or namespace
        Contains all physical constants
    max_steps : int
        Number of Phase 2 steps
    log_interval : int
        Logging interval

    Returns
    -------
    alpha, sigma, nu, J : np.ndarray
        Updated fields after Phase 2
    vort_history : list
        Vortex count over time
    """

    # Unpack parameters
    dt          = params.dt
    dx          = params.dx
    noise_level = params.noise_level
    sigma_min   = params.sigma_min

    # Couplings
    g_as = params.g_as
    g_sa = params.g_sa
    g_an = params.g_an
    g_sn = params.g_sn
    g_na = params.g_na
    g_ns = params.g_ns
    g_sat = params.g_sat
    g_jn = params.g_jn

    # Dynamics
    kappa_a = params.kappa_a
    kappa_s = params.kappa_s
    kappa_n = params.kappa_n
    gamma_n = params.gamma_n
    j_decay = params.j_decay
    j_alpha = params.j_alpha
    alpha_restore = params.alpha_restore
    stress_threshold = params.stress_threshold

    N = alpha.shape[0]
    vort_history = []

    print("Phase 2: nu and J active on ordered field...")

    for step in range(max_steps):

        # --- Magnitude and stress ---
        mag = np.abs(sigma)
        mag_safe = np.maximum(mag, 1e-10)
        local_stress = np.abs(alpha - 1.0) + np.abs(mag - sigma_min)
        g_local = g_as * np.exp(-local_stress / stress_threshold)

        # --- Alpha update ---
        dalpha_dt = (
            kappa_a * lap3(alpha, dx)
            - alpha_restore * (alpha - 1.0)
            + g_sa * (mag - sigma_min)
            + g_na * nu
            + g_jn * J
        )
        alpha += dt * dalpha_dt

        # --- Sigma update ---
        dV = -2.0 * params.mu2 * mag + 4.0 * params.lam * mag**3
        pot_term = -dV * sigma / mag_safe

        dsigma_dt = (
            kappa_s * lap3(sigma, dx)
            + pot_term
            + g_local * (alpha - 1.0) * sigma / mag_safe
            + g_sn * nu * sigma / mag_safe
        )
        sigma += dt * dsigma_dt

        # --- Nu update ---
        dnu_dt = (
            kappa_n * lap3(nu, dx)
            - gamma_n * nu
            + g_an * (alpha - 1.0)
            + g_ns * (mag - sigma_min)
        )
        nu += dt * dnu_dt

        # --- J update ---
        dJ_dt = (
            -j_decay * J
            + j_alpha * (alpha - 1.0)
            + g_jn * nu
        )
        J += dt * dJ_dt

        # --- Noise ---
        sigma += noise_level * 0.02 * (
            np.random.randn(N, N, N) + 1j * np.random.randn(N, N, N)
        )
        alpha += noise_level * 0.02 * np.random.randn(N, N, N)
        nu    += noise_level * 0.01 * np.random.randn(N, N, N)
        J     += noise_level * 0.01 * np.random.randn(N, N, N)

        # --- Clipping ---
        mag_clipped = np.clip(np.abs(sigma), 0.0, 6.5)
        sigma = mag_clipped * np.exp(1j * np.angle(sigma))
        alpha = np.clip(alpha, 0.4, 4.5)
        nu    = np.clip(nu, -4.0, 4.0)
        J     = np.clip(J, -4.0, 4.0)

        # --- Vortex counting ---
        vort_now = count_vortices_3d(sigma)
        vort_history.append(vort_now)

        # --- Logging ---
        if step % log_interval == 0:
            print(
                f"  [P2] step {step:6d} | vortices={vort_now:5d} | "
                f"|sigma|={mag.mean():.4f} | J_mean={J.mean():.5f} | J_max={J.max():.4f}"
            )

    print("\nPhase 2 complete.")
    return alpha, sigma, nu, J, vort_history

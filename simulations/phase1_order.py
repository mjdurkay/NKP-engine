# phase1_order.py
"""
Phase 1: Sigma + Alpha ordering with nu = J = 0.
This module evolves the fields until the vortex count drops below a
target threshold, while logging annihilation events into A(x,y,z).

Exports:
    run_phase1(alpha, sigma, lap3, count_vortices_3d, params)
"""

import numpy as np

def run_phase1(alpha,
               sigma,
               lap3,
               count_vortices_3d,
               params,
               log_window=100,
               top_frac=0.02,
               vortex_stop=10,
               max_steps=80000):
    """
    Run Phase 1 ordering: evolve sigma + alpha with nu=J=0.

    Parameters
    ----------
    alpha, sigma : np.ndarray
        Initial fields from fields.initialize_fields()
    lap3 : function
        3D Laplacian operator
    count_vortices_3d : function
        Vortex counter for 3D sigma field
    params : object or namespace
        Contains all physical constants (dt, noise_level, etc.)
    log_window : int
        Steps between annihilation logging checks
    top_frac : float
        Fraction of high-gradient cells to log during annihilation
    vortex_stop : int
        Stop Phase 1 when vortex count < vortex_stop
    max_steps : int
        Safety cap

    Returns
    -------
    A : np.ndarray
        3D annihilation density map
    alpha, sigma : np.ndarray
        Updated fields after Phase 1
    vort_history : list
        Vortex count over time
    stop_step : int
        Step at which Phase 1 ended
    """

    # Unpack parameters
    dt          = params.dt
    dx          = params.dx
    noise_level = params.noise_level
    sigma_min   = params.sigma_min
    g_as        = params.g_as
    g_sa        = params.g_sa
    alpha_restore = params.alpha_restore
    kappa_a     = params.kappa_a
    kappa_s     = params.kappa_s
    stress_threshold = params.stress_threshold

    # Annihilation density field
    N = alpha.shape[0]
    A = np.zeros((N, N, N), dtype=float)

    vort_history = []
    vort_prev = None
    step_since_log = 0

    print("Phase 1: Ordering sigma (nu=J off), logging annihilations...")

    for step in range(max_steps):

        mag = np.abs(sigma)
        local_stress = np.abs(alpha - 1.0) + np.abs(mag - sigma_min)
        g_local = g_as * np.exp(-local_stress / stress_threshold)

        # --- Alpha update ---
        dalpha_dt = (
            kappa_a * lap3(alpha, dx)
            - alpha_restore * (alpha - 1.0)
            + g_sa * (mag - sigma_min)
        )
        alpha += dt * dalpha_dt

        # --- Sigma update ---
        mag_safe = np.maximum(mag, 1e-10)
        dV = -2.0 * params.mu2 * mag + 4.0 * params.lam * mag**3
        pot_term = -dV * sigma / mag_safe

        dsigma_dt = (
            kappa_s * lap3(sigma, dx)
            + pot_term
            + g_local * (alpha - 1.0) * sigma / mag_safe
        )
        sigma += dt * dsigma_dt

        # --- Noise ---
        sigma += noise_level * 0.03 * (
            np.random.randn(N, N, N) + 1j * np.random.randn(N, N, N)
        )
        alpha += noise_level * 0.03 * np.random.randn(N, N, N)

        # --- Clipping ---
        mag_clipped = np.clip(np.abs(sigma), 0.0, 6.5)
        sigma = mag_clipped * np.exp(1j * np.angle(sigma))
        alpha = np.clip(alpha, 0.4, 4.5)

        # --- Vortex counting ---
        vort_now = count_vortices_3d(sigma)
        vort_history.append(vort_now)
        step_since_log += 1

        if vort_prev is None:
            vort_prev = vort_now

        # --- Annihilation logging ---
        if step_since_log >= log_window:
            if vort_now < vort_prev:
                phase = np.angle(sigma)
                gx, gy, gz = np.gradient(phase, dx, edge_order=2)
                G = np.sqrt(gx**2 + gy**2 + gz**2)

                flat = G.ravel()
                k = max(1, int(top_frac * flat.size))
                thresh = np.partition(flat, -k)[-k]
                A[G >= thresh] += 1.0

            vort_prev = vort_now
            step_since_log = 0

        # --- Logging ---
        if step % 5000 == 0:
            print(f"  [P1] step {step:6d} | vortices={vort_now:5d} | |sigma|={mag.mean():.4f}")

        # --- Stop condition ---
        if vort_now < vortex_stop:
            print(f"\nPhase 1 ordering complete at step {step}. Vortex count={vort_now}.")
            return A, alpha, sigma, vort_history, step

    # If max steps reached
    print(f"\nPhase 1 reached max_steps={max_steps} without vortices < {vortex_stop}.")
    print(f"Final vortex count in Phase 1: {vort_history[-1]}")

    return A, alpha, sigma, vort_history, max_steps

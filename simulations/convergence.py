# convergence.py
"""
Convergence diagnostics for Phase 2 of the 3D coherence substrate.

This module provides:
- energy-like metrics
- field-difference norms
- vortex stabilization checks

Exports:
    check_convergence(alpha, sigma, nu, J, vort_history, params)
"""

import numpy as np


def field_change_norm(f_new, f_old):
    """
    Compute L2 norm of the change between two fields.
    """
    return np.sqrt(np.mean(np.abs(f_new - f_old)**2))


def check_convergence(alpha,
                      sigma,
                      nu,
                      J,
                      alpha_prev,
                      sigma_prev,
                      nu_prev,
                      J_prev,
                      vort_history,
                      tol=1e-4,
                      window=50):
    """
    Determine whether Phase 2 has converged.

    Convergence criteria:
    - recent vortex count stable
    - fields changing slowly (L2 norm < tol)

    Parameters
    ----------
    alpha, sigma, nu, J : np.ndarray
        Current fields
    alpha_prev, sigma_prev, nu_prev, J_prev : np.ndarray
        Fields from previous check interval
    vort_history : list
        Vortex counts over time
    tol : float
        Threshold for field-change norms
    window : int
        Number of recent vortex samples to check

    Returns
    -------
    converged : bool
        True if convergence criteria met
    metrics : dict
        Diagnostic values for logging
    """

    # --- Field-change norms ---
    d_alpha = field_change_norm(alpha, alpha_prev)
    d_sigma = field_change_norm(sigma, sigma_prev)
    d_nu    = field_change_norm(nu,    nu_prev)
    d_J     = field_change_norm(J,     J_prev)

    # --- Vortex stabilization ---
    if len(vort_history) >= window:
        recent = vort_history[-window:]
        vort_var = np.var(recent)
    else:
        vort_var = np.inf

    converged = (
        d_alpha < tol and
        d_sigma < tol and
        d_nu    < tol and
        d_J     < tol and
        vort_var < 1.0
    )

    metrics = {
        "d_alpha": d_alpha,
        "d_sigma": d_sigma,
        "d_nu":    d_nu,
        "d_J":     d_J,
        "vort_var": vort_var,
        "converged": converged
    }

    return converged, metrics

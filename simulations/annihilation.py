# annihilation.py
"""
Utilities for annihilation logging in the 3D coherence substrate.

This module provides:
- gradient-based detection of annihilation regions
- updates to the annihilation density field A(x,y,z)

Phase 1 calls these functions whenever vortex count decreases.
"""

import numpy as np


def compute_phase_gradient(sigma, dx):
    """
    Compute |∇phase| for a complex sigma field.

    Parameters
    ----------
    sigma : np.ndarray
        Complex field sigma(x,y,z)
    dx : float
        Grid spacing

    Returns
    -------
    G : np.ndarray
        Magnitude of the phase gradient
    """
    phase = np.angle(sigma)
    gx, gy, gz = np.gradient(phase, dx, edge_order=2)
    return np.sqrt(gx**2 + gy**2 + gz**2)


def log_annihilation(A, G, top_frac=0.02):
    """
    Update the annihilation density field A(x,y,z) by adding +1
    to the top `top_frac` fraction of high-gradient cells.

    Parameters
    ----------
    A : np.ndarray
        Accumulated annihilation density
    G : np.ndarray
        Phase gradient magnitude |∇phase|
    top_frac : float
        Fraction of highest-gradient cells to increment

    Returns
    -------
    None (A is modified in-place)
    """
    flat = G.ravel()
    k = max(1, int(top_frac * flat.size))
    thresh = np.partition(flat, -k)[-k]
    A[G >= thresh] += 1.0

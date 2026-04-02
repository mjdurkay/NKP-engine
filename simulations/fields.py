# fields.py
"""
Field initialization for the 3D coherence substrate.

Responsibilities:
- Define the spatial grid
- Initialize alpha, sigma, nu, J
- Provide Laplacian and random-field helpers
"""

import numpy as np

# You can later move these into a separate params.py if you like.
N        = 64
L        = 40.0
dx       = L / N
x        = np.linspace(-L/2, L/2, N)

# Sigma potential parameters
mu2       = 0.5
lam       = 0.08
sigma_min = np.sqrt(mu2 / (2.0 * lam))

# Alpha parameters
xi_a          = 1.29
kappa_a       = 1.2
alpha_restore = kappa_a / xi_a**2

# Sigma dynamics
xi_s    = 0.3
kappa_s = 0.8

# Nu parameters
kappa_n = 0.6
gamma_n = 0.05
g_an    = 0.15
g_sn    = 0.10
g_na    = 0.25
g_ns    = 0.30
g_sat   = 0.08

# J parameters
g_jn    = 0.12
j_decay = 0.82
j_alpha = 0.38

# Couplings
g_as             = 0.35
g_sa             = 0.20
stress_threshold = xi_a

# Time stepping
dt          = 0.0003
noise_level = 0.004


def lap3(f, dx):
    """
    3D 6-point Laplacian with periodic boundaries.
    f: (N,N,N) array
    """
    return (
        np.roll(f,  1, 0) + np.roll(f, -1, 0) +
        np.roll(f,  1, 1) + np.roll(f, -1, 1) +
        np.roll(f,  1, 2) + np.roll(f, -1, 2) - 6*f
    ) / dx**2


def make_field_3d(N, dx, amp, seed=42):
    """
    Random smooth 3D field via 1/k spectrum in Fourier space.
    """
    np.random.seed(seed)
    freqs = np.fft.fftfreq(N, d=dx)
    kx, ky, kz = np.meshgrid(freqs, freqs, freqs, indexing="ij")
    k = np.sqrt(kx**2 + ky**2 + kz**2)
    k[0,0,0] = 1e-10

    phases   = 2*np.pi*np.random.rand(N, N, N)
    spectrum = amp / k * np.exp(1j*phases)
    spectrum[0,0,0] = 0

    field = np.real(np.fft.ifftn(spectrum))
    field = field / (field.std() + 1e-10) * amp
    return field


def initialize_fields(seed_alpha=42, seed_sigma=99):
    """
    Build initial alpha, sigma, nu, J fields.

    Returns
    -------
    alpha, sigma, nu, J : np.ndarray
        3D arrays of shape (N, N, N)
    """
    np.random.seed(seed_alpha)

    # Alpha: near 1 with smooth fluctuations
    alpha = np.ones((N, N, N)) + make_field_3d(N, dx, 0.08, seed=seed_alpha)
    alpha = np.clip(alpha, 0.4, 4.5)

    # Sigma: random magnitude + random phase
    mag_init   = np.abs(make_field_3d(N, dx, 0.3, seed=seed_sigma)) + 0.1
    phase_init = 2*np.pi*np.random.rand(N, N, N)
    sigma      = mag_init * np.exp(1j * phase_init)

    # Nu and J start at zero
    nu = np.zeros((N, N, N))
    J  = np.zeros((N, N, N))

    return alpha, sigma, nu, J

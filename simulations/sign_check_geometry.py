# ==============================================================================

# simulations/sign_check_geometry.py

# ==============================================================================

# Newton Kepler Protocol — Emergent Geometry Sign Check

# 

# PURPOSE:

# Tests whether the emergent metric construction from the coherence substrate

# produces the correct sign for attractive geometry (gravity-like behavior).

# 

# WHAT THIS TESTS:

# Given a spherically symmetric coherence “clump” (matter as coherence defect,

# per QCIT Axiom 1), does the effective metric show:

# g_rr < g_tt (transverse)?

# This is the correct sign for an attractive geometry — radial stretching

# consistent with Newtonian gravity in the weak-field limit.

# 

# RESULT (confirmed):

# RESULT: Geometry leans ATTRACTIVE (radial stretching)

# g_rr < g_tt — correct gravitational sign confirmed.

# 

# CONNECTION TO FRAMEWORK:

# - The coherence clump models δρ_matter from QCIT Axiom 1:

# ρ(x,y) = ρ_vac + δρ_matter(x,y)

# - High coherence → short effective distance → attractive geometry

# - The relational tensor M_ij and effective metric g_ij = N[M_ij]^{-1}

# are defined in docs/NKP_Continuum_Framework_Notes.md

# - This confirms the qualitative sign check described in Document 16

# (The Ocean Remembers) and the Poisson derivation (docs/poisson_derivation.md)

# 

# EPISTEMIC NOTE:

# This is a qualitative sign check, not a derivation of GR.

# It confirms the correct gravitational sign in the weak-field regime.

# Full Einstein dynamics (G_μν = 8πG T_μν) remain future work.

# 

# THEORY: github.com/mjdurkay/nkp-engine

# Author: Michael Durkay (@SpiritOfTruth64) | mjdurkay@gmail.com

# Collaboration: Copilot (Microsoft), Gemini (Google)

# Date: March 2026

# ==============================================================================

import numpy as np

def rho_clump(x, y, rho_bg=1.0, amp=2.0, Rc=0.5):
“””
Coherence field with a spherically symmetric clump.

```
Models QCIT Axiom 1: matter as a localized coherence defect.
    ρ(x,y) = ρ_vac + δρ_matter(x,y)

Parameters:
    rho_bg: background (vacuum) coherence level
    amp:    amplitude of the coherence defect (matter clump)
    Rc:     characteristic radius of the clump

High ρ → short effective distance → attractive geometry.
"""
mid = 0.5 * (x + y)
r_mid = np.linalg.norm(mid)
clump = amp * np.exp(-r_mid**2 / (2 * Rc**2))
return rho_bg + clump
```

def K_R(x, y, R=0.2):
“””
Gaussian coarse-graining kernel.

```
Weights contributions from neighbors within scale R.
Standard in emergent geometry constructions.
"""
diff = y - x
r = np.linalg.norm(diff)
return np.exp(-r**2 / (2 * R**2))
```

def sign_check_geometry(r=1.0, n_samples=5000, R=0.2):
“””
Compute the effective metric at position x = (r, 0, 0) and check
whether the geometry is attractive (g_rr < g_tt).

```
Construction:
    1. Sample neighbors y around x with Gaussian kernel K_R
    2. Compute effective distance: d_eff(x,y) = 1/ρ(x,y)
    3. Build relational tensor: M_ij = Σ K_R(x,y) (y-x)_i (y-x)_j / d_eff²
    4. Effective metric: g_ij = N [M_ij]^{-1}
    5. Compare g_rr vs g_tt (transverse)

Sign check:
    g_rr < g_tt → ATTRACTIVE geometry (correct gravitational sign)
    g_rr > g_tt → REPULSIVE or non-attractive
"""
x = np.array([r, 0.0, 0.0])
M = np.zeros((3, 3))

# Sample neighbors around x
neighbors = x + np.random.normal(0, R, size=(n_samples, 3))

for y in neighbors:
    diff = y - x
    w_kernel = K_R(x, y, R=R)
    rho_val = rho_clump(x, y)
    d_eff_sq = (1.0 / rho_val)**2
    weight = w_kernel / d_eff_sq
    M += weight * np.outer(diff, diff)

M /= n_samples  # normalize

# Effective metric: inverse of relational tensor
g = np.linalg.inv(M)

g_rr = g[0, 0]
g_tt = 0.5 * (g[1, 1] + g[2, 2])  # average transverse components

print("\nNKP Emergent Geometry — Sign Check")
print("=" * 45)
print(f"Test point: x = ({r}, 0, 0)")
print(f"Samples: {n_samples} | Kernel scale R = {R}")
print(f"\nEffective metric components:")
print(f"  g_rr (radial):      {g_rr:.6f}")
print(f"  g_tt (transverse):  {g_tt:.6f}")
print(f"  Ratio g_rr/g_tt:    {g_rr/g_tt:.6f}")

if g_rr < g_tt:
    print("\nRESULT: Geometry leans ATTRACTIVE (radial stretching).")
    print("  g_rr < g_tt — correct sign for gravitational attraction.")
    print("  Consistent with Newtonian weak-field limit.")
else:
    print("\nRESULT: Geometry leans REPULSIVE or non-attractive.")
    print("  g_rr >= g_tt — incorrect sign for gravity.")

print("\nEpistemic note: qualitative sign check only.")
print("Full Einstein dynamics remain future work.")
print("github.com/mjdurkay/nkp-engine")

return g_rr, g_tt
```

if **name** == “**main**”:
np.random.seed(42)
sign_check_geometry()

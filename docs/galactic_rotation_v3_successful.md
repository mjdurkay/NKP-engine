Galactic Rotation V3 — Nonlinear NKP Substrate (Successful Run)

Purpose
Implements the nonlinear NKP stiffness term

\alpha_{\text{eff}} = \frac{\alpha_0}{1 + \lambda \tanh(\beta |\Phi|)}


to test how substrate softening modifies gravitational grip at galactic scales.

Key Behavior

• Strong inner boost: ~8.7× enhancement at \( r = 5 \)
• Mid‑range enhancement: ~1.5× at \( r = 15 \)
• Outer screening: force ratio → 0 at large radii
• Fully stable under minimal numerical fixes (dtau=0.01, 4000 steps)


Interpretation
This simulation demonstrates the nonlinear regime predicted by the NKP continuum functional:

• high‑|Φ| regions soften the substrate
• the defect deepens the potential well
• mid‑range grip increases
• long‑range forces are naturally suppressed


This is the first reliable nonlinear benchmark for NKP galactic‑scale behavior and complements the linear‑α screening regime.

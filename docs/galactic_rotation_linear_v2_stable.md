Galactic Rotation — Linear α (Stable V2)

Purpose
Implements the linear‑stiffness NKP substrate (constant α) to establish the baseline “massive/Yukawa‑like” regime. This simulation provides the reference behavior before nonlinear softening is introduced.

Key Behavior

• Weaker inner force than near‑Newtonian (≈0.56× at r=5)
• Rapid mid‑range falloff (≈0.20× at r=15)
• Strong outer screening (≈0.14× at r ≥ 30)
• Fully stable with minimal numerical adjustments (dtau=0.01, 4000 steps)


Interpretation
Linear α produces a pure screening regime: gravity is suppressed at all radii, with an exponential‑like decay at large distances. This matches the NKP prediction that constant stiffness behaves like a massive gravity / IR cutoff term. It does not generate dark‑matter‑like extra grip, making it an essential contrast case for the nonlinear V3 simulation.

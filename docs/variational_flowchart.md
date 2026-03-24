# Variational Structures: Flowchart

## Date: March 22-23, 2026

## Source: Michael Durkay (@SpiritOfTruth64) · Copilot (Microsoft)

## Status: Documentation — renders on GitHub without images

-----

## ASCII Flowchart (GitHub-safe)

```
┌────────────────────────────────────────────┐
│   Deterministic Lagrangian System           │
│   L[ρ, ρ̇] = T[ρ̇] – V[ρ]                   │
│   T = (μ/2) ||ρ̇||²                          │
│   V = E[ρ] = -C[ρ] + L[ρ]                  │
└───────────────┬────────────────────────────┘
                │  Euler-Lagrange
                ▼
        μ ρ̈ + ∇E[ρ] = 0
                │
                │  Add Rayleigh dissipation R = (γ/2)||ρ̇||²
                ▼
┌────────────────────────────────────────────┐
│   Lagrange-Rayleigh System                  │
│   μ ρ̈ + γ ρ̇ + ∇E[ρ] = 0                   │
└───────────────┬────────────────────────────┘
                │  Overdamped limit μ → 0
                ▼
        γ ρ̇ + ∇E[ρ] = 0
                │
                │  Add Gaussian noise η(t)
                ▼
┌────────────────────────────────────────────┐
│   Stochastic Langevin Dynamics              │
│   ρ̇ = –∇E[ρ] + η(t)                        │
│   ⟨η(t)η(t')⟩ = 2D δ(t–t')                 │
└───────────────┬────────────────────────────┘
                │  Path probability
                ▼
┌────────────────────────────────────────────┐
│   Onsager-Machlup Action                    │
│   S_OM = (1/4D) ∫ ||ρ̇ + ∇E||² dt           │
│   P[ρ(t)] ∝ exp(–S_OM)                      │
└───────────────┬────────────────────────────┘
                │  Time discretization
                ▼
┌────────────────────────────────────────────┐
│   Executable Simulation (NKP Engine)        │
│   ρ ← ρ – dt ∇E[ρ] + √(2D dt) ξ            │
│   (bilocal_langevin_multiverse.py)          │
└────────────────────────────────────────────┘
```

-----

## Extension: Poisson Equation (March 24, 2026)

```
┌────────────────────────────────────────────┐
│   Add gradient stiffness to E[ρ]:           │
│   E_grad = (κ/2) ∫ |∇φ|² d³x               │
└───────────────┬────────────────────────────┘
                │  Mean-field stationary limit
                ▼
        -κ∇²φ + m²(φ - φ_vac) = J(x)
                │
                │  QCIT Axiom 1: matter = coherence defect
                │  J(x) = γ ρ_matter(x)
                ▼
┌────────────────────────────────────────────┐
│   Poisson-like Equation                     │
│   -κ∇²φ(x) ≈ γ ρ_matter(x)                 │
│   (in long-range / near-critical regime)    │
│                                            │
│   Compare: ∇²Φ = 4πG ρ_matter              │
└────────────────────────────────────────────┘
```

-----

## One-Sentence Summary

The bilocal Langevin substrate is the discrete, noisy, overdamped limit of a
Lagrangian + Rayleigh system; its stochastic paths are described by the
Onsager-Machlup functional; and with gradient stiffness plus the QCIT Axiom 1
defect identification, the mean-field limit produces a Poisson-like equation
with matter source — all without claiming E[ρ] is a fundamental physical Lagrangian.

-----

Michael Durkay · mjdurkay@gmail.com · @SpiritOfTruth64
github.com/mjdurkay/nkp-engine · March 2026

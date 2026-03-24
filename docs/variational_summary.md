# Variational Structures: Side-by-Side Summary

## Date: March 22-23, 2026

## Source: Michael Durkay (@SpiritOfTruth64) · Copilot (Microsoft)

## Status: Mathematical documentation — not physical field theory claims

-----

## The Four Structures

|Structure               |Mathematical Object     |Governs              |Notes                                      |
|------------------------|------------------------|---------------------|-------------------------------------------|
|Deterministic Lagrangian|L = T - V               |Conservative dynamics|Legitimate action; no dissipation; no noise|
|Rayleigh Dissipation    |R = (γ/2)                                    ||ρ̇                                          |
|Onsager-Machlup Action  |S_OM = (1/4D)∫                               ||ρ̇ + ∇E                                     |
|Simulation Update       |ρ ← ρ - dt∇E + √(2D dt)ξ|Executable dynamics  |Discrete integrator for overdamped Langevin|

-----

## Detailed Equations

### 1. Deterministic Lagrangian

```
L = T - V
T = (μ/2) Σ_{ij} ρ̇²_{ij}
V = E[ρ] = -C[ρ] + L[ρ]

Euler-Lagrange: μ ρ̈ + ∇E[ρ] = 0
```

### 2. Rayleigh Dissipation → Gradient Flow

```
R = (γ/2) Σ_{ij} ρ̇²_{ij}

Lagrange-Rayleigh: μ ρ̈ + γ ρ̇ + ∇E[ρ] = 0

Overdamped limit (μ → 0): γ ρ̇ + ∇E[ρ] = 0
```

### 3. Onsager-Machlup

```
S_OM = (1/4D) ∫ dt ||ρ̇ + ∇E[ρ]||²
P[ρ(t)] ∝ exp(-S_OM)
```

### 4. Simulation Update (bilocal_langevin_multiverse.py)

```
ρ ← ρ - dt ∇E[ρ] + √(2D dt) ξ
```

-----

## Epistemic Boundary

This embedding is mathematically legitimate, but:

- Does NOT imply E[ρ] is a physical Lagrangian
- Does NOT identify ρ with a physical field
- Does NOT derive noise from microscopic physics
- Does NOT elevate the simulation to a continuum field theory

It shows only that the simulation’s dynamics fit cleanly inside the standard
variational structures used for dissipative and stochastic systems.

-----

## One-Sentence Summary

The bilocal Langevin substrate is the discrete, noisy, overdamped limit of a system
that admits both a deterministic Lagrangian embedding (via T - V with Rayleigh
dissipation) and a stochastic variational embedding (via the Onsager-Machlup
functional), without implying that E[ρ] is a physical Lagrangian or that ρ is a
physically identified field.

-----

Michael Durkay · mjdurkay@gmail.com · @SpiritOfTruth64
github.com/mjdurkay/nkp-engine · March 2026

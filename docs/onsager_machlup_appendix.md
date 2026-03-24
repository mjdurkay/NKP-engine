# Appendix: Onsager-Machlup Variational Formulation

## Date: March 22-23, 2026

## Source: Michael Durkay (@SpiritOfTruth64) · Copilot (Microsoft)

## Status: Standard mathematical formulation — not a physical field theory claim

-----

## Purpose

This appendix shows how the stochastic overdamped dynamics used in the bilocal
Langevin substrate can be expressed in a variational framework using the
Onsager-Machlup functional. This does not make the model a physical field theory;
it places the stochastic process inside the standard mathematical structure used
for path-integral descriptions of Langevin systems.

-----

## 1. Overdamped Langevin Dynamics

The simulation evolves the bilocal field ρ(t) via:

```
ρ̇ = -∇E[ρ] + η(t)
```

where η(t) is Gaussian white noise with covariance:

```
⟨η_{ij}(t) η_{kl}(t')⟩ = 2D δ_{ik} δ_{jl} δ(t-t')
```

-----

## 2. Onsager-Machlup Action for Stochastic Trajectories

For a stochastic differential equation ρ̇ = f(ρ) + η(t), the path probability is:

```
P[ρ(t)] ∝ exp(-S_OM[ρ])
```

where the Onsager-Machlup action is:

```
S_OM[ρ] = (1/4D) ∫ dt ||ρ̇ + ∇E[ρ]||²
```

For the bilocal substrate:

```
S_OM[ρ] = (1/4D) ∫ dt Σ_{ij} (ρ̇_{ij} + ∂E/∂ρ_{ij})²
```

This assigns higher weight to trajectories following the deterministic gradient flow
and lower weight to trajectories that deviate due to noise.

-----

## 3. Interpretation

The Onsager-Machlup functional is:

- A statistical action
- Used to describe the probability of stochastic paths
- Derived from the Gaussian noise measure
- NOT associated with a Hamiltonian or canonical momenta
- NOT time-reversal invariant
- NOT a stationary-action principle in the usual sense

Nevertheless, it is a legitimate variational object: the most probable path between
two configurations minimizes S_OM.

-----

## 4. Relation to the Deterministic Variational Embedding

The deterministic embedding (variational_embedding.md) gives:

```
γ ρ̇ + ∇E[ρ] = 0
```

as the overdamped limit of a Lagrangian + Rayleigh system.

The Onsager-Machlup functional extends this by incorporating noise:

- The deterministic drift -∇E appears inside the action
- The noise strength D sets the weight of fluctuations
- The most probable path satisfies the deterministic equation
- Fluctuations around it are governed by the quadratic form in S_OM

-----

## 5. Caveats and Epistemic Boundaries

The Onsager-Machlup embedding does NOT imply:

- That E[ρ] is a physical action
- That ρ corresponds to a physical field
- That the noise is derived from a microscopic bath
- That the simulation is a continuum field theory

**The embedding is mathematical, not physical.**

-----

## 6. Summary

Two complementary variational embeddings:

1. **Deterministic:** L = T - E plus Rayleigh dissipation → gradient flow in overdamped limit
1. **Stochastic:** S_OM = (1/4D) ∫ dt ||ρ̇ + ∇E||² → path probability for stochastic trajectories

Together these give a complete and mathematically rigorous variational embedding
of the simulation’s dynamics — without overclaiming physical significance.

-----

Michael Durkay · mjdurkay@gmail.com · @SpiritOfTruth64
github.com/mjdurkay/nkp-engine · March 2026

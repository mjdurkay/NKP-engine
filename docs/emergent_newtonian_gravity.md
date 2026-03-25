# Emergent Newtonian Gravity from Coherence Substrate Dynamics

**NKP Continuum Framework — Document Addendum (March 2026)**

-----

## 1. Overview

This document formalizes the Newtonian limit of the NKP coherence substrate. The key result:

> A static coherence defect generates an attractive potential Φ obeying a Poisson-like equation, and test particles accelerate inward under −∇Φ.

This is not imposed. It emerges from:

- the substrate’s energy functional
- overdamped relaxation dynamics
- linearization around the vacuum
- coarse-graining of the bilocal field ρ(x, y)

The 2D simulation in `emergent_newtonian_2d_toy.py` reproduces this behavior directly.

-----

## 2. Substrate Dynamics

We begin with the overdamped gradient flow:

```
∂ₜρ = κ∇²ρ − αρ + nonlinear terms
```

Linearizing around the vacuum ρ = ρ₀ + δρ gives:

```
∂ₜδρ = κ∇²δρ − αδρ
```

In the static limit (∂ₜ → 0):

```
∇²δρ = (α/κ) δρ
```

A localized matter defect acts as a source term S(x):

```
∇²δρ = S(x)
```

Define the emergent potential:

```
Φ = −δρ
```

Then:

```
∇²Φ = −S(x)
```

This is the Newtonian Poisson equation up to constants.

-----

## 3. Simulation Summary

**File:** `emergent_newtonian_2d_toy.py`

### Setup

|Parameter            |Value                   |
|---------------------|------------------------|
|Grid                 |64×64                   |
|Domain               |L = 20                  |
|Coherence parameter α|0.3 (Document 3)        |
|Defect               |Gaussian, σ = 2         |
|Dynamics             |Overdamped relaxation   |
|Test particles       |10, randomly initialized|

### Results

|Metric         |Value                            |
|---------------|---------------------------------|
|Inward movement|100% of particles (all 10)       |
|Direction      |All particles moved toward defect|
|Potential well |Stable, correct sign             |

### Interpretation

- Φ = −ρ forms a stable potential well
- −∇Φ points inward
- Particles accelerate toward the defect
- No force law was imposed
- Attraction is a structural consequence of the substrate

-----

## 4. Limitations

- Overdamped dynamics → instantaneous propagation
- No Lorentz structure
- No stress-energy tensor
- Only weak-field Newtonian limit

These limitations motivate the next document: emergent Lorentz structure (`emergent_lorentz_structure.md`).

-----

## 5. Conclusion

The NKP substrate reproduces Newtonian gravity in the static, overdamped regime. This is the first falsifiable, simulation-backed demonstration of emergent attraction in the NKP framework.

# NKP Theory 013 — The χ Framework and the Deflection Prefactor

**Document ID:** NKP-THEORY-013
**Date:** 2026-04-06
**Author:** Michael Durkay
**Framework Layer:** Layer III — Geometry Mapping → Open Problem
**Status:** Motivated framework. Not a derivation of GR.
**Follows from:** NKP-THEORY-012 (Path B hypothesis)

-----

## 1. Motivation and Scope

This document introduces the coherence scalar χ as a framework
for investigating the factor-of-2 gap between the substrate
prediction (0.875 arcsec) and GR (1.750 arcsec).

**What is in scope:**

- Defining χ as a functional of existing fields
- Deriving the most general effective propagation equation
- Expressing the deflection prefactor k in terms of response
  coefficients A and B
- Stating the GR condition precisely

**What is explicitly out of scope:**

- Claiming A = B follows from the substrate
- Claiming k = 2 without derivation
- Closing the factor of 2

χ does not introduce new degrees of freedom. It is a scalar
summary of the local degree of order already present in the
σ-α-ν-J system. Whether it resolves the factor of 2 depends
on a calculation that has not been completed.

-----

## 2. Definition of χ

χ is defined as a functional of existing fields:

```
χ(x) = a_σ * (1 - |σ(x)|/σ_min)
      + a_α * |α(x) - 1|
      + a_ν * ν(x)²
      + a_J * |J(x) - J_vac| / J_vac
```

**Normalization:**

- In the far vacuum: χ → 0
- Near a stable vortex core: χ → χ_core > 0

**Illustrative core values from Path 3 simulation**
(marked as illustrative — not yet used to fix A or B):

```
|σ|/σ_min at core  ≈ 0      → contribution ≈ 1.0
|α - 1| at core    ≈ 0.15   → contribution ≈ 0.15
ν² at core         ≈ 0.022  → contribution ≈ 0.022
|J - J_vac|/J_vac  ≈ 0.70   → contribution ≈ 0.70

χ_core ≈ 1.872  (with a_σ = a_α = a_ν = a_J = 1)
```

The overall normalization is not fixed by these values.
The coefficients a_σ, a_α, a_ν, a_J would need to be
derived from the microscopic action, not chosen.

The specific choice of weights a_σ, a_α, a_ν, a_J is
constrained by symmetry and dimensional analysis but must
ultimately be derived from the microscopic action.

-----

## 3. Effective ψ-χ Lagrangian

Take ψ as a high-frequency scalar excitation of the ordered
phase (amplitude mode of σ).

The most general local, quadratic, χ-dependent Lagrangian
to first order in χ, consistent with:

- ψ → -ψ symmetry
- χ scalar, neutral, no new charges
- no preferred spatial direction

is:

```
L_eff = (1/2)(1 + A·χ)(∂_t ψ)²
      - (1/2)(1 + B·χ)|∇ψ|²
      - (1/2)(m₀² + C·χ)ψ²
```

Where:

- A encodes how χ modifies the temporal kinetic term
- B encodes how χ modifies the spatial kinetic term
- C encodes how χ modifies the mass term

**These are response coefficients to be derived from the
σ-α-ν-J microscopic action. They are not chosen here.**

-----

## 4. Eikonal Limit and Effective Metric

In the high-frequency eikonal limit with ψ = a·exp(iS/ε),
ε → 0, the equation of motion reduces to:

```
(1 + A·χ)(∂_t S)² - (1 + B·χ)|∇S|² - (m₀² + C·χ) = 0
```

This identifies the effective metric components:

```
g^tt_eff = 1 + A·χ
g^ij_eff = -(1 + B·χ)·δ^ij
```

Inverting to first order in χ:

```
g_tt ≈ -(1 - A·χ)
g_ij ≈ (1 - B·χ)·δ_ij
```

Mapping to the weak-field GR form:

```
g_tt = -(1 + 2Φ_t)
g_ij = (1 - 2Φ_s)·δ_ij
```

Gives:

```
2Φ_t ≈ A·χ
2Φ_s ≈ B·χ
```

-----

## 5. Deflection Prefactor k and GR Condition

The total light deflection in the weak-field limit is
proportional to Φ_t + Φ_s. The deflection prefactor
relative to the purely spatial (Newtonian) result is:

```
k = (Φ_t + Φ_s) / Φ_s = 1 + Φ_t/Φ_s = 1 + A/B
```

χ cancels in the ratio to leading order.

**Interpretation:**

- A/B is the ratio of temporal to spatial response
- k measures how much the temporal response adds to the
  spatial response
- k = 1: purely spatial, Newtonian (A = 0)
- k = 2: GR (A = B)

**The GR condition:**

```
A = B  →  k = 2
```

**Explicit statement:**

There is currently no evidence that A = B follows from
the σ-α-ν-J substrate. This condition may hold, may not
hold, or may hold approximately in a specific regime.
Whether it holds is a dynamical question about the substrate
that requires the full microscopic calculation.

-----

## 6. Open Problem and Program

**Open Problem:**

Derive A and B from the microscopic σ-α-ν-J action in
curved spacetime.

**Required work:**

1. Write or specify the four-field action in curved spacetime
   (NKP-THEORY-014, pending)
1. Identify the σ amplitude mode δr as the relevant
   excitation ψ
1. Integrate out fast modes to obtain the effective
   quadratic action for δr
1. Read off the coefficients in front of (∂_t δr)² and
   |∇δr|² as functions of the background fields
1. Express these coefficients in terms of χ to identify
   A(χ) and B(χ)
1. Evaluate the ratio A/B and compute k

**Until steps 1-6 are completed:**

χ is a framework for posing the question, not an answer.
k = 1 + A/B is a real result conditional on A and B
being derivable from the substrate. The factor of 2
remains an open problem.

-----

## 7. What This Document Establishes

**Established:**

- χ can be defined as a functional of existing fields
  with vacuum normalization χ → 0
- The most general effective propagation equation has
  the form given in Section 3
- The deflection prefactor k = 1 + A/B follows from
  the eikonal limit by standard methods
- The GR condition is A = B

**Not established:**

- That A and B are derivable from the substrate
- That A = B holds in the substrate
- That k = 2 follows without tuning
- That the factor of 2 is closed

-----

## 8. Derivation Chain

|Step|Document          |Result                                            |
|---:|------------------|--------------------------------------------------|
|1-6 |NKP-THEORY-001–006|Four-field substrate, bang, ringdown              |
|7   |NKP-THEORY-007    |Screened Poisson, Yukawa well                     |
|8   |NKP-THEORY-008    |Eikonal Δφ = 2A/b                                 |
|9   |NKP-THEORY-009    |Unit mapping (factor of 2 unresolved)             |
|10  |NKP-THEORY-010    |T_00 ≠ T_ii, sufficient condition missing         |
|11  |NKP-THEORY-011    |General isotropy result. Three paths.             |
|12  |NKP-THEORY-012    |Path B hypothesis. EFT direction motivated.       |
|13  |**NKP-THEORY-013**|**χ framework. k = 1 + A/B. GR condition: A = B.**|
|14  |NKP-THEORY-014    |Four-field action in curved spacetime (pending)   |

-----

*Newton Kepler Protocol — github.com/mjdurkay/nkp-engine*

*A framework that poses the question precisely
is more valuable than a narrative that answers it prematurely.*

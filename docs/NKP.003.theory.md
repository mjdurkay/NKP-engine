# NKP Theory — Substrate Stability and Local Homogeneity

**Document ID:** NKP-THEORY-003
**Date:** 2026-04-06
**Author:** Michael Durkay
**Framework Layer:** Layer I — Substrate
**Status:** Foundational. No geometric claims.
**Follows from:** NKP-THEORY-002
**Followed by:** NKP-THEORY-004

-----

## 1. Summary

This document explains why the substrate supports stable
ordered regions, stable defects, and locally homogeneous
behavior. No geometric interpretation is made. The term
“local flatness” is used strictly in the field-theoretic
sense — slow field variation over several lattice sites —
not in any metric or curvature sense.

-----

## 2. Stability of the Ordered Phase

The σ potential has a stable minimum at σ_min:

```
V(σ) = −μ²|σ|² + λ|σ|⁴
dV/d|σ| = 0  at  |σ| = σ_min
d²V/d|σ|² > 0  (stable minimum)
```

Any deviation from σ_min costs energy. The field relaxes
back toward σ_min under its own dynamics.

The α restoring term drives α → 1 in the absence of sources:

```
dα/dt ⊃ −α_restore · (α − 1)
```

Together these ensure the ordered phase is an attractor
of the dynamics, not an externally imposed condition.

-----

## 3. Stability of Defects

Vortex cores are topologically protected. A vortex with
winding number +1 cannot be continuously deformed to a
configuration with winding number 0 without passing through
a singular state. This is a property of the phase field of
σ, not of the potential.

Stable vortices persist indefinitely in the ordered phase
unless they encounter an antivortex of opposite charge.
This is confirmed by simulation — vortex pairs survive
for the full run length once the system orders.

-----

## 4. Local Homogeneity

Inside a coherence window W (defined in NKP-THEORY-002):

- σ varies slowly: |∇σ| ≪ σ_min / ξ_s
- α varies slowly: |∇α| ≪ 1 / ξ_a
- The field equations can be linearized

This is what is meant by “local flatness” in this framework.
It is a statement about field variation rates, not about
any metric or geometric curvature.

**This is not an analogy to GR’s local Minkowski space.**
It is a field-theoretic condition that enables linearization.
The connection to geometry, if any, is established later
in NKP-THEORY-007 onward.

-----

## 5. Why This Matters for NKP-THEORY-007

The screened Poisson equation derived in NKP-THEORY-007
requires:

- α linearized around α = 1
- σ approximately at σ_min (so the source term is well-defined)
- ν varying slowly (so gradient terms dominate)

These conditions are satisfied inside coherence windows.
NKP-THEORY-003 establishes that such windows exist and
are stable. NKP-THEORY-007 uses them.

-----

## 6. What Is and Is Not Claimed

**Established:**

- The ordered phase is dynamically stable
- Vortex defects are topologically stable within it
- Coherence windows support linearization of the field
  equations

**Not established:**

- Any geometric interpretation of local homogeneity
- Any connection to GR’s local flatness theorem

-----

## 7. Derivation Chain

|Step|Document          |Result                                       |
|---:|------------------|---------------------------------------------|
|1   |NKP-THEORY-001    |Four-field motivation and roles              |
|2   |NKP-THEORY-002    |Coherence functional and window              |
|3   |**NKP-THEORY-003**|**Substrate stability and local homogeneity**|
|4   |NKP-THEORY-004    |Bang → ringdown → ordered phase sequence     |
|5   |NKP-THEORY-005    |Vortices, σ suppression, α wells             |
|6   |NKP-THEORY-006    |Bridge to geometry mapping                   |
|7   |NKP-THEORY-007    |Screened Poisson equation, Yukawa well       |

-----

*Newton Kepler Protocol — github.com/mjdurkay/nkp-engine*

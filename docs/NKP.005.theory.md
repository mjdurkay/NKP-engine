# NKP Theory — Vortices, σ Suppression, and α Wells

**Document ID:** NKP-THEORY-005
**Date:** 2026-04-06
**Author:** Michael Durkay
**Framework Layer:** Layer II — Static Structures
**Status:** Partial derivation. Screened Poisson equation
established. No geometry.
**Follows from:** NKP-THEORY-004
**Followed by:** NKP-THEORY-006

-----

## 1. Summary

This document shows how σ suppression at vortex cores,
combined with ν accumulation, produces α depressions that
satisfy a screened Poisson equation. This is the direct
precursor to the Yukawa well derived in NKP-THEORY-007.

No geometric interpretation of α is made here. The
connection to gravitational analogs begins in NKP-THEORY-007.

-----

## 2. Vortex Structure in σ

A vortex is a topological defect in the phase of σ:

```
σ(r, θ) = f(r) · exp(iθ)

f(0) = 0          (core: σ suppressed to zero)
f(∞) = σ_min      (vacuum: σ fully ordered)
```

The phase winds by 2π around the core. This is topologically
protected — it cannot be removed without a global phase
reorganization.

At the core: |σ| = 0. This is the source of the α depression.

-----

## 3. The Source Term

The α equation contains:

```
dα/dt = κ_a ∇²α − α_restore(α−1) + g_sa(|σ|−σ_min) + g_an·ν
```

Near the vortex core:

- |σ| < σ_min  →  g_sa(|σ|−σ_min) < 0  (negative source)
- ν accumulates as a deficit  →  g_an·ν < 0  (negative source)

Both terms drive α below 1 at the core. The combined source:

```
S(r) = g_sa(|σ(r)|−σ_min) + g_an·ν(r)
```

is negative near the core and approaches zero far away.

-----

## 4. Screened Poisson Equation

At steady state (dα/dt = 0), defining φ = α − 1:

```
κ_a ∇²φ − α_restore · φ = −S(r)
```

Rearranging:

```
∇²φ − (1/ξ_a²) · φ = −S(r)/κ_a
```

where:

```
ξ_a = sqrt(κ_a / α_restore) = 1.29  (simulation units)
```

This is a screened Poisson equation. The screening length
ξ_a equals the coherence length set by the field parameters.
This is not a coincidence — it follows directly from the
definition of α_restore = κ_a / ξ_a².

-----

## 5. The Yukawa Solution

For a localized source S(r) concentrated at the vortex core,
the screened Poisson equation has the solution:

```
φ(r) = −(A/r) · exp(−r/ξ_a)
```

where A is determined by the source strength — specifically
by how deeply |σ| is suppressed and how strongly ν accumulates
at the core.

Properties:

- r ≪ ξ_a:  φ(r) ≈ −A/r     (deep well near core)
- r ∼ ξ_a:  transition zone
- r ≫ ξ_a:  φ → 0             (exponential recovery to vacuum)

This is the α well. NKP-THEORY-007 derives it in full and
evaluates A from simulation parameters.

-----

## 6. What Is and Is Not Claimed

**Established:**

- Vortex cores produce σ suppression and ν accumulation
- The α equation at steady state reduces to a screened
  Poisson equation
- The solution is a Yukawa well with screening length ξ_a
- The screening length follows from field parameters
  without tuning

**Not established:**

- Any geometric interpretation of α or φ
- That A corresponds to any physical quantity
  (this is addressed in NKP-THEORY-007 and 009)

-----

## 7. Derivation Chain

|Step|Document          |Result                                   |
|---:|------------------|-----------------------------------------|
|1   |NKP-THEORY-001    |Four-field motivation and roles          |
|2   |NKP-THEORY-002    |Coherence functional and window          |
|3   |NKP-THEORY-003    |Substrate stability and local homogeneity|
|4   |NKP-THEORY-004    |Bang → ringdown → ordered phase          |
|5   |**NKP-THEORY-005**|**Vortices, σ suppression, α wells**     |
|6   |NKP-THEORY-006    |Bridge to geometry mapping               |
|7   |NKP-THEORY-007    |Screened Poisson equation, Yukawa well   |

-----

*Newton Kepler Protocol — github.com/mjdurkay/nkp-engine*

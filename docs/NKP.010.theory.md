# NKP Theory — Stress-Energy Anisotropy and the Factor-of-2 Problem

**Document ID:** NKP-THEORY-010
**Date:** 2026-04-05
**Author:** Michael Durkay
**Framework Layer:** Layer III — Geometry Mapping → Open Problem
**Status:** Necessary condition identified. Sufficient condition missing.
**Follows from:** NKP-THEORY-009 (physical unit mapping)

-----

## 1. Summary

This document states precisely where the geometry mapping stands
and where it stops. The eikonal light deflection calculation gives
Δφ = 2A/b — half the GR value of 4A/b. Closing the factor of 2
requires showing that the four-field stress-energy tensor sources
an anisotropic metric. The necessary condition for that anisotropy
— T_00 ≠ T_ii — is likely satisfied near the vortex core. The
sufficient condition — field equations coupling T_μν to the metric
in a way that produces Schwarzschild-like splitting — does not yet
exist in this framework.

No further claims are made. This document is the exact boundary.

-----

## 2. What the Eikonal Calculation Establishes

From NKP-THEORY-008, using the eikonal (wave optics) approach
rather than null geodesics:

Light in the substrate follows the effective refractive index:

```
n(r) = 1/α(r) ≈ 1 + (A/r)·exp(−r/ξ_a)
```

The deflection integral gives:

```
Δφ = 2A/b
```

This result is not circular. It does not suffer from conformal
cancellation. It is the honest prediction of the framework as
currently formulated.

Comparing to GR:

```
Δφ_GR = 4GM/bc² = 4A/b  (if A = r_s)
```

The framework predicts half the GR deflection.

That is the current honest result: **0.875 arcsec at the solar
limb, not 1.750 arcsec.**

-----

## 3. Why GR Gets 4A/b

The Schwarzschild metric has the form:

```
ds² = −(1−r_s/r)dt² + (1+r_s/r)(dr² + r²dΩ²)
```

Time and space components scale differently. That asymmetry
produces equal contributions from spatial curvature and temporal
curvature — doubling the deflection over the purely spatial result.

The conformal metric used in this framework:

```
ds² = α(r)^{-2}·η_μν dx^μ dx^ν
```

scales time and space identically. The conformal factor cancels
in the null geodesic condition. Only the spatial gradient
contributes to deflection through the eikonal approach.

-----

## 4. The Stress-Energy Tensor at Steady State

For the α field, the stress-energy tensor has the general form:

```
T_μν = ∂_μα · ∂_να − g_μν · L
```

At steady state (∂_t α = 0) near the vortex core:

```
T_00 = V(α)
T_ii = (∂_i α)² − V(α)
```

Where V(α) is the potential energy density and (∂_i α)² is
the gradient energy density.

These are independent quantities. Near the vortex core:

- V(α) is set by the restoration term α_restore·(α−1)²/2
- (∂_i α)² is set by the slope of the Yukawa well

They are not equal in general.

**Therefore: T_00 ≠ T_ii near the vortex core.**

This is the necessary condition for the stress-energy tensor
to source an anisotropic metric — one with different time
and space scalings.

-----

## 5. The Missing Derivation

T_00 ≠ T_ii is necessary but not sufficient.

To close the factor of 2 requires:

1. Field equations coupling T_μν to the metric components
   in this framework — something equivalent to:
   
   ```
   G_μν = 8πG T_μν
   ```
   
   derived from varying the four-field action with respect
   to the metric.
1. Proof that those field equations produce Schwarzschild-like
   splitting — different scaling for time and space components.
1. Verification that the resulting metric gives Δφ = 4A/b
   rather than 2A/b.

None of these exist in the current framework. The four-field
action has not been varied with respect to the metric. The
Einstein equations or equivalent have not been derived. The
connection between T_μν and g_μν in this framework is unknown.

-----

## 6. What This Means for the Framework

The framework currently predicts:

```
Δφ = 2A/b = 0.875 arcsec at the solar limb
```

This is a real prediction. It differs from GR by a factor of 2.
It is falsifiable by precision astrometry.

The factor of 2 may close if the missing derivation is completed
and produces Schwarzschild-like metric splitting. It may not.
Both outcomes are scientifically meaningful.

**If the derivation closes the factor of 2:**
The framework reproduces GR light deflection from substrate
field dynamics. That is a significant result.

**If the derivation does not close the factor of 2:**
The framework predicts a specific deviation from GR — 0.875
arcsec versus 1.750 arcsec — that is in principle measurable.
That is also a significant result.

-----

## 7. The Honest Boundary

**Established by simulation:**

- α organizes around vortex cores through back-reaction (Path 3)
- Yukawa well structure emerges from screened Poisson equation
- Bang, post-bang relaxation, and J_vac = 0.4019 confirmed

**Established by mathematics:**

- Screened Poisson equation and Yukawa solution (NKP-THEORY-007)
- Eikonal deflection Δφ = 2A/b (NKP-THEORY-008, corrected)
- T_00 ≠ T_ii at steady state near vortex core (this document)

**Not yet established:**

- Field equations coupling T_μν to metric
- Proof of metric anisotropy from four-field action
- Factor of 2 closure
- Formal reduction to GR in any limit

-----

## 8. Derivation Chain

|Step|Document          |Result                                                  |
|---:|------------------|--------------------------------------------------------|
|1   |NKP-THEORY-001    |Four-field substrate derived                            |
|2   |NKP-THEORY-002    |Coherence functional, window formation                  |
|3   |NKP-THEORY-003    |Local flatness (needs strengthening)                    |
|4   |NKP-THEORY-004    |Excitation → directionality sequence                    |
|5   |NKP-SIM-001–006   |Simulation results confirmed                            |
|6   |NKP-THEORY-007    |Screened Poisson equation, Yukawa well                  |
|7   |NKP-THEORY-008    |Eikonal deflection Δφ = 2A/b                            |
|8   |NKP-THEORY-009    |Physical unit mapping (factor of 2 unresolved)          |
|9   |**NKP-THEORY-010**|**T_00 ≠ T_ii confirmed. Sufficient condition missing.**|
|10  |NKP-THEORY-011    |Metric from four-field action (pending)                 |

-----

*Newton Kepler Protocol — github.com/mjdurkay/nkp-engine*

*The boundary of what is known is as important as what is known.*

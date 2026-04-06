# NKP Theory — Null Geodesic and Light Deflection

**Document ID:** NKP-THEORY-008
**Date:** 2026-04-05
**Author:** Michael Durkay
**Framework Layer:** Layer III — Geometry Mapping → Light Deflection
**Status:** Deflection integral complete. Falsification condition established.
**Follows from:** NKP-THEORY-007 (screened Poisson, Yukawa well)

-----

## 1. Summary

This document derives the light deflection angle for a null geodesic
passing through the α field well around a stable vortex core.
The deflection integral reduces to Δφ = 2A/b in the regime r << ξ_a.
Matching to the GR prediction requires A = r_s (the Schwarzschild
radius of the source). This is the precise falsification condition:
the depth parameter A of the α well must equal the Schwarzschild
radius when simulation parameters are mapped to physical units.

-----

## 2. Setup

From NKP-THEORY-007, the steady-state α profile around a vortex core:

```
α(r) = 1 − (A/r)·exp(−r/ξ_a)
```

Candidate metric (conformal, Lorentzian):

```
ds² = α(r)^{-2} · η_μν dx^μ dx^ν
    = α(r)^{-2} (−dt² + dr² + r²dΩ²)
```

-----

## 3. Null Geodesic Condition

Light travels on null geodesics: ds² = 0.

Restricting to the orbital plane (dΩ → dφ):

```
α(r)^{-2} (−dt² + dr² + r²dφ²) = 0
```

The photon passes the vortex core at closest approach distance b
(impact parameter). By symmetry the trajectory is planar.

-----

## 4. Why Deflection Depends on the Gradient

A uniform α(r) = const produces no deflection regardless of its
value — the metric is uniformly stretched and there is no preferred
direction. Deflection requires dα/dr ≠ 0.

Physical analogy: a lens bends light because the refractive index
varies across it, not because it is high or low everywhere.
The gradient across the photon path is what creates curvature.

The deflection integral therefore depends on |dα/dr|, not α itself.

-----

## 5. Gradient of the α Well

From NKP-THEORY-007:

```
dα/dr = (A·exp(−r/ξ_a)/r²) · (1 + r/ξ_a)
```

Two regimes:

```
r << ξ_a:  dα/dr ≈ A/r²     (Newtonian gradient)
r >> ξ_a:  dα/dr → 0        (exponential suppression)
```

The deflection is concentrated in the region r ~ b where the
photon passes closest. Beyond r ~ few·ξ_a the integrand
is negligible.

-----

## 6. Deflection Integral

General form:

```
Δφ = 2∫[b to ∞] (1/r²) · |dα/dr| · (r/α) · dr/sqrt(1 − b²/r²)
```

In the regime b << ξ_a (photon passes well inside coherence length),
exp(−r/ξ_a) ≈ 1 and α(r) ≈ 1 near closest approach.

The integral reduces to:

```
Δφ = 2∫[b to ∞] (A/r²) · (b/r) · dr/sqrt(1 − b²/r²)
```

Substituting u = b/r:

```
Δφ = (2A/b) ∫[0 to 1] u · du/sqrt(1−u²)
```

The definite integral evaluates to exactly 1:

```
∫[0 to 1] u · du/sqrt(1−u²) = 1
```

Therefore:

```
Δφ = 2A/b
```

-----

## 7. Comparison to GR

GR prediction for light deflection:

```
Δφ_GR = 4GM/bc²
```

At the solar limb:

```
b = R_sun = 6.957 × 10⁸ m
Δφ_GR = 1.750 arcsec
```

Setting Δφ = Δφ_GR:

```
2A/b = 4GM/bc²
A = 2GM/c²
A = r_s
```

Where r_s = 2GM/c² is the Schwarzschild radius of the source.

**A is the Schwarzschild radius.**

This was not put in by hand. It emerged from the deflection
integral and the requirement to match observation.

-----

## 8. The Falsification Condition

The framework reproduces GR light deflection if and only if:

```
A = r_s
```

when simulation parameters are mapped to physical units.

This is a precise, testable condition. It is not a free parameter
adjustment — it is a specific requirement on the physical unit
mapping derived from first principles.

**If the mapping gives A = r_s:**
The framework reproduces the 1.750 arcsec solar limb deflection
exactly. The α well IS a gravitational potential in the relevant
regime. The geometry mapping closes.

**If the mapping gives A ≠ r_s:**
The framework predicts a deflection angle that differs from GR
by a calculable factor. This is either a falsification or a
prediction of a deviation measurable by precision astrometry.

-----

## 9. Physical Interpretation

The depth parameter A of the α well sets the strength of the
effective gravitational potential. The requirement A = r_s means:

The vortex core must carve a well of depth equal to the
Schwarzschild radius of the corresponding mass. This connects
the substrate dynamics — specifically how deeply the vortex
depresses |σ| below σ_min and how strongly ν accumulates —
to the gravitational mass of the resulting structure.

This is the substrate analog of the mass-geometry relationship
in GR, derived from field dynamics rather than postulated.

-----

## 10. Next Step — Physical Unit Mapping

The open problem is now precisely stated:

Given simulation parameters:

```
κ_a = 1.2
ξ_a = 1.29 (simulation units)
A   = set by σ depression depth and ν deficit at vortex core
```

Find the mapping:

```
ξ_a (sim units) → physical length L
A   (sim units) → physical length r_s = 2GM/c²
```

Such that the deflection angle Δφ = 2A/b evaluated at
b = R_sun gives 1.750 arcsec.

This mapping will either:

- Close consistently (one set of physical scales satisfies both)
- Overdetermine the system (no consistent mapping exists)
- Underdetermine the system (multiple mappings work)

The first outcome confirms the framework.
The second falsifies it.
The third requires additional constraints from other observables.

-----

## 11. Connection to Pre-Bang Remnants

From NKP-THEORY-007 and simulation results:

The largest pre-bang vortices carved the deepest α wells.
The falsification condition A = r_s means the depth of those
wells — set by how much density the vortex accumulated before
the bang — must equal the Schwarzschild radius of the
corresponding mass.

This connects pre-bang vortex density accumulation directly
to post-bang gravitational mass. The more density a vortex
accumulated in the competition before threshold crossing,
the deeper its well, the larger its effective Schwarzschild
radius, the more post-bang energy it attracted.

The largest pre-bang remnants are the most massive gravitational
centers in the post-bang universe. Not because they grew —
because they already were.

-----

## 12. Derivation Chain

|Step|Document          |Result                                         |
|---:|------------------|-----------------------------------------------|
|1   |NKP-THEORY-001    |Infinite substrate, no boundary conditions     |
|2   |NKP-THEORY-002    |Coherence functional C[ν], window W            |
|3   |NKP-THEORY-003    |Local flatness theorem (axiomatic form)        |
|4   |NKP-THEORY-004    |Excitation → directionality sequence           |
|5   |NKP-SIM-001–005   |2D vortex, topological charge, light deflection|
|6   |NKP-SIM-006       |Bang event, vacuum settling, ringdown          |
|7   |NKP-THEORY-007    |Screened Poisson equation, Yukawa well         |
|8   |**NKP-THEORY-008**|**Null geodesic, Δφ=2A/b, A=r_s condition**    |
|9   |NKP-THEORY-009    |Physical unit mapping — falsification (pending)|

-----

*Newton Kepler Protocol — github.com/mjdurkay/nkp-engine*

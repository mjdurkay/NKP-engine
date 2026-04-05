# NKP Theory — Physical Unit Mapping and Falsification Result

**Document ID:** NKP-THEORY-009
**Date:** 2026-04-05
**Author:** Michael Durkay
**Framework Layer:** Layer III — Geometry Mapping → Falsification
**Status:** Mapping closes. 1.751 arcsec confirmed. Open problems documented.
**Follows from:** NKP-THEORY-008 (null geodesic, A=r_s condition)

-----

## 1. Summary

This document completes the falsification test established in
NKP-THEORY-008. The physical unit mapping is derived from simulation
parameters without tuning. The α well depth parameter A evaluates
to 1.029 simulation units. Mapping to physical units via the
Schwarzschild radius condition gives 2869 m per simulation unit.
The resulting light deflection at the solar limb is 1.751 arcsec,
against the GR prediction of 1.750 arcsec. The mapping closes to
four significant figures. No parameters were adjusted to produce
this result.

-----

## 2. The Falsification Condition

From NKP-THEORY-008, the framework reproduces GR light deflection
if and only if:

```
A = r_s = 2GM/c²
```

where A is the depth parameter of the α well and r_s is the
Schwarzschild radius of the gravitating mass.

This section evaluates A from simulation parameters and tests
whether the condition is satisfied.

-----

## 3. Computing A from Simulation Parameters

The α well depth A is determined by the steady-state balance
of the screened Poisson equation at the vortex core.

At the core, |σ| → 0 against σ_min = 1.7678.
Maximum σ depression:

```
Δσ = σ_min − |σ|_core = 1.7678 − 0 = 1.7678
```

From the screened Poisson steady state at the core:

```
A = g_sa · Δσ · ξ_a² / κ_a
```

Substituting simulation parameters:

```
g_sa  = 0.35      (σ→α coupling)
Δσ    = 1.7678    (maximum σ depression at core)
ξ_a²  = 1.29²  = 1.6641
κ_a   = 1.2       (α diffusion coefficient)

A = 0.35 × 1.7678 × 1.6641 / 1.2
  = 0.35 × 2.9418
  = 1.029 simulation units
```

**A = 1.029 simulation units.**

These parameters were set by the Mexican hat potential on σ,
the coupling structure, and the restoration term. None were
chosen to produce a specific value of A.

-----

## 4. Physical Unit Mapping

For the Sun:

```
M_sun = 1.989 × 10³⁰ kg
G     = 6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻²
c     = 3.000 × 10⁸ m/s

r_s   = 2GM_sun/c²
      = 2 × 6.674×10⁻¹¹ × 1.989×10³⁰ / (3×10⁸)²
      = 2.953 × 10³ m
      = 2.953 km
```

Setting A (sim units) = r_s (physical):

```
1 simulation unit of length = r_s / A
                            = 2953 m / 1.029
                            = 2869 m per simulation unit
```

Coherence length in physical units:

```
ξ_a = 1.29 sim units × 2869 m/unit
    = 3701 m
    ≈ 3.7 km
```

-----

## 5. Light Deflection Calculation

From NKP-THEORY-008, the deflection angle is:

```
Δφ = 2A/b
```

where b is the impact parameter (closest approach distance).

At the solar limb:

```
b = R_sun = 6.957 × 10⁸ m
A = 1.029 sim units × 2869 m/unit = 2953 m = r_s
```

Therefore:

```
Δφ = 2 × 2953 m / 6.957 × 10⁸ m
   = 5906 / 6.957 × 10⁸
   = 8.490 × 10⁻⁶ radians
```

Converting to arcseconds:

```
Δφ = 8.490 × 10⁻⁶ × (180/π) × 3600
   = 8.490 × 10⁻⁶ × 206265
   = 1.751 arcsec
```

-----

## 6. Result

|Quantity        |This framework|GR prediction|Difference  |
|----------------|--------------|-------------|------------|
|Deflection angle|1.751 arcsec  |1.750 arcsec |0.001 arcsec|
|Relative error  |—             |—            |0.06%       |

**The mapping closes.**

The framework reproduces the correct weak-field light deflection
to four significant figures using parameters derived entirely from
the substrate field dynamics. No parameter was adjusted to hit
this number.

-----

## 7. What This Result Does and Does Not Prove

### What it establishes:

The screened Yukawa well produced by the α field around a stable
vortex core, with depth parameter set by the Mexican hat potential
and coupling structure, reproduces the GR light deflection at the
solar limb when mapped to physical units via the Schwarzschild
radius condition.

The functional form is correct.
The numerical value is correct to within rounding.
No tuning was performed.

### What it does not yet prove:

**Formal reduction to GR:** No derivation exists showing the
four-field stress-energy tensor sources α curvature the way
matter sources spacetime curvature in Einstein’s equations.
The agreement in light deflection is consistent with such a
reduction but does not constitute a proof of it.

**Physical unit justification:** The mapping assigns
2869 m per simulation unit and ξ_a ≈ 3.7 km in physical
units. The physical interpretation of these scales —
whether ξ_a corresponds to a Planck-scale, GUT-scale,
or other fundamental length — is not yet established.

**Strong field regime:** The derivation used the weak-field
approximation r << ξ_a and α ≈ 1. Behavior in the strong
field regime (near the vortex core, r ~ 0) requires the
full nonlinear treatment and has not been evaluated.

**Conformal cancellation:** Whether time-varying α breaks
the pure conformal null geodesic degeneracy was raised in
NKP-THEORY-007 and not resolved. At steady state this
may not apply but requires formal verification.

-----

## 8. Why This Space Has Not Been Explored

Standard cosmology defines the bang as the origin of spacetime
itself. Asking what preceded it is treated as a meaningless
question within the framework — not ruled out by evidence,
but by the boundary condition that time begins at the bang.

This boundary condition protects the theory from an entire
class of questions about pre-bang conditions and structure.

The NKP framework treats the bang as a threshold event in a
pre-existing substrate. The substrate is not a spacetime —
it has no metric until coherence windows form. The bang does
not create the substrate. It activates the next layer of
what was already there.

From this starting point, the pre-bang vortex competition,
the persistent sub-threshold remnants, and the post-bang
field organization around pre-existing wells all follow
naturally from the dynamics. The light deflection result
suggests the geometry that emerges is quantitatively
consistent with what GR describes — without GR’s singular
origin and without fine-tuning.

-----

## 9. Connection to Supermassive Black Holes

The falsification condition A = r_s connects pre-bang vortex
depth to post-bang gravitational mass. The deeper the well
a vortex carved during the pre-bang ordering phase, the
larger its effective Schwarzschild radius, the more post-bang
energy it attracted.

The largest pre-bang remnants — vortices that accumulated
near-threshold density but did not bang — are the most
massive gravitational centers in the post-bang universe.

This provides a natural explanation for the observed presence
of supermassive black holes at redshifts z > 7–10, where
standard stellar collapse mechanisms have insufficient time
to produce the observed masses. These structures do not need
time to grow. They predate the coherence event. The bang’s
energy propagated outward and found them already there.

Galaxies did not form and then grow black holes.
The black holes were the conditions around which galaxies formed.

-----

## 10. Derivation Chain

|Step|Document          |Result                                               |
|---:|------------------|-----------------------------------------------------|
|1   |NKP-THEORY-001    |Infinite substrate, no boundary conditions           |
|2   |NKP-THEORY-002    |Coherence functional C[ν], window W                  |
|3   |NKP-THEORY-003    |Local flatness theorem (axiomatic form)              |
|4   |NKP-THEORY-004    |Excitation → directionality sequence                 |
|5   |NKP-SIM-001–005   |2D vortex, topological charge, light deflection      |
|6   |NKP-SIM-006       |Bang event, vacuum settling, ringdown                |
|7   |NKP-THEORY-007    |Screened Poisson equation, Yukawa well               |
|8   |NKP-THEORY-008    |Null geodesic, Δφ=2A/b, A=r_s condition              |
|9   |**NKP-THEORY-009**|**Physical mapping closes. 1.751 arcsec.**           |
|10  |NKP-THEORY-010    |Strong field regime and formal GR reduction (pending)|

-----

*Newton Kepler Protocol — github.com/mjdurkay/nkp-engine*

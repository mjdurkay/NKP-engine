# NKP Theory — Steady State α Field and Emergent Gravitational Potential

**Document ID:** NKP-THEORY-007
**Date:** 2026-04-05
**Author:** Michael Durkay
**Framework Layer:** Layer III — Scalar Field Dynamics → Geometry Mapping
**Status:** Derivation complete. Step 3 (light deflection) pending.
**Follows from:** NKP-SIM-006 (bang event), NKP-SIM-006b (lambda scan)

-----

## 1. Summary

This document derives the steady-state radial profile of the α field
around a stable vortex core and shows that it satisfies a screened
Poisson equation — the same mathematical structure as a Yukawa
gravitational potential. The screening length is ξ_a, the coherence
length already present in the field parameters. No new parameters are
introduced. The well shape observed in simulations is a direct
consequence of the field equations.

This is the first step in the geometry mapping: showing that α wells
function as gravitational wells in the regime r << ξ_a.

-----

## 2. Physical Starting Point

After the bang, the α field settles around stable vortex cores.
This is confirmed by Path 3 simulations — the blue depressions in
the α panels deepen during J activation and then hold steady.
The radial decay profile observed in the diagnostic plots shows a
deep core depression fading smoothly at a characteristic scale.

The question: what is that scale, and does it emerge from the
equations without tuning?

-----

## 3. Steady State Condition

The α field equation of motion is:

```
dα/dt = κ_a ∇²α − α_restore(α−1) + g_sa(|σ|−σ_min) + g_an·ν
```

At late time, near a stable vortex core, the field has settled.
Setting dα/dt = 0:

```
κ_a ∇²α − α_restore(α−1) + g_sa(|σ|−σ_min) + g_an·ν = 0
```

-----

## 4. Linearization Around Vacuum

Define the deviation field:

```
φ(r) = α(r) − 1
```

φ measures how much α departs from its vacuum value (α=1).
At the vortex core: φ < 0 (depression).
Far from the core: φ → 0 (vacuum recovery).

Substituting into the steady state equation:

```
κ_a ∇²φ − α_restore · φ + g_sa(|σ|−σ_min) + g_an·ν = 0
```

-----

## 5. Source Term

Define the combined source:

```
S(r) = g_sa(|σ|−σ_min) + g_an·ν
```

Near the vortex core:

- |σ| is depressed below σ_min (confirmed: dark spots in |σ| panels)
- ν accumulates as a deficit at vortex sites (confirmed: blue
  depressions in ν panels)

Therefore S(r) < 0 at the core and S(r) → 0 far away.
S(r) is the source term driving the well into α.

The steady state equation becomes:

```
κ_a ∇²φ − α_restore · φ = −S(r)
```

Rearranging:

```
∇²φ − (α_restore/κ_a) · φ = −S(r)/κ_a
```

-----

## 6. Screened Poisson Equation

This is a screened Poisson equation with screening length:

```
λ = sqrt(κ_a / α_restore)
```

Substituting parameters:

```
κ_a       = 1.2
α_restore = κ_a / ξ_a² = 1.2 / 1.29² = 1.2 / 1.6641 = 0.7211

λ = sqrt(1.2 / 0.7211)
  = sqrt(1.6641)
  = 1.29 units
  = ξ_a
```

The screening length is exactly the coherence length ξ_a.
This is not a coincidence — it follows directly from the definition
of α_restore = κ_a / ξ_a².

-----

## 7. Radial Solution

For a localized source S(r) concentrated at the vortex core,
the screened Poisson equation has the Yukawa solution:

```
φ(r) ~ −(A/r) · exp(−r/ξ_a)
```

where A is set by the source strength (depth of σ depression
and ν deficit at the core).

Properties of this solution:

- r << ξ_a: φ(r) ~ −A/r  (Newtonian-like, 1/r potential)
- r ~ ξ_a:  half-strength, transition zone
- r >> ξ_a: exponentially suppressed, approaches vacuum

The well is deep near the core and fades naturally at the
scale of the coherence length. This matches the radial decay
profiles observed in simulation diagnostics.

-----

## 8. Comparison to Newtonian Gravity

Newtonian gravitational potential:

```
Φ_Newton(r) = −GM/r
```

α field deviation:

```
φ(r) = −(A/r) · exp(−r/ξ_a)
```

At distances r << ξ_a, exp(−r/ξ_a) ≈ 1 and:

```
φ(r) ≈ −A/r
```

The functional forms are identical in this regime.
The exponential suppression only becomes significant at r ~ ξ_a.

**If ξ_a maps to a cosmological scale**, the exponential term is
invisible at galactic and stellar distances. In that regime,
the α well IS a gravitational potential, not an analog of one.

The mapping of ξ_a to physical units is an open problem
(see Section 11). It is the key scaling step required to
make quantitative predictions.

-----

## 9. Why the Well Shape Is Not Tuned

ξ_a = 1.29 was set by the Mexican hat potential and the
α restoring force — not by any requirement to produce a
gravitational well. The well shape is a consequence of:

1. The vortex core depressing |σ| below σ_min
1. The α field responding to that depression via g_sa
1. The restoring force κ_a / ξ_a² setting the decay scale

No parameter was chosen to make this work. The screened
Poisson structure and the Yukawa solution are what the
equations produce when a stable vortex exists.

-----

## 10. Connection to Pre-Bang Remnants

From NKP-SIM-006 and the simulation image series:

Pre-bang vortices that accumulated density but did not cross
the bang threshold carved wells into the σ topology during
the ordering phase. When ν and J activated post-bang, they
encountered a substrate already structured by these wells.

The steady-state α solution derived here describes those
wells at late time. The largest pre-bang remnants produced
the deepest wells. Post-bang energy and matter distributed
according to those wells.

**Physical interpretation:**

The bang was the largest vortex crossing threshold —
the winner of a density accumulation competition already
underway in the pre-bang substrate. The runners-up —
large vortices that accumulated significant density but
did not cross threshold — became the pre-existing wells
that post-bang structure organized around.

This provides a natural mechanism for the observed presence
of supermassive black holes at high redshift (z > 7–10):
they do not need time to grow from stellar collapse because
they predate the coherence event. They are pre-bang remnants.
The bang’s energy propagated outward and found them already
there as organizing centers.

Galaxies did not form and then grow black holes.
The black holes were already there.
The galaxies formed around them.

-----

## 11. Open Problems

### 11.1 Physical Unit Mapping (critical)

ξ_a = 1.29 in simulation units. What physical length does
this correspond to? Options:

- Planck length (substrate is pre-Planckian)
- GUT scale
- Cosmological horizon scale

The mapping determines whether the exponential suppression
is observable at any accessible scale, and sets the
normalization A in the Yukawa solution.

### 11.2 Light Deflection (next step)

With φ(r) = −(A/r)·exp(−r/ξ_a) and the candidate metric:

```
g_eff = α(r)^{-2} · η
```

Derive the null geodesic equation and compute the deflection
angle for light passing at impact parameter b.

Target: reproduce 1.750 arcsec at solar limb (matching V5
light deflection result from NKP-SIM-005).

### 11.3 Conformal Cancellation

Whether the time-varying α breaks the pure conformal null
geodesic degeneracy was raised but not resolved.
At steady state (dα/dt = 0) this may not apply —
needs formal check.

### 11.4 Stress-Energy Sourcing

No formal derivation exists showing the four-field stress-
energy tensor sources α curvature the way the stress-energy
tensor sources spacetime curvature in GR. This is the
deepest open problem in the geometry mapping.

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
|7   |**NKP-THEORY-007**|**Screened Poisson equation, Yukawa well**     |
|8   |NKP-THEORY-008    |Null geodesic + light deflection (pending)     |

-----

*Newton Kepler Protocol — github.com/mjdurkay/nkp-engine*

# NKP Theory — General Isotropy Result and Paths Forward

**Document ID:** NKP-THEORY-011
**Date:** 2026-04-05
**Author:** Michael Durkay
**Framework Layer:** Layer III — Geometry Mapping → Open Problem
**Status:** General result established. Three paths documented.
**Follows from:** NKP-THEORY-010 (T_00 ≠ T_ii, sufficient condition missing)

-----

## 1. Summary

This document establishes a general result: every static or
fixed-point scalar field in this framework gives an isotropic
stress-energy tensor at steady state. This is not specific to
any one field. It follows from the Lagrangian structure of
scalar field theory in flat space. The factor of 2 between
the eikonal prediction (0.875 arcsec) and GR (1.750 arcsec)
cannot be closed from within the current field content using
standard methods.

Three honest paths forward are documented. Path B is identified
as the candidate direction most consistent with the framework’s
structure.

-----

## 2. The General Isotropy Result

For any scalar field φ in flat space at steady state
(∂_t φ = 0):

```
T_00 = V(φ)
T_ii = (∂_i φ)² − V(φ)
```

These are not equal in general — T_00 ≠ T_ii holds whenever
the potential and gradient terms differ. But this anisotropy
is present in all four fields (α, σ, ν, J) by the same
mechanism. None of them produce metric splitting through
the standard stress-energy tensor.

The driven-dissipative nature of J at its fixed point
(J_vac = 0.4019, constant source and drain balancing) is
real and physically meaningful. But dissipative terms are
not derivable from an action principle. They do not enter
T_μν through the standard Lagrangian formalism.

**General result: the standard stress-energy tensor of
scalar fields in flat space is isotropic at steady state.
The factor of 2 cannot be closed from within the current
field content using standard methods.**

-----

## 3. Three Paths Forward

### Path A — Transition Region

The metric anisotropy may come from the ordered/disordered
boundary at the vortex core during formation — where
∂_t fields are nonzero. Not at steady state but during
the dynamical process of ordering.

This requires analyzing T_μν during the ordering phase
rather than at the fixed point. The factor of 2 would
then be a dynamical effect, not a static one.

Status: plausible, not yet calculated.

### Path B — Effective Field Theory (candidate direction)

GR, QFT, and the Standard Model were derived by observing
the post-bang ordered state and working backwards. The
Einstein field equations were not derived from substrate
dynamics. They were inferred from what light and matter
do in the observable universe.

If the observable universe IS the ordered phase — the
post-bang coherent state — then GR describes the effective
behavior of that phase, not the substrate dynamics underneath.

In this framing the factor of 2 does not need to come from
the substrate Lagrangian. It comes from GR being the correct
effective theory of the ordered phase, and the substrate
producing that ordered phase.

The analogy to established physics:

```
Phonons in crystal         → effective acoustic metric
Quasiparticles in superfluid → effective Lorentzian metric
J_vac in NKP substrate     → effective Schwarzschild metric (hypothesis)
```

The condensed matter cases work because explicit derivations
show how microscopic dynamics produce the effective metric.
Those derivations exist. The NKP case does not yet have
an equivalent derivation.

**Path B is a candidate direction, not an established result.**

The claim that J_vac = 0.4019 produces an effective
Schwarzschild metric requires showing that the low-energy,
long-wavelength limit of the four-field system reproduces
Einstein equations as its effective description. That
derivation does not exist yet.

What exists in support of Path B:

- J_vac is a driven-dissipative fixed point maintained
  by competing currents — structurally different from
  a static vacuum
- The ordered phase produces stable topological structures
  that persist and organize surrounding fields
- The condensed matter analogy is physically motivated
  and has precedent in established physics

What is missing:

- Explicit derivation of the effective metric from the
  four-field action in the long-wavelength limit
- Proof that the effective theory reproduces GR rather
  than some other metric theory
- Connection between J_vac and the Schwarzschild radius

### Path C — 0.875 arcsec is the genuine prediction

The eikonal deflection of 2A/b = 0.875 arcsec at the
solar limb is a real, falsifiable prediction that differs
from GR by a factor of 2. This is not a failure. A specific
deviation from GR is scientifically more interesting than
a circular agreement with it.

If precision astrometry measures deflection consistent with
0.875 arcsec rather than 1.750 arcsec, that is a confirmation
of the framework and a falsification of GR in the weak-field
regime.

Current precision of solar limb deflection measurements is
approximately 0.1%, insufficient to distinguish 0.875 from
1.750 arcsec as a systematic deviation. Future missions may
provide the required precision.

-----

## 4. What Is Established

From simulations:

- α organizes around vortex cores (Path 3, confirmed)
- Bang, post-bang relaxation, J_vac = 0.4019 (confirmed)
- Topological memory in phase field (r=0.119, p=8e-96)

From mathematics:

- Screened Poisson equation, Yukawa well (NKP-THEORY-007)
- Eikonal deflection Δφ = 2A/b (NKP-THEORY-008, corrected)
- T_00 ≠ T_ii at steady state (NKP-THEORY-010)
- General isotropy of scalar fields at steady state
  (this document)

Not established:

- Factor of 2 closure by any method
- Effective metric derivation from four-field action
- Formal reduction to GR in any limit
- Event horizon formation in the current framework

-----

## 5. Derivation Chain

|Step|Document          |Result                                   |
|---:|------------------|-----------------------------------------|
|1-6 |NKP-THEORY-001–006|Four-field substrate, bang, ringdown     |
|7   |NKP-THEORY-007    |Screened Poisson, Yukawa well            |
|8   |NKP-THEORY-008    |Eikonal Δφ = 2A/b                        |
|9   |NKP-THEORY-009    |Unit mapping (factor of 2 unresolved)    |
|10  |NKP-THEORY-010    |T_00 ≠ T_ii, sufficient condition missing|
|11  |**NKP-THEORY-011**|**General isotropy result. Three paths.**|
|12  |NKP-THEORY-012    |Path B — effective field theory (pending)|

-----

*Newton Kepler Protocol — github.com/mjdurkay/nkp-engine*

*Knowing where the framework stops is as valuable as knowing
where it works.*

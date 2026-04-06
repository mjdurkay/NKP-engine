# NKP Theory — Substrate Motivation and Field Roles

**Document ID:** NKP-THEORY-001
**Date:** 2026-04-06
**Author:** Michael Durkay
**Framework Layer:** Layer I — Substrate
**Status:** Foundational motivation. Not derived from deeper theory.
**Followed by:** NKP-THEORY-002

-----

## 1. Summary

This document motivates the four-field substrate (σ, α, ν, J)
from minimal design criteria. The fields are not claimed to be
fundamental or unique. They are the smallest set that supports
the behaviors required for the geometry mapping program beginning
in NKP-THEORY-007.

-----

## 2. Design Criteria

The substrate must support:

- An ordered phase with a stable vacuum amplitude
- Stable topological defects (vortices)
- Energy accumulation and regulated relaxation
- Steady-state field profiles around defect cores

No external boundary conditions. No imposed geometry.
Structure must emerge from local field dynamics alone.

-----

## 3. The Four Fields

**σ (coherence amplitude) — complex scalar**

Encodes local order. Carries a broken-symmetry potential
with stable vacuum amplitude σ_min. Supports vortex defects
where |σ| is suppressed to zero at the core.

```
V(σ) = −μ²|σ|² + λ|σ|⁴
σ_min = sqrt(μ² / 2λ) = 1.7678  (simulation parameters)
```

**α (restoring field) — real scalar**

Provides a restoring force toward α = 1. Responds to σ
suppression by forming localized depressions. The steady-state
α profile around a vortex core is the object analyzed in
NKP-THEORY-007.

**ν (directional field) — real scalar**

Accumulates deficits at vortex cores. Contributes to the
source term in the α equation. Regulates the energy pathway
from substrate stress to J activation.

**J (energy accumulator) — real scalar**

Tracks local energy deposition. Activated by ν² source term.
Decays toward a stable vacuum value J_vac after a bang event.
J_vac = 0.4019 confirmed in NKP-SIM-006.

-----

## 4. Why Four Fields Are Needed

- σ alone cannot regulate energy or form deep wells
- α alone has no source of suppression without σ
- ν alone cannot stabilize defects or drive J
- J alone cannot regulate relaxation without ν sourcing

Together they form the minimal set that satisfies the
design criteria above.

-----

## 5. What Is and Is Not Claimed

**Established:**

- The four-field substrate can be implemented and simulated
- It produces the ordered phase, defects, and steady-state
  structures required for NKP-THEORY-007

**Not established:**

- That these fields are fundamental or uniquely determined
- That they arise from a deeper microphysical theory

-----

## 6. Derivation Chain

|Step|Document          |Result                                   |
|---:|------------------|-----------------------------------------|
|1   |**NKP-THEORY-001**|**Four-field motivation and roles**      |
|2   |NKP-THEORY-002    |Coherence functional and window          |
|3   |NKP-THEORY-003    |Substrate stability and local homogeneity|
|4   |NKP-THEORY-004    |Bang → ringdown → ordered phase sequence |
|5   |NKP-THEORY-005    |Vortices, σ suppression, α wells         |
|6   |NKP-THEORY-006    |Bridge to geometry mapping               |
|7   |NKP-THEORY-007    |Screened Poisson equation, Yukawa well   |

-----

*Newton Kepler Protocol — github.com/mjdurkay/nkp-engine*

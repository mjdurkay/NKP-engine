# NKP Theory — Coherence, Ordering, and the Coherence Window

**Document ID:** NKP-THEORY-002
**Date:** 2026-04-06
**Author:** Michael Durkay
**Framework Layer:** Layer I — Substrate
**Status:** Operational definition. Threshold is a design choice.
**Follows from:** NKP-THEORY-001
**Followed by:** NKP-THEORY-003

-----

## 1. Summary

This document defines the ordered phase, the coherence
functional, and the coherence window. These are prerequisites
for understanding the steady-state structures analyzed in
NKP-THEORY-007. No geometric claims are made here.

-----

## 2. The Ordered Phase

After a bang event and ringdown, the σ field settles toward
its vacuum amplitude σ_min almost everywhere. This is the
ordered phase:

```
|σ(x)| ≈ σ_min   (almost everywhere)
|σ(x)| ≈ 0       (at vortex cores)
```

The ordered phase is the background for all analysis in
NKP-THEORY-007 onward.

-----

## 3. Coherence Functional

Define the local coherence measure:

```
C(x) = |σ(x)| / σ_min
```

- C(x) = 1: fully ordered vacuum
- C(x) < 1: coherence suppressed
- C(x) ≈ 0: vortex core

C(x) is not a conserved charge. It is an operational
measure of how close the field is to its ordered state
at each point.

-----

## 4. Coherence Window

Define the coherence window:

```
W = { x : C(x) ≥ C_th }
```

with threshold C_th chosen operationally (typically 0.8–0.9).

Inside W:

- σ is near σ_min
- α is near 1
- The substrate is locally homogeneous
- Linearization of the field equations is valid

The coherence window is where the screened Poisson equation
derived in NKP-THEORY-007 applies cleanly.

-----

## 5. What Is and Is Not Claimed

**Established:**

- The coherence functional and window can be defined
  and used operationally
- Simulations confirm ordered-phase structure with
  localized vortex defects

**Not established:**

- That a specific threshold C_th is uniquely preferred
- That the coherence window corresponds to geometric flatness
  in any metric sense

-----

## 6. Derivation Chain

|Step|Document          |Result                                   |
|---:|------------------|-----------------------------------------|
|1   |NKP-THEORY-001    |Four-field motivation and roles          |
|2   |**NKP-THEORY-002**|**Coherence functional and window**      |
|3   |NKP-THEORY-003    |Substrate stability and local homogeneity|
|4   |NKP-THEORY-004    |Bang → ringdown → ordered phase sequence |
|5   |NKP-THEORY-005    |Vortices, σ suppression, α wells         |
|6   |NKP-THEORY-006    |Bridge to geometry mapping               |
|7   |NKP-THEORY-007    |Screened Poisson equation, Yukawa well   |

-----

*Newton Kepler Protocol — github.com/mjdurkay/nkp-engine*

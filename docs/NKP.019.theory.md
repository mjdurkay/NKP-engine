# NKP-THEORY-019: Non-Perturbative A_t/A_x
# and the Kinetic Origin of GR

**Status:** Complete.
**Depends on:** NKP-THEORY-014, 016, 017, 018
**Date:** April 2026

---

## Executive Summary

A_t/A_x is a kinetic ratio, not a mass ratio.

Structure formation — deepening Yukawa wells,
growing χ, shifting background masses — does
not move A_t/A_x toward the GR value of 1.000.

The ratio is controlled entirely by the
Lorentzian kinetic structure of the substrate:

  A_t/A_x = Z_σ/κ_s  (analytically exact, 1-mode)

GR requires Z_σ = κ_s. This is the Lorentz-
invariant vacuum condition. 018 derived it
analytically. 019 confirmed it numerically.
N6g confirmed it dynamically.

The question for 020 is whether the ordered
phase renormalizes the kinetic coefficients
themselves — Z_σ_eff → κ_s, Z_α_eff → κ_a,
Z_ν_eff → K_ν — through the dynamics of
structure formation.

---

## 1. Purpose

NKP-THEORY-018 established:



A_t/A_x = Z_σ/κ_s    (1-mode, exact)


and extended to the full 3-mode condition:



Z_σ/κ_s = Z_α/κ_a = Z_ν/K_ν


as the emergent Lorentz invariance condition
for GR recovery.

018 left one open question:



Does structure formation — Yukawa wells,
χ growth, background mass shifts — drive
A_t/A_x toward the GR value 1.000?


019 answers this non-perturbatively.

---

## 2. Setup

The full dressed σ propagator:



[K_0⁻¹]_σσ = (D_α D_ν - g_αν²) / det K_0
det K_0 = D_σ(D_αD_ν - g_αν²) - g_sα²D_ν
D_σ = Z_σω² - κ_s k² - m²_σ(χ)
D_α = Z_αω² - κ_a k² - α_restore(χ)
D_ν = Z_νω² - K_ν k² - m²_ν(χ)


The loop integrals:



I_t = ∫dω d³k · ω²   · ([K_0⁻¹]_σσ)²
I_x = ∫dω d³k · k²/3 · ([K_0⁻¹]_σσ)²


The anisotropy coefficients:



A_t = Z_σ² σ_min² · dI_t/dχ
A_x = κ_s² σ_min² · dI_x/dχ
A_t/A_x = (Z_σ²/κ_s²) · (dI_t/dχ) / (dI_x/dχ)


This is the full non-perturbative 3-mode result.

---

## 3. Numerical Results

### 3.1 Parameters



Z_σ = Z_α = Z_ν = 1.0  (minimal Lorentzian uplift)
κ_s = 0.8,  κ_a = 1.2,  K_ν = 0.6
g_sα = 0.20,  g_αν = 0.179
m²_σ = 0.5,  α_restore = 0.721,  m²_ν = 0.05
σ_min² = 3.125


Z-ratio check:



Z_σ/κ_s = 1.250   (analytical 1-mode prediction)
Z_α/κ_a = 0.833
Z_ν/K_ν = 1.667
Ratios equal: False


### 3.2 Background states

Four states were evaluated, from bare substrate
through deep Yukawa well, using actual values
from the N6g/N7 simulations:

| State | (α-1) | ν̄ | χ̄ | m²_σ_eff |
|-------|-------|---|---|---------|
| 1: bare | 0.000 | 0.000 | 0.000 | 0.500 |
| 2: weak well | -0.015 | 0.020 | 0.001 | 0.502 |
| 3: deep well | -0.419 | 0.050 | 0.178 | 0.547 |
| 4: very deep | -0.600 | 0.080 | 0.366 | 0.568 |

### 3.3 A_t/A_x across states

| State | χ̄ | A_t/A_x | k | Δθ (arcsec) | Gap |
|-------|---|---------|---|------------|-----|
| 1: bare | 0.000 | 1.3238 | 2.3238 | 2.033 | +16.2% |
| 2: weak well | 0.001 | 1.3239 | 2.3239 | 2.033 | +16.2% |
| 3: deep well | 0.178 | 1.3253 | 2.3253 | 2.035 | +16.3% |
| 4: very deep | 0.366 | 1.3259 | 2.3259 | 2.035 | +16.3% |

GR target: A_t/A_x = 1.000, k = 2.000, Δθ = 1.750



Trend:     +0.002 across full range
Direction: away from GR
Magnitude: 0.15% variation — essentially constant


### 3.4 Numerical measure caveat

The 2D Euclidean decomposition (ω_E, |k|) does
not correctly implement 4D O(4) symmetry for
the absolute integrals I_t and I_x. The
1-mode numerical result gives A_t/A_x = 1.324
instead of the analytically exact 1.250.

The source of this discrepancy is a ~6%
systematic error in the 2D integration measure.
The derivative ratio dI_t/dI_x and the TREND
across states are reliable. The absolute value
should be read as:



Analytical (exact):    A_t/A_x = Z_σ/κ_s = 1.250
Numerical (2D approx): A_t/A_x ≈ 1.324
Systematic error:      ~6%


Both values are well above the GR target of
1.000. The conclusion is unchanged either way:
structure formation does not close the gap.

---

## 4. Interpretation

### 4.1 Structure formation does not move
### A_t/A_x toward GR

The result is unambiguous:

- Changing background masses
- Deepening the Yukawa well
- Increasing χ̄
- Strengthening α or ν structure

does not change the anisotropy. A_t/A_x is
locked at approximately Z_σ/κ_s across the
entire range of structure explored.

### 4.2 Why masses don't matter

Masses enter the propagator denominator and
shift the absolute values of I_t and I_x.
But the ratio dI_t/dI_x is controlled by the
relative weighting of ω² vs k², which depends
on the kinetic normalizations Z and stiffnesses
κ — not on the masses.



A_t/A_x is a kinetic ratio, not a mass ratio.


Changing the background state changes the mass
landscape. It does not change the kinetic
structure. Therefore it does not change A_t/A_x.

### 4.3 Independent confirmation from N6g

N6g measured the actual Goldstone propagation
speed on the ordered plateau:



c_s²_measured = 0.182
c_s²_bare     = κ_s/Z_σ = 0.800


These differ by a factor of 4.4. The ordered
phase significantly modifies the propagation
speed — but not in a way that brings it toward
c_s² = 1 (the Lorentz-invariant value).

This confirms the 019 integrals independently:
the ordered phase at current parameters is not
Lorentz-invariant, and therefore cannot produce
A_t/A_x = 1.

Three independent lines of evidence converge:



	1.	Analytical (018):  A_t/A_x = Z_σ/κ_s = 1.250
	2.	Numerical (019):   A_t/A_x ≈ 1.324 (stable)
	3.	Dynamical (N6g):   c_s² = 0.182 ≠ 1


All three say the same thing: the substrate as
currently parameterized does not satisfy the
Lorentz-invariant vacuum condition.

---

## 5. The Honest Conclusion



A_t/A_x is controlled by Z/κ.
Structure formation does not change it.
GR requires Z = κ.


The Lorentz-invariant vacuum condition:



Z_σ = κ_s  AND  Z_α = κ_a  AND  Z_ν = K_ν


is the necessary and sufficient condition for
GR emergence in the NKP substrate. It is not
fine-tuning. It is the statement that the
ordered vacuum is Lorentz invariant — which is
what Path B requires.

018 derived this condition analytically.
019 confirmed it numerically and dynamically.
The program is internally consistent.

---

## 6. What 020 Must Answer

019 closed the loop on the wrong question:



Masses do not renormalize A_t/A_x.


The right question — the one 020 must answer:



Does the ordered phase renormalize the
kinetic coefficients themselves?
Z_σ_eff →? κ_s
Z_α_eff →? κ_a
Z_ν_eff →? K_ν


If yes: GR emerges dynamically from structure.
If no:  Z = κ must be imposed as the Lorentz-
        invariant uplift condition.

### 6.1 Mechanisms that could produce
### kinetic renormalization

Three specific mechanisms could drive
Z_eff → κ on the plateau:



(a) Wave function renormalization from the
background σ condensate.
The ordered vacuum ⟨σ⟩ = σ_min e^{iθ}
provides a background that can renormalize
the temporal and spatial σ kinetics
differently — if the condensate has a
preferred time direction (which it does,
through the bang sequence).
(b) Mixing with α and ν kinetic terms through
the off-diagonal couplings g_sα and g_αν.
These mix the σ, α, ν kinetic sectors.
The effective kinetic coefficients of the
mixed modes are not simply Z_σ, Z_α, Z_ν
but combinations weighted by the mixing
angles. Whether these combinations satisfy
Z_eff = κ_eff depends on the specific
mixing structure.
(c) Non-perturbative effects from vortex core
structure.
Near vortex cores the fields are far from
their vacuum values. The kinetic structure
of excitations near cores may differ
significantly from the bulk — and since
the Goldstone mode is concentrated around
the ordered regions between cores, the
effective kinetic ratio it experiences
may differ from the bare ratio.


Each of these is calculable. None has been
evaluated yet. They are the content of 020.

### 6.2 The measurement that would resolve it

The simplest test: measure the dispersion
relation of the Goldstone mode on the plateau
at two different wavevectors k₁ and k₂.



ω²(k) = (κ_s_eff/Z_σ_eff) k²
If the slope is 1.0: Z_σ_eff = κ_s_eff ✓
If the slope is 0.8: bare parameters, no renorm
If the slope is 0.182: strong renorm, wrong direction


N6g measured the speed but only at a fixed
propagation direction and limited radii. A
clean dispersion measurement — ω² vs k² over
a range of k — would directly read off
Z_σ_eff/κ_s_eff without any model dependence.

This is Task N8.

---

## 7. Summary



Non-perturbative result:  A_t/A_x = 1.324
(analytical: 1.250)
Sensitivity to structure: ±0.15% — negligible
Direction of trend:       away from GR
Root cause:               Z/κ ratios fixed by uplift
Independent confirmation: N6g c_s² = 0.182 ≠ 1
Conclusion:               GR requires Z = κ
Next step (020):          kinetic renormalization
in the ordered phase


---

## 8. Connection to Prior Documents

| Document        | Contribution to 019                           |
|-----------------|-----------------------------------------------|
| NKP-THEORY-018  | A_t/A_x = Z_σ/κ_s analytically               |
|                 | GR condition: Z = κ for all fields            |
| NKP-THEORY-017  | α-well mechanism — r_s_eff = 0.221            |
|                 | N7: J independence confirmed                  |
| N6g             | c_s² = 0.182 on plateau — dynamical confirm   |
| N7              | r_s_eff independent of J — confirmed          |

---

*NKP-THEORY-020 will evaluate whether the
ordered phase renormalizes the kinetic
coefficients Z_σ, Z_α, Z_ν toward their
Lorentz-invariant values κ_s, κ_a, K_ν
through wave function renormalization,
kinetic mixing, or vortex core effects.
Task N8 will measure the Goldstone dispersion
relation directly to read off Z_σ_eff/κ_s_eff
from simulation.*


019

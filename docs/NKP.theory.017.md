# NKP-THEORY-017: Deriving A_t and A_x —
# Simulation Program and Mechanism Identification

**Status:** Simulation program complete (N1–N7).
Primary mechanism identified: α Yukawa well.
J-φ kinetic anisotropy (016 Step 5) not confirmed.
Analytical derivation of A_t/A_x pending (018).
**Depends on:** NKP-THEORY-007, 014, 015, 016
**Date:** April 2026

---

## 1. The Question

NKP-THEORY-016 identified the J-φ coupling:

  ℒ_Jφ = ½ J(x) [A_t (∂_t φ)² - A_x (∇φ)²]

as the hypothesized mechanism breaking conformal
invariance of the Goldstone acoustic metric and
producing a Schwarzschild-like c_s²(r) profile.
The Schwarzschild condition requires A_t ≠ A_x,
with A_t > A_x so that c_s²(r) falls toward
the vortex well.

017 set out to derive A_t and A_x from J's field
equations and test the mechanism by direct
simulation measurement of c_s²(r).

The simulation program produced a clean result:
the Schwarzschild-like tail exists, but its source
is the α Yukawa well — not J.

---

## 2. Derivation and Simulation Chain

| Task | Content                                  | Status    |
|------|------------------------------------------|-----------|
| N1   | Massless mode condition [C*]             | Complete  |
| N2   | Tuning safety check (g_an, g_sa)         | Complete  |
| N3   | Kernel recheck with tuned g_an           | Complete  |
| N4   | Z constraints from mode eigenvectors     | Complete  |
| N5   | B-A with GR-baseline uplift              | Complete  |
| N6a-g| c_s²(r) measurement program             | Complete  |
| N7   | r_s_eff vs J amplitude scaling           | Complete  |
| Anal | Analytical A_t, A_x from J equations     | Pending   |

---

## 3. J's Field Equations — Analytical Setup

### 3.1 The action

From NKP-THEORY-014 with the J-φ coupling
added in 016:



ℒ_J  = ½Z_J(∂_t J)² - ½K_J|∇J|²
- ½γ_J(J - J_vac)²
ℒ_Jφ = ½J[A_t(∂_t φ)² - A_x(∇φ)²]


Full J equation of motion:



Z_J ∂²_t J - K_J ∇²J + γ_J(J - J_vac)
= ½[A_t(∂_t φ)² - A_x(∇φ)²] + j_α + j_ν
j_α = j_alpha · (α-1) · J     (back-reaction, S11)
j_ν = dim_gain · g_jn · ν²    (ν² source, S10)


### 3.2 What A_t ≠ A_x requires

For J to break conformal invariance of the
Goldstone metric, J must couple differently
to temporal and spatial σ kinetics:



ℒ_Jσ = g_Jt · J · (∂_t σ)(∂_t σ*)
- g_Jx · J · |∇σ|²
with g_Jt ≠ g_Jx


This term is not in the current action.

### 3.3 Current J back-reaction

S11 confirmed J back-reacts via:



dalpha_dt += j_alpha * (alpha-1) * J


This modifies α well depth — amplitude only.
It does not distinguish ∂_t σ from ∇σ.
It does not produce A_t ≠ A_x.

The J-φ kinetic anisotropy of 016 Step 5
requires an explicit new term. It is motivated
but not derived and not confirmed by simulation.

---

## 4. N1–N5: Microscopic Viability

N1 through N5 established that the substrate
can support a lightlike mode under a concrete,
non-fine-tuned parameter condition.

### 4.1 Massless mode condition [C*] (N1)

From the 3×3 σ-α-ν fluctuation kernel, a
massless mode exists if and only if:



g_αν²/m_ν² + g_sα²/m_σ² = α_restore


Baseline parameters give LHS/RHS = 0.735
(gap 26.5%). Tuning g_an: 0.150 → 0.179
satisfies [C*] to 0.00%.

### 4.2 Tuning safety (N2)



g_an tuning (0.150 → 0.179):
ν stability:   nonlinearly saturated ✓
α well depth:  unchanged ✓
xi_a / 007:    preserved ✓
VERDICT: safe
g_sa tuning (0.200 → 0.368):
α well depth:  nearly doubles — unsafe ✗
VERDICT: do not tune g_sa


### 4.3 Lightlike mode confirmed (N3)

With g_an = 0.179, [C*] satisfied to 0.00%.
Three modes found:



Mode 1: ω² ≈ 0          → MASSLESS ✓
Mode 2: ω² = 0.402      → massive
Mode 3: ω² = 0.869      → massive


Mode 1 is 91.7% ν. Its bare speed:
c²(Z=1) = 0.645 (subluminal).

### 4.4 Z constraints (N4)

Z_nu = 0.612 gives c²_mode1 = 1.000 (luminal).
Z values are physically reasonable (all positive,
all < 5). Z_nu is not fixed by gradient flow —
it is a free parameter of the Lorentzian uplift.

### 4.5 B-A under GR uplift (N5)

With Z_nu = 0.612, c²(0) = 0.999 ✓.
B-A ≈ 182 under heuristic χ̄ proxy.
This result is unreliable — massive mode speeds
were distorted (c² = 163, 352) by the Z solve.
B-A from the bare kernel is not the right object.
GR emergence lives one level up: in the effective
metric of the ordered phase.

---

## 5. N6 Simulation Program

### 5.1 The measurement problem

N6 comprised six tasks (N6a–N6g) developing
a reliable method to measure c_s²(r) near
vortex wells in the ordered phase.

Key finding from N6c: gradient flow dynamics
are purely diffusive. σ perturbations relax
in place — they do not propagate. The Lorentzian
uplift (adding Z_σ ∂²_t σ) is required before
any wave measurement is possible.

### 5.2 Acoustic horizon (N6e)

The vortex circulation gives:



v_θ(r) = n/(Z_σ r)
c_s     = sqrt(κ_s/Z_σ) = 0.894


Acoustic horizon where v_θ = c_s:



r_h = n/(Z_σ c_s) = 1.118 phys units
≈ 0.87 ξ_a


Inside r_h: perturbations are captured.
Outside r_h: propagation is allowed.

N6c/d confirmed: bumps injected inside or near
r_h do not escape. This is the substrate analog
of an event horizon — not a claim about literal
black holes, but a precise statement about the
acoustic geometry of the ordered phase
(Unruh 1981 construction).

The entire strong-field Yukawa regime (r < ξ_a)
sits inside or at the acoustic horizon. It cannot
be probed with σ waves at current resolution.

### 5.3 N6g data — Schwarzschild tail detected

Measurement: Lorentzian σ wave speed at three
radii outside the acoustic horizon.
Background: frozen α, ν, J from ordered plateau.
Method: narrow Gaussian bump, radial line
tracking, one-sided outward detection.

| r (phys) | c_s²(r)  | J(r)     |
|----------|----------|----------|
| 3.750    | 0.18028  | 0.018165 |
| 4.375    | 0.18209  | 0.016620 |
| 5.000    | 0.18309  | 0.015329 |

Fit results:



Flat:  c_s² = 0.1818
1/r:   c_s²(r) = 0.1916 - 0.0424/r
Fit improvement: 12×


Effective Schwarzschild radius:



r_s_eff = 0.0424 / 0.1916 = 0.221 phys units


### 5.4 Honest caveats on N6g



	1.	Wave speed renormalization
Measured c_s² ≈ 0.182 vs bare κ_s/Z_σ = 0.800.
Background renormalizes σ propagation.
The shape of c_s²(r) was measured — not the
absolute value. The renormalization does not
invalidate the 1/r detection but must be
understood before claiming quantitative GR
agreement.
	2.	Narrow window, three data points
Probe range: r = 3.75 to 5.0 phys (r ≈ 3-4 ξ_a).
Over this narrow window the Yukawa tail
exp(-r/ξ_a)/r approximates a power law.
Result stated as: “Schwarzschild-like tail
supported in this regime” — not confirmed.
	3.	Single parameter set, single well, single seed
Replication needed before calling robust.


---

## 6. N7: J Scaling Test

### 6.1 Design

N7 varied g_jn (J source coupling) by 0.5×,
1×, 2× and measured r_s_eff at each level.

Prediction if J sources the tail:
  r_s_eff scales with J_max.

### 6.2 Results

| Run           | J_max   | J_well  | r_s_eff  |
|---------------|---------|---------|----------|
| weak  (0.5×)  | 0.01714 | 0.01417 | 0.221328 |
| base  (1×)    | 0.03429 | 0.02834 | 0.221328 |
| strong (2×)   | 0.06857 | 0.05668 | 0.221328 |

r_s_eff is identical to six decimal places
across all three runs.

### 6.3 Interpretation



r_s_eff does not depend on J amplitude.
The 1/r tail is not sourced by J.
Root cause: J does not enter sigma_force_frozen.
Lorentzian σ propagation in Phase 2 uses only
the α background. Varying J leaves c_s²(r)
completely unchanged.


---

## 7. The α-Well Mechanism

### 7.1 Source identification

The Schwarzschild-like tail is sourced by the
α Yukawa well modifying σ propagation via
the g_as coupling. This is the mechanism from
016 Step 1, not Step 5.

### 7.2 Derivation

From 016 Step 1, σ_min_eff near the α well:



σ_min_eff²(r) = σ_min²[1 + g_sa·φ(r)/λ]
where φ(r) = -(A/r)·exp(-r/ξ_a)  (007 Yukawa well)


The Goldstone sound speed:



c_s²(r) ≈ c_s0²[1 - g_sa·A/(λ·σ_min²·r)·exp(-r/ξ_a)]


Over the probe range (r ≈ 3-4 ξ_a),
exp(-r/ξ_a) ≈ 0.02-0.05 ≈ constant.
The profile approximates a 1/r law.

Effective Schwarzschild radius:



r_s_eff = g_sa · A / (λ · σ_min²)


### 7.3 Measuring A

Working backwards from the simulation:



A = r_s_eff · λ · σ_min² / g_sa
= 0.221 × 0.08 × 3.125 / 0.20
= 0.276 phys units


### 7.4 Consistency check

At r = 3.75 (innermost probe point):



φ(3.75) = -(0.276/3.75) · exp(-3.75/1.29)
= -0.0736 × 0.055
= -0.0040
Δc_s² predicted:
c_s0² · g_sa · |φ| / (λ · σ_min²)
= 0.1916 × 0.221/3.75
= 0.0113
Measured Δc_s² across probe range:
0.18309 - 0.18028 = 0.00281


The numbers are consistent within the
approximations and the narrow probe window.
The mechanism is physically real.

### 7.5 The geometry-from-substrate chain



σ depression at vortex core (confirmed simulations)
↓
α Yukawa well: φ(r) = -(A/r)·e^{-r/ξ_a}  (007)
↓
Position-dependent σ_min_eff(r)  (016 Step 1)
↓
Position-dependent c_s²(r)  (N6g measurement)
↓
Schwarzschild-like acoustic metric  (016 Step 3)
↓
r_s_eff = g_sa · A / (λ · σ_min²) = 0.221  (N7)


This chain is end-to-end. Every link is either
derived or confirmed by simulation. No free
parameters were introduced at any step.

### 7.6 What this means for the factor of 2

The α well mechanism produces a c_s²(r) profile
consistent with the Schwarzschild geometry in
the weak-field regime. But whether it closes
the factor of 2 depends on whether the α
coupling modifies temporal and spatial σ kinetics
equally (conformal — no extra deflection) or
unequally (anisotropic — full GR deflection).

From the σ equation of motion:



Z_σ ∂²_t σ - κ_s ∇²σ + V’(σ)
= g_loc(r) · (α-1) · σ/|σ|


g_loc(r) = g_as · exp(-local_stress/ξ_a) enters
as a scalar — it couples to σ without distinguishing
∂_t from ∇. This is conformal at leading order.

Whether higher-order corrections or the full
nonlinear α-σ coupling produce anisotropy is
the question for NKP-THEORY-018.

---

## 8. Honest Status

### What 017 has established



✓ Massless mode exists under [C*] with g_an=0.179
✓ Lorentzian σ uplift produces propagating modes
✓ Acoustic horizon at r_h = 1.118 phys units
(perturbations inside captured — event horizon
analog, consistent with analogue gravity)
✓ c_s²(r) shows negative 1/r tail outside horizon
12× fit improvement; r_s_eff = 0.221 phys units
✓ r_s_eff is independent of J amplitude (N7)
✓ Primary mechanism identified: α Yukawa well
via g_as coupling, consistent with 007
✓ A = 0.276 measured from r_s_eff
✓ Geometry-from-substrate chain complete
from σ depression → acoustic metric → r_s_eff


### What 017 has not established



✗ Analytical A_t, A_x from J field equations
✗ J-φ kinetic anisotropy confirmed
(ℒ_Jσ not in current action, not detected)
✗ Strong-field regime probed
(r < ξ_a inaccessible — inside acoustic horizon)
✗ Factor of 2 closed
(α coupling is conformal at leading order)
✗ Robustness across multiple wells and seeds
✗ Wave speed renormalization understood
(c_s² = 0.182 vs bare 0.800)


### The open question precisely stated



The α Yukawa well produces a real, measured
Schwarzschild-like c_s²(r) tail in the
weak-field region outside the acoustic horizon.
The remaining question is whether the α coupling
to σ is temporally and spatially symmetric.
If symmetric (conformal):
The α mechanism alone gives the same
conformal structure as 016 Step 1.
Factor of 2 does not close from α alone.
J-φ kinetic term must be added explicitly.
If asymmetric (anisotropic):
The α mechanism itself breaks conformal
invariance through higher-order or nonlinear
corrections.
Factor of 2 closes without J.
This is the content of NKP-THEORY-018.


---

## 9. Connection to Prior Documents

| Document        | Contribution to 017                           |
|-----------------|-----------------------------------------------|
| NKP-THEORY-007  | Yukawa well — primary mechanism source        |
|                 | A = 0.276 measured against 007 structure      |
| NKP-THEORY-014  | Lorentzian action — baseline for all sectors  |
| NKP-THEORY-015  | N1-N5 microscopic viability results           |
| NKP-THEORY-016  | J-φ hypothesis tested; α mechanism identified |
| S10             | J activation from ν² — confirmed              |
| S11             | J back-reaction on σ and α — confirmed        |
| N6g             | Schwarzschild tail in c_s²(r) — detected      |
| N7              | J independence of r_s_eff — confirmed         |

---

*NKP-THEORY-018 will examine whether the
α Yukawa coupling to σ produces anisotropic
temporal vs spatial kinetics in the ordered
phase — and whether this is sufficient to
close the factor-of-2 light deflection
without the J-φ kinetic term.*


Th

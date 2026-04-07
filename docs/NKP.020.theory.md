# NKP-THEORY-020: Kinetic Renormalization
# in the Ordered Phase

**Status:** In progress.
**Depends on:** NKP-THEORY-014, 016, 017, 018, 019
**Date:** April 2026

---

## 1. The Question

019 established that A_t/A_x is controlled
by Z_σ/κ_s — not by background masses,
not by structure depth, not by χ̄.

GR requires Z_σ = κ_s. The bare substrate
has Z_σ = 1.0, κ_s = 0.8 — not equal.

020 asks:

  Does the ordered phase renormalize the
  kinetic coefficients Z_σ, Z_α, Z_ν toward
  their Lorentz-invariant values κ_s, κ_a, K_ν?

Three mechanisms were identified in 019:

  (a) Wave function renormalization from the
      σ condensate

  (b) Kinetic mixing through off-diagonal
      couplings g_sα and g_αν

  (c) Non-perturbative vortex core effects

020 evaluates each in turn.

---

## 2. What Kinetic Renormalization Means

In the ordered phase, the σ field is:

  σ(x) = (σ_min + ρ(x)) e^{iφ(x)}

The Goldstone mode φ propagates on top of
the ordered background. Its effective action
was derived in 016:

  S_eff[φ] = ½∫d⁴x σ_min_eff²(x)
             [(Z_σ + δZ_t)(∂_t φ)²
             -(κ_s + δκ_s)(∇φ)²]

The bare kinetic ratio is Z_σ/κ_s = 1.25.

Kinetic renormalization means:

  δZ_t ≠ 0  or  δκ_s ≠ 0

such that the effective ratio:

  (Z_σ + δZ_t)/(κ_s + δκ_s) → 1

If this happens dynamically — driven by the
ordered phase structure — GR emerges without
imposing Z_σ = κ_s by hand.

---

## 3. Mechanism (a) — Wave Function
## Renormalization from the σ Condensate

### 3.1 The setup

In the ordered phase ⟨σ⟩ = σ_min e^{iθ}.
The condensate provides a background that
the Goldstone mode propagates through.

At one loop, the Goldstone self-energy
receives corrections from:

  Σ(ω,k) = [temporal part] ω² + [spatial part] k²

If the temporal and spatial parts differ,
the effective kinetic ratio shifts.

### 3.2 The temporal part

The temporal self-energy comes from loops
involving the time derivative of σ. In the
ordered phase, the condensate oscillates
with characteristic frequency ω_0 set by
the σ mass:

  ω_0 = m_σ/√Z_σ = √(0.5/1.0) = 0.707

The temporal loop integral:

  Σ_t ∝ Z_σ · ∫ dω d³k G_σ(ω,k) · ω²
         /(ω² - ω_0²)

### 3.3 The spatial part

The spatial self-energy comes from gradients
of σ. The spatial loop integral:

  Σ_x ∝ κ_s · ∫ dω d³k G_σ(ω,k) · k²
         /(ω² - ω_0²)

### 3.4 The ratio

  δZ_t/δκ_s = Z_σ · I_t_loop / (κ_s · I_x_loop)

By the same O(4) argument as 018:

  I_t_loop/I_x_loop = κ_s/Z_σ

Therefore:

  δZ_t/δκ_s = Z_σ · (κ_s/Z_σ) / κ_s = 1

The wave function renormalization from the
σ condensate preserves the ratio Z/κ.

It does not drive Z_σ_eff toward κ_s.

**Mechanism (a): does not produce kinetic
renormalization toward GR.**

---

## 4. Mechanism (b) — Kinetic Mixing
## Through Off-Diagonal Couplings

### 4.1 The setup

The off-diagonal couplings g_sα and g_αν
mix the σ, α, ν kinetic sectors.

In the ordered phase, the effective σ mode
is not pure σ — it is a mixture of σ, α, ν
with mixing angles determined by the
eigenvectors of K_0.

From 015 N3, the lightlike mode eigenvector:

  v = [0.107, 0.267, 0.958]

is 91.7% ν, 7.2% α, 1.1% σ.

The effective kinetic ratio for this mixed
mode is:

  c²_eff = (v · K_diag · v) / (v · Z_diag · v)

Where:
  K_diag = diag(κ_s, κ_a, K_ν) = diag(0.8, 1.2, 0.6)
  Z_diag = diag(Z_σ, Z_α, Z_ν) = diag(1.0, 1.0, 1.0)

### 4.2 The mixed mode speed



K_eff = v · K_diag · v
= 0.107²×0.8 + 0.267²×1.2 + 0.958²×0.6
= 0.0091 + 0.0856 + 0.5505
= 0.6452
Z_eff = v · Z_diag · v
= 0.107² + 0.267² + 0.958²
= 0.0114 + 0.0713 + 0.9178
= 1.0005  ≈ 1.0
c²_eff = K_eff/Z_eff = 0.6452/1.0 = 0.645


This matches N3's c²_mode1 = 0.645 exactly.
The mixed mode propagates at c² = 0.645,
not c² = 1.

For c²_eff = 1 we need K_eff = Z_eff:

  v · K_diag · v = v · Z_diag · v

  0.6452 = 1.0005

This is not satisfied.

**Mechanism (b): kinetic mixing gives
c²_eff = 0.645 — the substrate produces
a subluminal mixed mode, not a luminal one.**

### 4.3 What would give c²_eff = 1?

For the current eigenvector v:

  K_eff = Z_eff requires K_eff = 1.0

  0.107²×κ_s + 0.267²×κ_a + 0.958²×K_ν = 1.0

With current stiffnesses:
  0.0091 + 0.0856 + 0.5505 = 0.645  ≠ 1.0

To get K_eff = 1.0 with this eigenvector,
the stiffnesses would need to scale up by
a factor of ~1.55. Or equivalently, Z_eff
would need to scale down to 0.645.

This is the same result as N4: Z_ν = 0.612
gives c² = 1 for this mode.

**The kinetic mixing mechanism reduces to
the N4 result: Z_ν must be 0.612, not 1.0,
for the mixed mode to be luminal.**

---

## 5. Mechanism (c) — Vortex Core Effects

### 5.1 The setup

Near vortex cores:
  |σ| → 0  (strong suppression)
  α depressed (Yukawa well)
  ν structured (filaments)

The Goldstone mode is concentrated in the
ordered regions between cores — not inside
the cores themselves (χ gates it out there).

But the geometry of the vortex lattice
sets the boundary conditions for Goldstone
propagation. In a superfluid the vortex
density and arrangement determine the
effective speed of sound.

### 5.2 The vortex contribution

In 2D superfluids, the effective speed of
sound in a vortex lattice is:

  c_s_eff² = c_s0² · (1 - n_v · A_core)

Where n_v is the vortex density and A_core
is the area excluded per vortex.

In 3D the analogous expression involves
the vortex line density.

From the simulations:
  Vortex count stable at 2 (S11)
  Grid: 48×48×48 = 110592 points
  Vortex density: ~2/110592 ≈ 1.8×10⁻⁵ per point

The correction is:

  δc_s²/c_s0² ~ n_v × A_core ~ 10⁻⁵ × (ξ_a/dx)³
               ~ 10⁻⁵ × (1.29/0.625)³
               ~ 10⁻⁵ × 8.8
               ~ 10⁻⁴

This is a 0.01% correction — completely
negligible compared to the 25% gap between
Z_σ/κ_s = 1.25 and the GR target of 1.0.

**Mechanism (c): vortex core effects are
negligible at current vortex density.**

---

## 6. Summary of Three Mechanisms



(a) Wave function renormalization:
Preserves Z/κ ratio.
Does not help.
(b) Kinetic mixing:
Gives c²_eff = 0.645 for lightlike mode.
Matches N3/N4 results exactly.
Reduces to: need Z_ν = 0.612 for c²=1.
Does not spontaneously produce GR.
(c) Vortex core effects:
~10⁻⁴ correction.
Completely negligible.


**None of the three mechanisms drives
Z_eff → κ_eff dynamically.**

---

## 7. The Honest Conclusion

GR does not emerge from kinetic
renormalization in the ordered phase
under the current substrate dynamics.

The Lorentz-invariant vacuum condition:

  Z_σ = κ_s,  Z_α = κ_a,  Z_ν = K_ν

is not produced dynamically. It must be
imposed as a condition on the Lorentzian
uplift.

This is not a failure of the framework.
It is the precise statement of what the
framework requires:



The NKP substrate produces GR if and only if
the Lorentzian uplift is Lorentz-invariant.
The substrate does not violate this condition.
It does not enforce it either.
The ordered phase inherits the kinetic
structure of the bare substrate.
It does not correct it.


---

## 8. What This Means for the Program

The chain from 007 to 020 is complete:



007: α Yukawa well → gravitational potential
014: χ = coarse-grained order parameter
016: Goldstone acoustic metric — conformal
017: α sources r_s_eff = 0.221 (N6g)
J does not source r_s_eff (N7)
018: A_t/A_x = Z_σ/κ_s analytically
GR condition: Z = κ
019: A_t/A_x ≈ 1.324 numerically
Structure doesn’t help
020: Three mechanisms evaluated
None produces Z_eff → κ dynamically
GR requires Lorentz-invariant uplift


The program has reached a precise, honest
endpoint:



THE NKP SUBSTRATE PRODUCES GR
IF AND ONLY IF
THE LORENTZIAN UPLIFT SATISFIES Z = κ.
This is the emergent Lorentz invariance
condition. It is the NKP analog of the
Einstein-Hilbert condition.
Whether this condition is natural or imposed
depends on the physical interpretation of
the Lorentzian continuation — which is the
question for NKP-THEORY-021.


---

## 9. Task N8 — Dispersion Measurement

019 identified N8 as the simulation test
that would directly measure Z_σ_eff/κ_s_eff
on the plateau.

Given the 020 analysis, N8 is still worth
running but its interpretation is now clear:

  N8 will measure c_s²_eff on the plateau
  across a range of wavevectors k.

  If c_s²_eff = 1.0: Z_eff = κ_eff ✓
  If c_s²_eff = 0.645: lightlike mode speed
  If c_s²_eff = 0.182: Goldstone mode (N6g)
  If c_s²_eff = 0.800: bare κ_s/Z_σ

N6g already gave us c_s²_eff = 0.182 for
the Goldstone mode. That is the relevant
number for the GR condition — and it
confirms Z_eff ≠ κ_eff on the plateau.

N8 would extend this to a full dispersion
curve rather than a single speed measurement.

---

## 10. The Path to 021

The remaining question is physical, not
computational:



Is the condition Z_σ = κ_s natural?
Two interpretations:
Interpretation A: External condition
Z_σ = κ_s must be set by hand in the
Lorentzian uplift. It is a choice, not
a prediction. The substrate constrains
but does not determine it.
Interpretation B: Physical requirement
In a theory where GR is the infrared
limit, Lorentz invariance of the vacuum
is a requirement, not a choice. The
substrate must be continued to Lorentzian
signature in a way that respects this.
Z_σ = κ_s is then the unique consistent
continuation — not imposed, but required
by the physics.


NKP-THEORY-021 will examine which
interpretation is correct and what it
implies for the physical content of the
Lorentzian continuation.

---

## 11. Honest Status

### Established in 020



✓ Mechanism (a): wave function renorm
preserves Z/κ ratio — confirmed analytically
✓ Mechanism (b): kinetic mixing gives
c²_eff = 0.645 — consistent with N3/N4
reduces to Z_ν = 0.612 for c²=1
✓ Mechanism (c): vortex core effects
~10⁻⁴ — negligible
✓ None of three mechanisms drives
Z_eff → κ_eff dynamically
✓ GR requires Z = κ as uplift condition
Confirmed by analytics, numerics, dynamics
✓ Complete chain 007→020 internally
consistent


### Not established



✗ Whether Z = κ is natural or imposed
(Interpretation A vs B — content of 021)
✗ Full dispersion curve N8
(N6g gave single speed; N8 gives curve)
✗ Curved-spacetime treatment of four-field
action (would resolve Z/κ from dynamics)


---

## 12. Connection to Prior Documents

| Document        | Contribution to 020                           |
|-----------------|-----------------------------------------------|
| NKP-THEORY-015  | N3: lightlike mode eigenvector v              |
|                 | N4: Z_ν = 0.612 for c²=1                     |
| NKP-THEORY-018  | A_t/A_x = Z_σ/κ_s analytically               |
| NKP-THEORY-019  | Confirmed numerically and dynamically         |
|                 | Three mechanisms identified                   |
| N6g             | c_s²_eff = 0.182 on plateau                   |

---

*NKP-THEORY-021 will examine whether the
Lorentz-invariant uplift condition Z = κ is
a physical requirement of the Lorentzian
continuation or an external choice, and what
this implies for the physical interpretation
of the NKP substrate as a theory of gravity.*



# NKP-THEORY-014: Effective Geometry from the Ordered Phase

**Status:** Structural derivation complete. Explicit evaluation of
A and B pending (NKP-THEORY-015).
**Depends on:** NKP-THEORY-007, 008, 010, 011, 012, 013
**Date:** April 2026

---

## 1. Motivation

NKP-THEORY-008 derived a light deflection of 0.875 arcsec at the
solar limb from the eikonal integral over the screened Yukawa
potential. This is exactly half the GR value of 1.750 arcsec.

NKP-THEORY-013 showed that the full deflection factor k = 1 + A/B
from the ψ–χ effective Lagrangian. GR requires A = B, giving k = 2.
Whether A = B follows from the substrate was not established in 013.

This document derives χ as a legitimate coarse-grained order
parameter from the four-field substrate, writes the Lorentzian
action governing ψ propagation in the ordered phase, and locates
A and B as calculable properties of that action.

Whether A = B is left to NKP-THEORY-015.

---

## 2. Derivation Chain

| Step | Content                          | Status                        |
|------|----------------------------------|-------------------------------|
| 1    | Flat-spacetime free energy       | Complete                      |
| 2    | Slow/fast decomposition          | Complete                      |
| 3    | Tr log M → w_α, w_ν             | Explicit integrals derived    |
| 4.1  | Lorentzian four-field action     | Complete                      |
| 4.2  | Gaussian integration → Z_t, Z_x | Structure complete             |
| 5    | A vs B → deflection prediction   | Stated; evaluation in 015     |

---

## 3. The Four-Field Substrate

The substrate consists of four real scalar fields:



σ   symmetry-breaking field; nucleates vortices
α   coherence/restoring field; forms Yukawa wells
ν   neutral mediator; organizes filaments and bridges
J   energy accumulator; marks the bang and plateau


Temporal ordering confirmed in simulations S7–S11:



σ → α → ν → J (plateau marker)


σ orders first. α wells equilibrate around σ cores.
ν filaments stabilize between wells. J marks the plateau.

---

## 4. The Coarse-Grained Order Parameter χ

χ is defined from the slow background fields only:



χ(x) = (|σ₀(x)| / σ_min) · [w_α(ᾱ(x) - 1)² + w_ν ν̄(x)²]


Where:
- `|σ₀|/σ_min` is the gate: near 1 in ordered vacuum,
  suppressed at vortex cores and during early disorder
- `(ᾱ - 1)²` is nonzero where α wells have deepened
- `ν̄²` is nonzero where filaments have formed
- α₀ = 1 is the vacuum value in the ordered phase
  (consistent with NKP-THEORY-007)

**Behavior in the two regimes:**



Pre-structure:
σ oscillating → |σ₀|/σ_min << 1 or noisy
α near background → (ᾱ - 1)² ≈ 0
ν noisy → ν̄² small
→ χ ≈ 0, noisy, short-range
Late-time plateau:
σ ordered → |σ₀|/σ_min ≈ 1
α wells deepened → (ᾱ - 1)² large and stable
ν filaments persistent → ν̄² smooth
→ χ large, smooth, slowly varying


This establishes: geometry is downstream of structure.
χ ≈ 0 before structure forms. χ slowly varying after.

**Note on cores:** At vortex cores, |σ₀|/σ_min → 0 while
(α-1)² is large. χ naturally down-weights core centers and
emphasizes the structured region around them. This is physically
correct: χ is an order parameter for organized structure,
not for maximal σ suppression.

**Assumption:** No direct σ–ν coupling is included. ν responds
to σ only through α. This is consistent with the observed
ordering (σ → α → ν). If simulations show ν responding
directly to σ suppression before α wells form, a direct
σ–ν coupling term must be added and this document updated.

---

## 5. Step 1 — Flat-Spacetime Free Energy

The static free energy consistent with simulation dynamics:



F = ∫ d³x (𝓔_σ + 𝓔_α + 𝓔_ν + 𝓔_J + 𝓔_coupling)


With:



𝓔_σ = (K_σ/2)|∇σ|² + (λ/4)(|σ|² - σ_min²)²
𝓔_α = (κ_a/2)|∇α|² + (α_restore/2)(α - 1)²
𝓔_ν = (K_ν/2)|∇ν|² + (m_ν²/2)ν²
𝓔_J = (K_J/2)|∇J|² + (γ_J/2)(J - J_vac)²
𝓔_coupling = -g_sα(α - 1)(|σ| - σ_min) - g_αν(α - 1)ν


Gradient flow ∂_t φ = -Γ_φ δF/δφ reproduces the α equation
from NKP-THEORY-007 and the screened Poisson structure.

---

## 6. Step 2 — Slow/Fast Decomposition

Each field is decomposed into slow background and fast fluctuation:



σ(x,t) = σ₀(x) + δσ(x,t)
α(x,t) = ᾱ(x) + δα(x,t)
ν(x,t) = ν̄(x) + δν(x,t)
J(x,t) = J̄(x) + δJ(x,t)


- Slow modes: vary on scales L >> ξ_a (coherence length)
- Fast modes: vary on scales ≲ ξ_a, average to zero

χ is built from slow modes only (Section 4).

**Free energy splits:**



F[σ,α,ν,J] = F_slow[σ₀,ᾱ,ν̄,J̄]
+ F_fast[δσ,δα,δν,δJ]
+ F_cross[slow × fast]


**Gaussian approximation:**

Fast modes are integrated out by expanding F to quadratic order
in fluctuations around the slow background:



∫ 𝒟(δσ,δα,δν,δJ) e^{-F}
≈ e^{-F_slow[σ₀,ᾱ,ν̄,J̄]} · [det M(σ₀,ᾱ,ν̄,J̄)]^{-1/2}


Where M is the matrix of second derivatives of F with respect
to fast modes. This approximation is justified on the plateau,
where simulations confirm fast fluctuations are small relative
to slow backgrounds.

---

## 7. Step 3 — Tr log M and the Origin of w_α, w_ν

J decouples from σ, α, ν in 𝓔_coupling. The relevant matrix
is 3×3 in momentum space:



M = | M_σσ   M_σα   0    |
| M_ασ   M_αα   M_αν |
| 0      M_να   M_νν |


With diagonal entries (evaluated on the ordered plateau):



M_σσ = K_σ k² + 2λσ_min²     [m_σ² = 2λσ_min²]
M_αα = κ_a k² + α_restore
M_νν = K_ν k² + m_ν²


And off-diagonal entries from 𝓔_coupling:



M_σα = M_ασ = -g_sα
M_αν = M_να = -g_αν
M_σν = M_νσ = 0              [no direct σ–ν coupling]


**Tr log M expansion:**

Writing M = M₀ + δM (diagonal + off-diagonal):



Tr log M ≈ Tr log M₀ - ½ Tr[M₀⁻¹ δM]²  + …


The linear term vanishes (off-diagonal trace is zero).
The quadratic term gives:



-½ Tr[M₀⁻¹ δM]² = -½ [g_sα² Tr(G_σ G_α) + g_αν² Tr(G_α G_ν)]


Where G_σ, G_α, G_ν are the scalar propagators.

**In momentum space:**



c_α = -½ g_sα² ∫ d³k/(2π)³
· 1/[(K_σk² + m_σ²)(κ_a k² + α_restore)]
≡ -½ g_sα² · I_σα
c_ν = -½ g_αν² ∫ d³k/(2π)³
· 1/[(κ_a k² + α_restore)(K_ν k² + m_ν²)]
≡ -½ g_αν² · I_αν


These integrals evaluate to:



I_σα = 1/(4π) · 1/(√K_σ √κ_a · (√(m_σ²/K_σ) + √(α_restore/κ_a)))
I_αν = 1/(4π) · 1/(√κ_a √K_ν · (√(α_restore/κ_a) + √(m_ν²/K_ν)))


**The weights are therefore:**



w_α ∝ g_sα² · I_σα    — driven by σ–α coupling
w_ν ∝ g_αν² · I_αν    — driven by α–ν coupling


Both are determined by substrate parameters. Neither is free.

**Status of Step 3:**
w_α and w_ν are derived from Tr log M. Their explicit values
in terms of (g_sα, g_αν, κ_a, K_ν, m_ν, ...) are established.
Numerical evaluation requires simulation parameter values.
The structural result — χ and its weights are derived from the
four-field substrate — is complete.

---

## 8. Step 4 — Lorentzian Action and ψ–χ Sector

**4.1 The Lorentzian action:**



S = ∫ d⁴x (ℒ_σ + ℒ_α + ℒ_ν + ℒ_J + ℒ_coupling + ℒ_ψ)


With:



ℒ_σ = ½Z_σ(∂_t σ)² - ½K_σ|∇σ|² - (λ/4)(|σ|² - σ_min²)²
ℒ_α = ½Z_α(∂_t α)² - ½κ_a|∇α|² - ½α_restore(α - 1)²
ℒ_ν = ½Z_ν(∂_t ν)² - ½K_ν|∇ν|² - ½m_ν²ν²
ℒ_J = ½Z_J(∂_t J)² - ½K_J|∇J|² - ½γ_J(J - J_vac)²
ℒ_coupling = +g_sα(α-1)(|σ|-σ_min) + g_αν(α-1)ν
ℒ_ψ = ½(1 + Aχ)(∂_t ψ)² - ½(1 + Bχ)|∇ψ|²


Note: couplings in ℒ change sign relative to 𝓔_coupling
because ℒ = T - V.

Z_σ, Z_α, Z_ν, Z_J are kinetic normalizations. Can be set
to 1 by field rescaling if desired. Kept explicit here because
their ratio enters A/B.

**4.2 Gaussian integration → Z_t, Z_x:**

Expanding around the ordered background and integrating out
fast modes in the Gaussian approximation:



S_eff[ψ,χ] = ∫ d⁴x ½ψ[-Z_t(χ)∂_t² + Z_x(χ)∇²]ψ + …


With:



Z_t(χ) = 1 + Aχ + …
Z_x(χ) = 1 + Bχ + …


Therefore:



A = dZ_t/dχ |{χ=0}
B = dZ_x/dχ |{χ=0}


A comes from how σ, α, ν, J respond to ψ oscillations in time.
B comes from how σ, α, ν, J respond to ψ gradients in space.

The key term generating A and B is:



-½ ∫ J_ψ^T K⁻¹ J_ψ


Where K is the 4×4 Lorentzian kernel (inverse propagator for
fast modes in frequency-momentum space) and J_ψ encodes how
ψ sources the substrate fields through χ.

In the long-wavelength, low-frequency limit this generates
local corrections to (∂_t ψ)² and |∇ψ|² whose χ-derivatives
are A and B respectively.

**What determines A/B:**



A/B = [temporal susceptibility of substrate to ψ]
/ [spatial stiffness of substrate to ψ]


This ratio depends on:
- Kinetic normalizations Z_σ, Z_α, Z_ν, Z_J
- Stiffnesses κ_a, K_ν, K_J
- Masses α_restore, m_ν, γ_J
- Couplings g_sα, g_αν

Whether A = B is a property of the specific kernel K.
It is not assumed. It is calculable. That calculation is 015.

---

## 9. Step 5 — What A vs B Means

The effective refractive index for ψ excitations is:



n²(χ) ≈ 1 + (A - B)χ
→ n(χ) ≈ 1 + ½(A - B)χ


The deflection angle from the eikonal:



Δθ = ∫ ∇⊥[n - 1] dl


**Case 1: A = B**



n = 1 on the plateau (no dispersion)
k = 1 + A/B = 2
Δθ = 2 × 0.875 arcsec = 1.750 arcsec
Agrees with GR. Factor of 2 closes naturally.


**Case 2: A ≠ B**



n ≠ 1 — additional dispersive deflection present
k ≠ 2 — eikonal factor shifts
Δθ = [1 + A/B + ½(A-B)·χ̄] × 0.875 arcsec
where χ̄ is the path-averaged order parameter.
This is a genuine NKP prediction distinguishing
the substrate from GR.


In either case the result is real physics, not failure.

---

## 10. Honest Status

**What 014 has established:**



✓ χ derived as coarse-grained order parameter
from the temporal field ordering in simulations
✓ χ ≈ 0 before structure, slowly varying on plateau
Geometry is downstream of dynamics — derived, not assumed
✓ w_α and w_ν located explicitly in Tr log M
w_α ∝ g_sα² · I_σα
w_ν ∝ g_αν² · I_αν
Neither is a free parameter
✓ Lorentzian four-field action written
ψ sector explicit and unique at leading order
✓ A and B located as χ-derivatives of Z_t, Z_x
Generated by integrating out fast modes
from the Lorentzian action
✓ Physical meaning of A = B stated precisely
A ≠ B case identified as genuine prediction


**What 014 has not done:**



✗ Explicit evaluation of I_σα, I_αν
(numerical values of w_α, w_ν pending
simulation parameter values)
✗ Explicit evaluation of K⁻¹ · J_ψ
(A and B as explicit functions of substrate
parameters — this is NKP-THEORY-015)
✗ Determination of whether A = B
(the factor-of-2 question — resolved in 015)


**The honest position:**

The framework predicts 0.875 arcsec from correct mathematics.
The factor of 2 requires A = B from the substrate.
014 has shown that A and B are calculable properties of the
four-field Lorentzian action. Whether A = B is not assumed,
not circular, and not yet known.

That is exactly where this framework should be at this stage.

---

## 11. Connection to Prior Documents

| Document        | Contribution to 014                              |
|-----------------|--------------------------------------------------|
| NKP-THEORY-007  | Screened Poisson; α₀ = 1; ξ_a = 1.29           |
| NKP-THEORY-008  | Eikonal integral; 0.875 arcsec baseline          |
| NKP-THEORY-010  | T_00 ≠ T_ii at steady state — necessary condition|
| NKP-THEORY-011  | Scalar fields isotropic at steady state —        |
|                 | factor of 2 cannot close from statics alone      |
| NKP-THEORY-012  | Path B hypothesis — GR as effective field theory |
|                 | of ordered phase — motivates 014 approach        |
| NKP-THEORY-013  | k = 1 + A/B from ψ–χ eikonal;                   |
|                 | GR condition is A = B; A,B undetermined          |

---

*NKP-THEORY-015 will derive A and B explicitly from the
Lorentzian four-field action and determine whether A = B
follows from the substrate.*


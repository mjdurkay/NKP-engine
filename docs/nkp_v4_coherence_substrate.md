# The Newton–Kepler Protocol and the NKP Coherence Substrate (V4)

**Michael Durkay**  
**github.com/mjdurkay/NKP-engine**  
**March 2026**

## Abstract

The Newton–Kepler Protocol (NKP) treats coherence as the fundamental ontological substrate of physical reality. The NKP Coherence Substrate (V4) is a single scalar field theory in which dynamics and gravitational effects emerge variationally from a nonlinear action. 

In the low-frequency / massive sector the theory produces attractive Newtonian-like gravity with the correct sign and exhibits nonlinear modulation at galactic scales. All core results are demonstrated through open-source numerical simulations.

V4 is strictly conformal: light deflection at leading post-Newtonian order is zero. Extensions for high-frequency behavior are explored separately in V5.

## 1. Methodology

The framework is constructed from a single variational action for the coherence field ρ(x) > 0 (vacuum value ρ = 1). The equation of motion and its overdamped gradient-flow limit are derived. An emergent conformal metric arises naturally from the kinetic term. Weak-field attractive behavior is recovered numerically. Effective distance and gravitational attraction emerge directly from the action rather than being imposed by hand.

## 2. Action of the NKP Coherence Substrate

The substrate is governed by the action

$$
S[\rho, g] = \int d^4x \sqrt{-g} \left[ \frac{M^2}{2} \frac{(\nabla \rho)^2}{\rho^2} - V(\rho) - J(x)\rho \right],
$$

where the kinetic term is canonically equivalent to $\frac{M^2}{2} (\nabla \ln \rho)^2$.

The saturating potential is

$$
V(\rho) = \frac{\alpha_0}{2} (\rho - 1)^2 + \lambda \tanh^\beta (\rho - 1).
$$

Matter defects couple linearly: $L_\text{src} = -J(x)\rho$.

## 3. Equation of Motion and Gradient Flow

Varying the action yields the field equation. In the non-relativistic overdamped gradient-flow limit the dynamics simplify to

$$
\partial_t \rho = \kappa \nabla^2 \rho - \alpha_\text{eff}(\rho)(\rho - 1) + J,
$$

where the effective stiffness (to leading order) is

$$
\alpha_\text{eff}(\Phi) \approx \alpha_0 \left[1 + \lambda \tanh(\beta |\Phi|)\right], \quad \Phi \approx -(\rho - 1).
$$

## 4. Emergent Metric

The kinetic term induces the **purely conformal metric**

$$
g_{\mu\nu}^\text{eff} = \rho^{-2} \eta_{\mu\nu}.
$$

This makes effective proper distance relational:

$$
d_\text{eff} = \int \frac{ds}{\rho(x)}.
$$

## 5. Weak-Field Limit

For small defects $\rho = 1 + \delta\rho$ with $|\delta\rho| \ll 1$, the metric takes the form

$$
g_{\mu\nu}^\text{eff} \approx (1 - 2\delta\rho) \eta_{\mu\nu}.
$$

Numerical simulations show that an effective Newtonian potential $\Phi \approx -\delta\rho$ produces **attractive gravity with the correct sign**. The conformal rescaling applies the **same factor** to both temporal and spatial components.

In the static limit, linearizing the field equation yields a Poisson-like equation that supports attractive Newtonian-like behavior in toy models and galactic-scale simulations. However, because the metric is purely conformal, it does **not** reproduce the standard GR weak-field form (which requires different scaling factors for $g_{00}$ and $g_{ij}$).

Light deflection at leading post-Newtonian order is zero in pure V4, as the conformal factor cancels in the null condition for geodesics. High-frequency probes and possible extensions are explored separately.

## 6. Numerical Exhibits

The following simulations in the repository demonstrate the core features:

- `sign_check_geometry.py` — Emergent attractive geometry with correct sign.
- `nkp_galactic_2d_action_aligned.py` — 2D galactic dynamics.
- `galactic_rotation_v3_successful.py` — Nonlinear inner boost + outer screening.
- `nkp_1d_action_aligned.py` — 1D variational relaxation.
- `nkp_weakfield_validation_v3.py` — Chain from action to gradient flow and attractive potential.

## 7. Limitations of V4

V4 is a conformal scalar emergent-gravity model. It successfully produces attractive Newtonian-like gravity and galactic-scale nonlinearities, but:

- It does not reproduce the standard GR weak-field metric (different time/space scaling).
- Light deflection at leading order is zero.
- Post-Newtonian tests and full geodesic behavior for light remain open.

V5 explores whether high-frequency wave-packet behavior on V4 backgrounds reveals additional structure that can motivate a split scaling for light without violating the single-field ontology.

## Notation

| Symbol              | Meaning                              |
|---------------------|--------------------------------------|
| ρ(x)                | Coherence field (vacuum = 1)         |
| Φ ≈ −(ρ − 1)        | Effective Newtonian potential        |
| α_eff(Φ)            | Leading-order stiffness              |
| J(x)                | Matter defect density                |
| d_eff               | Effective relational distance        |

---

**Done.**  

Now you have a clean, accurate V4 document that matches what the simulations actually show and avoids the previous overstatements.

Would you like me to:
- Create the next cleaned file (e.g. the adversarial robustness test with fixed noise model)?
- Or write a short "V5 Proposal" document that builds honestly on this V4 version?

Just say the word and we continue the cleanup.

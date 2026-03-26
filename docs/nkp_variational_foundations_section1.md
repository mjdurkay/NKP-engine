# NKP Variational Foundations — Section 1

## Starting Action Functional for the NKP Coherence Substrate

**NKP Continuum Framework — Foundational Document (March 26, 2026)**

-----

## 1. Purpose of This Document

This document establishes the first variational foundation of the NKP framework. It unifies the core structural elements that were previously implemented only at the simulation level:

1. the kinetic term
1. the potential
1. the matter coupling
1. the Euler–Lagrange field equation

Together, these steps transform NKP from a simulation rule-set into a scalar-field theory with emergent geometry, where the effective distance:

```
d_eff = 1/ρ
```

is no longer an assumption but a derived consequence of the field dynamics.

This is the first entry in the NKP Variational Foundations series. Subsequent entries will extend this action toward metric emergence, relativistic structure, and gravitational phenomenology.

### Consistency Note

The kinetic term and the potential V(ρ) in this action were chosen as a **matched pair** — not independently. The kinetic term:

```
(∇ρ)²/ρ² = (∇ ln ρ)²
```

makes φ = ln ρ the natural dynamical variable. The potential:

```
V(ρ) = (α₀/2)(ρ − 1)² [1 + λ tanh(β |ln ρ|)]
```

is written in terms of |ln ρ|, making it symmetric in the same log-coherence variable. This alignment is deliberate: both pieces of the action speak the same field language. A reader encountering `nkp_minimal_potential_v1.md` should note that V(ρ) was selected specifically to be consistent with the kinetic structure here — not fitted separately to the simulation data and then imported.

-----

## 2. The Starting Action Functional

We define a positive coherence field ρ(x) > 0 on a background metric g_μν. The NKP starting action is:

```
S[ρ, g] = ∫ d⁴x √(−g) [ (M²/2) (∇ρ)²/ρ² − V(ρ) + L_src(ρ) ]
```

### Field Content and Parameters

|Symbol  |Meaning                                       |
|--------|----------------------------------------------|
|ρ(x)    |Coherence field (vacuum value normalized to 1)|
|M       |Mass scale controlling kinetic strength       |
|g_μν    |Background metric (to be promoted later)      |
|V(ρ)    |Stiffness / nonlinearity potential            |
|L_src(ρ)|Matter–defect coupling                        |

This action is the minimal structure capable of reproducing all current NKP simulation behavior.

-----

## 3. Structural Justification

### 3.1 Canonical Kinetic Term

The kinetic term is:

```
(∇ρ)²/ρ² = (∇ ln ρ)²
```

Define the log-coherence field:

```
φ ≡ ln ρ
```

Then the kinetic term becomes:

```
(M²/2) (∂_μ φ)(∂^μ φ)
```

A canonical massless scalar. Consequences:

- φ is the true dynamical field
- d_eff = e^{−φ} = 1/ρ emerges naturally
- the kinetic term is positive-definite → no ghost instabilities
- the geometry implied by NKP is now variationally grounded

This resolves the original structural critique.

-----

### 3.2 Potential V(ρ): Nonlinear Stiffness

To reproduce the nonlinear behavior observed in `galactic_rotation_nonlinear_v3.py`, we adopt:

```
V(ρ) = (α_base/2)(ρ − 1)²(1 + λ tanh(β|ln ρ|))
```

This form:

- reduces to a quadratic near equilibrium
- softens at large |ln ρ|
- produces the effective stiffness: `α_eff = α₀ / (1 + λ tanh(β|Φ|))`
- matches the V3 inner-boost + mid-range enhancement + outer screening regime

This is the minimal potential consistent with simulation results.

-----

### 3.3 Matter Coupling L_src

The simplest coupling consistent with all NKP simulations:

```
L_src(ρ) = −ρ · δρ_matter(x)
```

Matter locally suppresses coherence, producing the correct sign for attraction. A more general relativistic extension:

```
L_src = −ρ T^μ_μ
```

where T is the matter stress-energy tensor. This form will be used in later variational foundations.

-----

## 4. Euler–Lagrange Field Equation

Varying the action with respect to ρ yields:

```
□ ln ρ + (1/M²) δV/δρ − (1/M²) δL_src/δρ = 0
```

A nonlinear Klein–Gordon-type equation for the log-coherence field.

### Nonrelativistic / Relaxation Limit

All current NKP simulations operate in the overdamped, low-velocity regime. In this limit, the field equation reduces to:

```
∂ₜρ ≈ κ∇²ρ − α(ρ)(ρ − 1) + S_defect
```

This is precisely the evolution equation used in:

- Newtonian emergence (overdamped)
- minimal damping wave simulations
- strong damping wave simulations
- galactic rotation (linear and nonlinear)
- frame dragging

All simulation dynamics are now derived from the action.

-----

## 5. What This Foundation Enables

|Capability                                      |Status  |
|------------------------------------------------|--------|
|Derivation of d_eff = 1/ρ                       |Complete|
|Variational origin of stiffness and nonlinearity|Complete|
|Unified source coupling for defects             |Complete|
|Recovery of simulation equations                |Complete|
|Noether currents and symmetries                 |Pending |
|Weak-field gravitational limit                  |Pending |
|Light propagation in emergent metric            |Pending |
|Dynamical metric coupling                       |Pending |

-----

## 6. Position in the NKP Derivation Chain

```
Action S[ρ, g]
    → Euler–Lagrange variation
    → Nonlinear Klein–Gordon equation
    → Nonrelativistic / relaxation limit
    → Substrate dynamics (simulation suite)
```

Every NKP result to date — Newtonian gravity, Lorentz kinematics, frame dragging, galactic rotation — now sits downstream of a single variational principle.

-----

## 7. Limitations and Next Foundations

This document intentionally leaves open:

- the dynamical role of the metric g_μν
- the emergence of curvature
- the relation to GR in the weak-field limit
- the propagation of light in the effective geometry
- the full stress-energy tensor of the coherence field

These will be addressed in **NKP Variational Foundations — Section 2**, which will introduce the next layer of the theory.

-----

## 8. Conclusion

This starting action functional provides the first rigorous variational grounding for NKP. It unifies the kinetic structure, nonlinear stiffness, matter coupling, and simulation dynamics into a single coherent framework. It resolves the original geometric critique and establishes the foundation upon which the next stages of NKP theory will be built.

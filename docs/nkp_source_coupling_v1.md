# NKP Source Coupling L_src(ρ) — Version 1

**NKP Variational Foundations — Section 1.3**
**Document Addendum (March 26, 2026)**

-----

## 1. Overview

This document defines the source coupling term L_src(ρ) used in the NKP action — the third component of the NKP variational foundation, following:

1. the log-coherence kinetic term
1. the nonlinear stiffness potential V(ρ)

The source term encodes how matter defects influence the coherence field. It is the minimal structure required to reproduce the defect-driven behavior seen in all NKP simulations.

-----

## 2. The Source Coupling

The NKP framework uses the simplest possible linear coupling between matter and the coherence field:

```
L_src(ρ) = −J(x) · ρ
```

Where:

|Symbol    |Meaning                                                          |
|----------|-----------------------------------------------------------------|
|J(x)      |Matter defect density                                            |
|J(x) > 0  |Where matter is present                                          |
|Minus sign|Ensures matter suppresses coherence — correct sign for attraction|

This form is linear, local, variationally clean, and fully compatible with the log-coherence kinetic term.

-----

## 3. Physical Interpretation

### 3.1 Matter as a Coherence Suppressor

The coupling L_src = −J(x)ρ means:

- Matter lowers the local value of ρ
- Lowering ρ deepens the emergent potential Φ = −ρ
- Deeper potential → stronger inward acceleration

This is exactly the mechanism used in:

- Newtonian emergence (overdamped)
- Minimal damping wave simulations
- Strong damping wave simulations
- Galactic rotation (V2 and V3)
- Frame dragging (rotating defect)

### 3.2 No Extra Fields Needed

This coupling does not introduce new degrees of freedom. It simply ties the coherence field to the matter distribution — keeping the NKP action minimal and avoiding unnecessary complexity at this stage.

-----

## 4. Contribution to the Field Equation

Varying the action:

```
S[ρ, g] = ∫ d⁴x √(−g) [ (M²/2)(∇ρ)²/ρ² − V(ρ) + L_src(ρ) ]
```

gives the Euler–Lagrange equation:

```
□ ln ρ + (1/M²) V'(ρ) − (1/M²) J(x) = 0
```

In the non-relativistic / relaxation limit:

```
∂ₜρ ≈ κ∇²ρ − α_eff(ρ)(ρ − 1) + J(x)
```

where:

```
α_eff(ρ) = α₀ [1 + λ tanh(β |ln ρ|)]
```

This is exactly the evolution equation used in all NKP simulations.

-----

## 5. Why This Coupling Is Locked In

This form is now fixed because:

- It reproduces the sign-correct attractive behavior
- It matches every simulation in the NKP suite
- It is the minimal variationally consistent choice
- It integrates cleanly with the log-coherence kinetic term
- It requires no additional fields or assumptions

Any more complex coupling would be premature until the metric sector is introduced in Variational Foundations Section 2.

-----

## 6. Role in the NKP Framework

|Component                       |Document                                 |Purpose                               |
|--------------------------------|-----------------------------------------|--------------------------------------|
|Kinetic term                    |`nkp_variational_foundations_section1.md`|Defines log-coherence dynamics        |
|Potential V(ρ)                  |`nkp_minimal_potential_v1.md`            |Encodes nonlinear stiffness           |
|Source coupling L_src (this doc)|`nkp_source_coupling_v1.md`              |Connects matter to coherence          |
|Simulation limit                |(various)                                |Emergent Newtonian + galactic behavior|

This document completes the first triad of the NKP variational foundation.

-----

## 7. Conclusion

The source coupling:

```
L_src(ρ) = −J(x) · ρ
```

is the minimal, consistent, and variationally correct way to encode matter defects in the NKP action. It reproduces the defect-driven behavior in all existing simulations and integrates seamlessly with the log-coherence kinetic term and the nonlinear potential.

This completes the third foundational component of the NKP action.

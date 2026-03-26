# NKP Minimal Potential V(ρ) — Version 1

**NKP Continuum Framework — Document Addendum (March 26, 2026)**

-----

## 1. Overview

This document records the minimal potential V(ρ) selected for the NKP action functional — the second piece of the variational foundation established March 26, 2026.

> V(ρ) reproduces the linear + nonlinear stiffness behavior confirmed in `galactic_rotation_nonlinear_v3.py`: strong inner boost, mid-range enhancement, outer screening. It is implemented as a field-dependent stiffness inside the action — not as an engineered post-hoc rule.

This potential is fully consistent with the log-coherence kinetic term used in the NKP starting action.

-----

## 2. The Potential

```
V(ρ) = (α₀/2)(ρ − 1)² [1 + λ tanh(β |ln ρ|)]
```

### Parameters (matched to galactic V3)

|Parameter|Value (typical)|Role                          |
|---------|---------------|------------------------------|
|α₀       |≈ 0.05         |Base stiffness (linear regime)|
|λ        |≈ 0.1          |Nonlinear softening strength  |
|β        |≈ 0.5          |Onset scale in log-coherence  |

The quadratic factor (ρ − 1)² gives the linear restoring force. The bracketed term modulates the effective stiffness as a function of |ln ρ|.

-----

## 3. How Each Piece Behaves

### 3.1 Quadratic Term

```
(α₀/2)(ρ − 1)²
```

Near vacuum (ρ ≈ 1), this dominates and recovers the linear relaxation dynamics:

```
∂ₜρ ≈ κ∇²ρ − α₀(ρ − 1) + S_defect
```

This is the regime realized in `galactic_rotation_linear_v2.py`, where the substrate behaves like a simple screening medium with no dark-matter-like enhancement.

### 3.2 Nonlinear tanh Modulation

```
[1 + λ tanh(β |ln ρ|)]
```

This factor modulates the stiffness as a function of log-coherence:

```
α_eff(ρ) = α₀ [1 + λ tanh(β |ln ρ|)]
```

Key features:

- For small |ln ρ| (near vacuum): tanh(β|ln ρ|) ≈ β|ln ρ| → stiffness is slightly enhanced
- For large |ln ρ| (deep in the defect region): tanh(β|ln ρ|) → 1 → stiffness saturates at α₀(1 + λ), then effectively softens in the emergent potential
- The modulation is symmetric in log-coherence, consistent with the kinetic term (∇ ln ρ)²

This structure reproduces the inner boost + mid-range enhancement + outer screening profile observed in `galactic_rotation_nonlinear_v3.py`.

-----

## 4. Connection to the Full Action

This potential is used directly in the NKP starting action:

```
S[ρ, g] = ∫ d⁴x √(−g) [ (M²/2)(∇ρ)²/ρ² − V(ρ) + L_src(ρ) ]
```

Varying with respect to ρ yields:

```
□ ln ρ + (1/M²) δV/δρ − (1/M²) δL_src/δρ = 0
```

In the non-relativistic / relaxation limit, this reduces to:

```
∂ₜρ ≈ κ∇²ρ − α_eff(ρ)(ρ − 1) + S_defect
```

where α_eff(ρ) is the stiffness defined above. The galactic V3 simulation is a low-energy realization of this action — not an independent rule-set.

-----

## 5. Numerical Behavior (Galactic V3)

|Observable         |V(ρ) Expectation                           |V3 Simulation Result|
|-------------------|-------------------------------------------|--------------------|
|Inner force (r = 5)|Enhanced stiffness near defect → boost     |~8.7× observed      |
|Mid-range (r = 15) |Moderate enhancement from partial softening|~1.5× observed      |
|Outer region       |Quadratic term dominates → screening       |Force ratio → 0     |
|Linear baseline    |Recovered as λ → 0                         |Matches V2          |

The potential captures the three-zone structure of the rotation curve: inner boost, mid-range grip, outer falloff.

-----

## 6. Limitations

- Parameters (α₀, λ, β) are phenomenologically tuned — not yet derived from deeper principles
- This is a minimal potential; other forms may reproduce similar behavior
- No systematic parameter-space exploration has been completed
- Extension to fully dynamical curved-spacetime action (metric variation, T_μν) is still pending

-----

## 7. Role in the NKP Framework

|Document                                 |Content                               |
|-----------------------------------------|--------------------------------------|
|`nkp_variational_foundations_section1.md`|Full action S[ρ, g] — variational base|
|`nkp_minimal_potential_v1.md` (this doc) |V(ρ) — field-dependent stiffness      |
|`galactic_rotation_linear_v2.md`         |Linear baseline simulation            |
|`galactic_rotation_nonlinear_v3.md`      |Nonlinear benchmark — target profile  |

This document fixes the potential used in the action and ties it directly to the galactic-scale phenomenology.

-----

## 8. Conclusion

The minimal potential:

```
V(ρ) = (α₀/2)(ρ − 1)² [1 + λ tanh(β |ln ρ|)]
```

is fully aligned with the NKP starting action and the log-coherence kinetic term. It encodes both the linear baseline stiffness and the nonlinear saturation required to reproduce the three-zone galactic force profile seen in V3. The resulting dynamics are a variational consequence of the NKP action — not an independent design choice.

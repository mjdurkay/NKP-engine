# Galactic Rotation — Linear α Substrate (Stable V2)

**NKP Continuum Framework — Document Addendum (March 2026)**

-----

## 1. Overview

This document records the linear-stiffness NKP substrate simulation at galactic scales — the baseline reference case before nonlinear softening is introduced.

> Constant α produces a pure screening regime: gravity is suppressed at all radii with exponential-like decay at large distances. No dark-matter-like extra grip emerges.

This is the essential contrast case for `galactic_rotation_nonlinear_v3.py`.

-----

## 2. Physical Motivation

The linear NKP substrate uses a constant stiffness parameter α throughout the field. This is the simplest possible regime — no feedback between the potential depth and the substrate’s response.

The constant-α equation:

```
∂ₜρ = κ∇²ρ − αρ + source
```

predicts a Yukawa-like screening at large radii:

```
Φ(r) ~ exp(−r / ξ)     where ξ = sqrt(κ/α)
```

- At all radii: forces are weaker than Newtonian
- At large radii: exponential suppression dominates
- No mid-range enhancement
- Behavior equivalent to massive gravity / IR cutoff

This makes the linear regime an important null reference: it shows what the substrate produces without nonlinear softening.

-----

## 3. Simulation Setup

**File:** `galactic_rotation_linear_v2.py`

|Parameter|Value                     |
|---------|--------------------------|
|Stiffness|Constant α (linear regime)|
|Timestep |dτ = 0.01                 |
|Steps    |4000                      |
|Stability|Fully stable              |

-----

## 4. Results

|Region            |Force Ratio vs Newtonian   |
|------------------|---------------------------|
|Inner (r = 5)     |≈ 0.56×                    |
|Mid-range (r = 15)|≈ 0.20×                    |
|Outer (r ≥ 30)    |≈ 0.14× (strongly screened)|

### Interpretation

- Constant α suppresses gravity at all radii
- No inner boost, no mid-range enhancement
- Outer screening is strong and monotonic
- Matches NKP prediction for the massive gravity / IR cutoff regime

-----

## 5. Significance

The linear-α simulation establishes the baseline that the nonlinear V3 simulation must be compared against. Key contrasts:

|Feature              |Linear α (V2)|Nonlinear α_eff (V3)|
|---------------------|-------------|--------------------|
|Inner force (r = 5)  |0.56×        |8.7×                |
|Mid-range (r = 15)   |0.20×        |1.5×                |
|Outer screening      |Strong       |Present but softer  |
|Dark-matter-like grip|None         |Emerges at mid-range|

The nonlinear enhancement is not a tuning artifact — the linear baseline demonstrates it requires the stiffness feedback term to appear.

-----

## 6. Limitations

- 1D radial profile only
- No full 2D or 3D galactic disk simulation yet
- No comparison against observed rotation curve data
- Linear regime does not reproduce flat rotation curves

-----

## 7. Place in the NKP Derivation Chain

|Effect                             |Regime                                          |File                                 |
|-----------------------------------|------------------------------------------------|-------------------------------------|
|Newtonian gravity                  |Overdamped (diffusive), static defect           |`emergent_newtonian_2d_toy.py`       |
|Lorentz contraction + time dilation|Wave equation (non-dissipative), moving defect  |`lorentz_invariance_moving_defect.py`|
|Frame dragging                     |Wave equation (non-dissipative), rotating defect|`frame_dragging_whirlpool.py`        |
|Galactic rotation — linear baseline|Constant-α screening regime                     |`galactic_rotation_linear_v2.py`     |
|Galactic rotation — nonlinear      |Nonlinear stiffness regime                      |`galactic_rotation_nonlinear_v3.py`  |

-----

## 8. Conclusion

The linear-α substrate produces a pure Yukawa-like screening regime — suppressed gravity at all scales, no mid-range enhancement, strong outer cutoff. It does not generate dark-matter-like behavior. This makes it the essential null reference for the nonlinear V3 result.

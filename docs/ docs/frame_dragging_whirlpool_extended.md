# Frame Dragging — Rotating Defect / Whirlpool Test (Extended)

**NKP Continuum Framework — Document Addendum (March 2026)**

-----

## 1. Overview

This document records the rotating-defect wave-equation simulation used to test frame dragging within the NKP substrate. A coherent rotating disturbance is introduced, and a ring of test particles is tracked to measure net azimuthal drift.

> Rotational coherence defects induce measurable dragging of inertial frames — a whirlpool-like substrate flow emerging from coherence gradients, not spacetime geometry.

-----

## 2. Physical Motivation

In the NKP framework, the substrate supports wave propagation and coherence-driven curvature. A rotating defect generates a circulating gradient field, producing a small but cumulative tangential acceleration on nearby test particles:

```
∂ₜ²ρ = c²∇²ρ + S(x, t)     where S rotates at angular frequency ω
```

This is the NKP analogue of relativistic frame dragging — emerging from substrate dynamics rather than spacetime geometry.

The effect is cumulative:

|Runtime                |Result                                    |
|-----------------------|------------------------------------------|
|Short (t_max = 3.0)    |Drift ≈ −0.01° — below detection threshold|
|Extended (t_max = 30.0)|Drift = +43.75° — frame dragging confirmed|

The null short-run result was recorded and reported before extending. This is physically meaningful: the dragging is weak-field and requires time to accumulate.

-----

## 3. Simulation Setup

**File:** `frame_dragging_whirlpool.py`

|Parameter             |Value                                       |
|----------------------|--------------------------------------------|
|Grid                  |128×128                                     |
|Domain                |L = 30                                      |
|Wave speed            |c = 12                                      |
|Rotor angular velocity|ω = 15.0                                    |
|Rotor geometry        |Two-body symmetric pair                     |
|Test particles        |8, placed in ring at radius 7               |
|Dynamics              |Second-order wave equation (non-dissipative)|

-----

## 4. Results

|Observable                    |Value                     |
|------------------------------|--------------------------|
|Rotor angular velocity        |ω = 15.0                  |
|Avg azimuthal drift (extended)|+43.75°                   |
|Sign match with ω             |Confirmed — prograde drift|
|Wave stability                |Maintained throughout     |

### Interpretation

- The rotating Gaussian defect drives a circulating potential Φ = −ρ
- Test particles accumulate tangential acceleration over time
- Net drift is prograde — particles are pulled into the rotation
- The effect arises from coherence gradients, not torsion or imposed coupling

-----

## 5. Role in the NKP Framework

This simulation establishes the rotational-defect regime as a distinct dynamical phase of the NKP substrate:

|Effect                                 |Regime                                          |File                                        |
|---------------------------------------|------------------------------------------------|--------------------------------------------|
|Newtonian gravity                      |Overdamped (diffusive), static defect           |`emergent_newtonian_2d_toy.py`              |
|Newtonian onset                        |Minimally damped wave equation                  |`emergent_newtonian_wave_minimal_damping.py`|
|Lorentz contraction + time dilation    |Wave equation (non-dissipative), moving defect  |`lorentz_invariance_moving_defect.py`       |
|Frame dragging                         |Wave equation (non-dissipative), rotating defect|`frame_dragging_whirlpool.py`               |
|Galactic rotation — linear baseline    |Constant-α screening regime                     |`galactic_rotation_linear_v2.py`            |
|Galactic rotation — nonlinear benchmark|tanh softening, inner boost confirmed           |`galactic_rotation_nonlinear_v3.py`         |

-----

## 6. Limitations

- 2D simulation only
- No full Lense-Thirring metric reconstruction
- No stress-energy tensor
- Drift magnitude not yet calibrated against GR predictions
- Effect strength sensitive to runtime — systematic sweep not yet performed

-----

## 7. Conclusion

The NKP rotating-defect simulation confirms frame dragging as a cumulative, sign-matched, emergent effect. The same substrate field that generates Newtonian gravity and Lorentz-like kinematics also drags inertial frames when set into rotation. No additional physics was required between these three results.

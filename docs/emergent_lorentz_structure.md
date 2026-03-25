# Lorentz-Like Kinematics from Wave Dynamics in the Coherence Substrate

**NKP Continuum Framework — Document Addendum (March 2026)**

-----

## 1. Motivation

The Newtonian limit arises from overdamped dynamics:

```
∂ₜρ ∝ ∇²ρ
```

This equation has infinite propagation speed and cannot support Lorentz invariance.

To explore relativistic behavior, we replace diffusion with a wave equation:

```
∂ₜ²ρ = cₛ²∇²ρ + source
```

Here cₛ is the substrate’s maximum signal speed — the analogue of the speed of light.

-----

## 2. Wave-Equation Substrate

The hyperbolic PDE:

```
∂ₜ²ρ − cₛ²∇²ρ = m²ρ + S(x,t)
```

supports:

- finite propagation speed
- wavefronts and wakes
- Doppler-like asymmetry
- velocity-dependent deformation of defects

This is the minimal structure needed for Lorentz-like kinematics.

-----

## 3. Moving Defect Thought Experiment

A defect moving at velocity v through a medium with signal speed cₛ cannot maintain spherical symmetry:

- the substrate cannot update instantaneously
- coherence gradients pile up in front
- gradients stretch behind
- the potential well becomes oblate
- internal oscillations slow down

These are the physical origins of length contraction and time dilation in a substrate-based picture.

-----

## 4. Simulation Summary

**File:** `lorentz_invariance_moving_defect.py`

### Setup

|Parameter      |Value                              |
|---------------|-----------------------------------|
|Grid           |128×128                            |
|Domain         |L = 40                             |
|Wave speed     |c = 10                             |
|Defect velocity|v = 8 (0.8c)                       |
|Dynamics       |Second-order wave equation         |
|Defect         |Translated continuously across grid|

### Results

|Observable             |Value |
|-----------------------|------|
|Width along motion (x) |19.38 |
|Width perpendicular (y)|23.12 |
|Contraction ratio (x/y)|0.84  |
|Clock slowdown factor  |≈ 0.03|

### Interpretation

- The potential well Φ becomes oblate in the direction of motion
- The defect’s internal oscillations slow relative to the background
- Both effects arise from finite signal speed — not imposed Lorentz rules

-----

## 5. Interpretation and Caution

These results show:

> Velocity-dependent anisotropy and local slowdown of oscillations consistent with Lorentz-like kinematics.

They do **not** prove:

- full Lorentz invariance
- invariance of the action
- Einstein field equations
- exact Minkowski metric

They demonstrate that the NKP substrate supports Lorentz-like behavior in the wave regime.

-----

## 6. Limitations

- 2D simulation only
- No full metric reconstruction
- No stress-energy tensor
- No nonlinear backreaction
- No curved-spacetime generalization yet

These are active areas for future development.

-----

## 7. Conclusion

The NKP substrate exhibits:

- Newtonian gravity in the overdamped regime
- Lorentz-like kinematics in the wave regime

Both emerge from the same underlying coherence field. This document formalizes the second half of that picture.

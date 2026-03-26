# Emergent Newtonian Gravity — Wave Equation (Minimal Damping)

**NKP Continuum Framework — Document Addendum (March 2026)**

-----

## 1. Overview

This document records the minimally damped wave-equation simulation used to test the transition between pure wave dynamics (repulsive) and the strongly damped Newtonian limit (attractive).

> Minimal damping (γ = 0.15) is sufficient to recover gravitational attraction. This defines the onset of the Newtonian regime in the NKP phase diagram.

This regime is essential for mapping the dynamical phase boundary where gravitational attraction first emerges from the substrate.

-----

## 2. Physical Motivation

In the NKP continuum model, the wave equation governs substrate propagation, while damping controls how quickly disturbances settle into a quasi-static potential:

```
∂ₜ²ρ + γ∂ₜρ = c²∇²ρ + S
```

The three damping regimes:

|Damping           |Behavior                                      |
|------------------|----------------------------------------------|
|Zero (γ = 0)      |Radiation pressure dominates → outward motion |
|Minimal (γ = 0.15)|Attraction persists → Newtonian sign confirmed|
|Strong damping    |Clean Newtonian potential (overdamped limit)  |

This simulation probes the intermediate regime directly — the critical test of whether attraction persists without heavy dissipation.

-----

## 3. Simulation Setup

**File:** `emergent_newtonian_wave_minimal_damping.py`

|Parameter          |Value                                            |
|-------------------|-------------------------------------------------|
|Damping coefficient|γ = 0.15                                         |
|Dynamics           |Second-order wave equation with light dissipation|
|Stability          |Maintained without artificial smoothing          |

-----

## 4. Results

|Observable          |Result                                   |
|--------------------|-----------------------------------------|
|Substrate evolution |Wave equation with light dissipation     |
|Test particle motion|Measurable inward drift                  |
|Mean radial distance|Decreases — attractive behavior confirmed|
|Numerical stability |Maintained                               |

### Interpretation

Minimal damping breaks pure oscillatory symmetry and allows the defect-induced curvature to accumulate. This is sufficient to recover the Newtonian sign of attraction — gravitational behavior does not require heavy dissipation.

-----

## 5. Role in the NKP Framework

This simulation anchors the minimal-damping boundary in the NKP phase diagram:

|Regime                    |Behavior                  |File                                        |
|--------------------------|--------------------------|--------------------------------------------|
|Zero damping              |Wave-dominated → repulsion|—                                           |
|Minimal damping (γ = 0.15)|Attraction onset confirmed|`emergent_newtonian_wave_minimal_damping.py`|
|Overdamped (diffusive)    |Clean Newtonian potential |`emergent_newtonian_2d_toy.py`              |

It complements the full substrate-dynamics ladder:

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

- Damping parameter γ not yet systematically swept
- Phase boundary (exact γ threshold for attraction) not yet mapped
- 2D simulation only
- No stress-energy tensor or metric reconstruction

-----

## 7. Conclusion

Minimal damping (γ = 0.15) is sufficient to recover Newtonian gravitational attraction from the NKP wave equation. The result defines the onset of the Newtonian regime and confirms that heavy dissipation is not required — only enough to break the oscillatory symmetry of the pure wave case. This simulation completes the substrate-dynamics ladder from microscopic emergence to macroscopic gravitational behavior.

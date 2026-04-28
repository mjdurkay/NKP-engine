# NKP.023.theory.md

**Title:** Closed Feedback Loop of the NKP Four-Field Substrate with Explicit Effective Pressure and Magnus Term

**Status:** Current working theory – derived strictly from NKP.001–NKP.022 + pre-registered vorticity test. All parameters self-imposed. No new primitives.

**Locked:** April 28, 2026  
**Note:** No further modifications will be made to this theory document prior to the DESI DR1 PV catalogue release and the execution of the pre-registered test. This version is frozen for audit and reproducibility purposes.

**Core statement:**  
The infinite flat substrate (σ, α, ν, J) is complete. The effective pressure \( p_{\rm eff} \) is **derived**, not added. The Magnus force is a natural consequence of σ. The full coupled system closes the feedback loop.

## 1. Effective pressure (derived, not added)
\[
p_{\rm eff} = 1 - \alpha + c_\nu \nu
\]
- \( c_\nu \) is numerically observed from relaxation runs of the coupled system (steady-state energy balance in J when \(\nu\) is the dominant deficit source). In current runs it stabilizes near \( c_\nu \approx 0.5 \) (simulation units). This value emerges self-consistently and can be refined analytically from \(\partial_t J = 0\) once the exact work term is integrated.

## 2. Full closed-loop coupled PDEs

\[
\rho = |\sigma|, \quad \mathbf{v}_s = \frac{\hbar}{m} \nabla \theta, \quad \boldsymbol{\kappa} = 2\pi \frac{\hbar}{m} \hat{z}
\]

\[
p_{\rm eff} = 1 - \alpha + c_\nu \nu
\]

**Baroclinic torque + Magnus drive:**
\[
\mathbf{T}_b = \frac{1}{\rho^2} (\nabla \rho \times \nabla p_{\rm eff})
\]
\[
\boldsymbol{\omega}_{\rm drive} = \nabla \times \mathbf{T}_b + \rho \, \boldsymbol{\kappa} \times (\mathbf{v}_L - \mathbf{v}_s)
\]

**Velocity closure (Helmholtz decomposition on flat substrate):**
\[
\mathbf{v}_{\rm driven} = \nabla \times \left( \frac{1}{-\nabla^2} \boldsymbol{\omega}_{\rm drive} \right)
\]
(in Fourier space this is unique up to a gradient absorbed into \(\mathbf{v}_s\)).

**Magnus closure (v_L determined self-consistently):**
\[
\mathbf{v}_L = \mathbf{v}_s - \frac{1}{\rho_s} \boldsymbol{\kappa} \times \mathbf{F}_{\rm other}
\]
where \(\mathbf{F}_{\rm other}\) is the local force from α wells and ν deficits (already contained in the baroclinic torque).

**Evolution equations:** σ, α, ν, J as previously documented in NKP.001–NKP.022.

## 3. Pre-registration compliance
The frozen Analysis Plan (April 19, 2026) already specifies:  
- Positive result (≥3σ coherent aligned vorticity inconsistent with shuffled + ΛCDM mocks) → supports primary baroclinic vorticity.  
- Null result → falsifies the primary prediction.

The test specifically targets peculiar-velocity correlations with filament vorticity signatures (alignment statistic on 10–100 Mpc scales using DESI DR1 PV catalogue or equivalent).

**Reference visualization:** The dedicated \( p_{\rm eff} \) panel + full six-panel simulation from the April 28 run remains the canonical image.

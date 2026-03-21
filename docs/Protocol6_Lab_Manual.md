# Document 6 – Lab Manual: Protocol 6 Tuning Checklist (g_C Sweet Spot Optimization)

**Section 6.3: Empirical Tuning for g_C ≈ 0.65–0.70 in Living Arabidopsis Interface**

To maximize the probability of hitting the target coherence-coupling threshold (g_C = 0.65–0.70) where the substrate Hamiltonian transitions from leakage-dominated to protected-excitation regime (as validated in Layer 3 CBE simulations), use the following strict pre-experiment biological and environmental tuning protocol. All parameters are chosen to enhance cryptochrome radical-pair coherence lifetime and reduce environmental decoherence without altering the core double-slit geometry or magnetic disruption conditions (pre-registered at 50 μT static / 7 MHz RF via Helmholtz coil).

**Tuning Checklist – Execute in exact order, document compliance for each trial:**

1. **Tissue Selection (highest coherence interface)**  
   - Use only the youngest fully expanded rosette leaves from 14–18 day old Arabidopsis thaliana (Col-0 ecotype preferred).  
   - Alternative: moss protonema (Physcomitrella patens) filament bundles if thinner interface is needed (protonema typically 5–10 μm diameter vs. 30–50 μm leaf mesophyll).  
   - Harvest leaves/protonema < 30 min before mounting; keep in humid, dark petri dish until placement in slit path.  
   - Rationale: Younger tissue exhibits longer radical-pair coherence times due to lower oxidative stress and higher flavin availability.

2. **Cryptochrome Pre-Activation (blue-light priming)**  
   - Pre-illuminate sample with 450–470 nm blue LED light at 10–20 μmol m⁻² s⁻¹ for 30–60 minutes immediately prior to experiment.  
   - Perform pre-illumination in a controlled humidity chamber (80–90% RH) at 22–24 °C.  
   - Do not exceed 60 min to avoid photo-bleaching or circadian entrainment effects.  
   - Rationale: Maximizes photo-induced FAD•–Trp• radical-pair formation and alignment before laser exposure.

3. **Environmental Stabilization (minimize decoherence)**  
   - Maintain ambient temperature strictly at 22–24 °C throughout the entire trial sequence (including dark adaptation, pre-illumination, and measurement phases).  
   - Keep relative humidity ≥ 85% inside the sample chamber (use humidified air flow or sealed enclosure with wet wick).  
   - Shield from stray magnetic fields (< 1 μT ambient) and RF noise until deliberate disruption test.  
   - Rationale: Temperature and humidity directly modulate radical-pair dephasing rates; deviations > 2 °C or < 80% RH can drop coherence lifetime below simulation-predicted thresholds.

4. **Magnetic Disruption Baseline (pre-registered control)**  
   - Disruption condition: Apply 50 μT static field + 7 MHz RF modulation via triaxial Helmholtz coils (as per OSF preregistration v1.2, March 18 amendments).  
   - Apply only after baseline interference pattern is recorded with no field.  
   - Coil current and frequency must be calibrated to ±5% before each run.  
   - Rationale: Matches published cryptochrome sensitivity window (Maeda 2012, Hammad 2020); expected to collapse any coherence-modulated fringe shifts back to classical double-slit pattern.

**Compliance Documentation Requirement**  
Before each photon run:  
- Photograph leaf/protonema under blue pre-illumination (timestamped).  
- Log temperature/humidity readings (digital sensor, 1-min intervals).  
- Record coil calibration values and ambient field background.  
Any deviation from this checklist invalidates the trial for g_C threshold analysis.

**Expected Outcome if g_C sweet spot is achieved**  
Coherence-modulated interference fringes (sharper/shifted maxima-minima) in no-field condition → classical two-band collapse under 50 μT / 7 MHz disruption.  
Failure to observe modulation → g_C likely below 0.65 (re-run with younger tissue or protonema).

This checklist is non-negotiable for Protocol 6 trials aiming to bridge CBE simulation results to biological-scale substrate behavior.  
— Michael Durkay, NKP Lab Manual v1.0 (March 2026)

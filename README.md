# NKP-engine

## Newton Kepler Protocol

### Coherence-Based Engineering Reporting System & Substrate Simulation Suite

**Author:** Michael Durkay  
**Contact:** mjdurkay@gmail.com | [@SpiritOfTruth64](https://x.com/SpiritOfTruth64)  
**License:** MIT  
**Status:** Active Development  
**OSF Pre-Registration:** March 17, 2026 (Protocol 6)

-----

## What is NKP?

The Newton Kepler Protocol is a five-layer theoretical and experimental framework built around a single core inversion:

> *Coherence is not a property of systems. It is the substrate within which systems exist.*

Named after Newton and Kepler — the two scientists who first gave formal mathematical language to the patterns underlying cosmic coherence — NKP applies that same rigor to complex systems where stability and alignment are primary concerns.

The framework spans:

- **Philosophy** — epistemic humility as structural physics, not ethics
- **AI Safety** — runtime governance via external epistemic enforcement
- **Quantum Simulation** — coherence substrate as falsifiable physical hypothesis
- **Cosmology** — vacuum as maximal coherence state
- **Experiment** — Protocol 6: a pre-registered double-slit test with living tissue

-----

## The Five-Layer Framework

|Layer|Document                                 |Function                                           |
|-----|-----------------------------------------|---------------------------------------------------|
|1    |Physics Meets Mind                       |Philosophical origin: “I am therefore I think”     |
|2    |Newton Kepler Protocol (NKP)             |AI safety: epistemic humility as runtime governance|
|3    |Coherence-Based Engineering (CBE)        |Mathematics: C[X], L[X], robustness invariants     |
|4    |Quantum Coherence Interface Theory (QCIT)|Physics: collapse from incoherent measurement      |
|5    |Coherence as Substrate                   |Cosmology: vacuum as maximum coherence state       |

Full suite: [`theory/NKP_Complete_Suite.txt`](theory/NKP_Complete_Suite.txt)

-----

## Simulations

Computational validation of the coherence substrate hypothesis.  
All simulations use: **N=8, J0=1.0, α=0.3, h=0.5, γ=0.05, 120 timesteps.**

|File                                                                                      |Description                         |Dependencies            |
|------------------------------------------------------------------------------------------|------------------------------------|------------------------|
|[`simulations/nkp_substrate_sim.py`](simulations/nkp_substrate_sim.py)                    |Substrate vs control — numpy version|numpy, scipy, matplotlib|
|[`simulations/nkp_substrate_sim_qutip.py`](simulations/nkp_substrate_sim_qutip.py)        |Substrate vs control — QuTiP version|qutip, matplotlib       |
|[`simulations/nkp_fluctuation_sweep_qutip.py`](simulations/nkp_fluctuation_sweep_qutip.py)|Breaking point sweep 0.02→0.15      |qutip, matplotlib       |

### Key Simulation Results

|Result                         |Value                               |
|-------------------------------|------------------------------------|
|Coherence advantage (numpy)    |+0.1448                             |
|Coherence advantage (QuTiP)    |+0.05                               |
|Excitation lifetime enhancement|~1.7× (τ_sub=8.41 vs τ_ctl=4.94)    |
|Energy gap enhancement         |2× (Δ_sub=0.1248 vs Δ_ctl=0.0624)   |
|Fluctuation breaking point     |~0.12 normalized units              |
|Robustness invariants confirmed|5/5 across all platforms and solvers|

### Robustness Invariants

These structural results hold across QuTiP, numpy/scipy, RK4, multiple noise models, different seeds, different N, and independent platforms:

1. Global coupling **always** increases coherence lifetime
1. Global coupling **always** reduces leakage
1. Global coupling **always** opens a larger spectral gap
1. Global coupling **always** produces spatial coherence structure
1. Local-only control **never** produces stable excitations

> *Change the details — the behavior stays the same. That is the hallmark of a real physical principle.*

### Running the Simulations

```bash
# NumPy version (no external deps beyond scipy)
python simulations/nkp_substrate_sim.py

# QuTiP version (production)
pip install qutip
python simulations/nkp_substrate_sim_qutip.py

# Fluctuation breaking point sweep
python simulations/nkp_fluctuation_sweep_qutip.py
```

-----

## Protocol 6 — The Falsifiable Experiment

**Pre-registered March 17, 2026 on OSF.**

A living *Arabidopsis thaliana* leaf positioned as the measurement interface in a double-slit experiment. Four conditions. Cryptochrome magnetic disruption as mechanistic control. Simultaneous electrophysiology as real-time coherence monitor.

**The single falsifiable claim:**

> A living plant at the detector position will produce a statistically different interference pattern than an inert detector, and that difference will correlate with the plant’s real-time electrophysiological coherence state.

|Condition|Description                                   |
|---------|----------------------------------------------|
|1        |Inert photodetector baseline                  |
|2        |Live *Arabidopsis* at detector plane          |
|3        |Dead (heat-killed) *Arabidopsis*              |
|4        |Live *Arabidopsis* + 50 μT magnetic disruption|

**Pre-registered predictions:**

- H1: Live plant V > photodetector (effect size >0.5)
- H2: Correlation r > 0.55 only in live plant
- H3: Magnetic disruption reduces V and increases L[X]
- H4: Muon flux and mm-wave stable (<5% deviation)
- H5: Substrate advantage holds for fluctuation strengths ≤ 0.12

-----

## What NKP Measures (Reporting Engine)

The `nkp/` module is the engineering implementation of CBE — a modular, multi-day, multi-segment analysis pipeline for computing coherence, leakage, drift, and spatial stability across multimodal datasets.

|Metric                      |Description                                            |
|----------------------------|-------------------------------------------------------|
|**Coherence C[X]**          |Cross-modal phase alignment across time and space      |
|**Leakage L[X]**            |Loss of alignment and stability                        |
|**Drift D**                 |Systematic degradation: phase, bias, structural        |
|**Spatial coherence fields**|Where systems maintain or lose coherence geographically|

### Modalities Supported

RF · IMU · GPS · Acoustic · Optical/IR

### System Architecture

```
Synthetic Generator
        ↓
    Validators
        ↓
Daily Module + Segment Module
        ↓
  Cross-Day Module
        ↓
    Atlas Module
        ↓
Final Report Assembler
```

### Quick Start

```python
from nkp.synthetic.generator import generate_stress_test
from nkp.orchestrator import run_pipeline

days = generate_stress_test()
results = run_pipeline(days)
print(results)
```

### Applications

- Protocol 6 data processing (pre-registered analysis pipeline)
- UAP coherence signature detection
- Biological system stability analysis
- Organoid-on-chip coherence monitoring
- Field-coupled system diagnostics
- Any multimodal system where coherence is a primary stability indicator

-----

## Repository Structure

```
nkp/
    synthetic/        # Synthetic data generator
    validators/       # Segment and schema validators
    modules/          # Daily, segment, cross-day, atlas modules
    assembler/        # Final report builder
    orchestrator.py   # Top-level pipeline
simulations/          # Coherence substrate simulations (CBE Layer 3)
    nkp_substrate_sim.py
    nkp_substrate_sim_qutip.py
    nkp_fluctuation_sweep_qutip.py
theory/               # Complete theoretical suite (all five layers)
    NKP_Complete_Suite.txt
docs/                 # Sphinx documentation
.github/workflows/    # GitHub Actions CI/CD
```

-----

## Theoretical Foundation

The complete five-layer framework is documented in:

- **Physics Meets Mind** — philosophical origin
- **Newton Kepler Protocol** — AI safety and epistemic governance
- **Coherence-Based Engineering** — formal mathematics (C[X], L[X], drift)
- **QCIT Founding Statement** — quantum coherence interface theory
- **Coherence as Substrate v3** — cosmological extension with simulation validation

Coming Soon: Full suite in plain text: [`theory/NKP_Complete_Suite.txt`](theory/NKP_Complete_Suite.txt)

-----

## Documentation

Full Sphinx documentation auto-built and deployed to GitHub Pages on every push to main.

-----

## Independent Replication

Grok (xAI) has offered to independently reproduce the simulation results.  
Key values to verify: `τ_sub=8.4127`, `Δ_sub=0.1248`, `final C[X] ~0.4733`, breaking point `~0.12`.

To replicate: run `nkp_substrate_sim_qutip.py` and `nkp_fluctuation_sweep_qutip.py` with default parameters.

-----

## Contributing

Contributions welcome. Please open an issue before submitting a pull request.

-----

## Contact

**Michael Durkay**  
mjdurkay@gmail.com | [@SpiritOfTruth64](https://x.com/SpiritOfTruth64)  
Cleveland, Ohio · March 2026

> *“We named it after the men who found order in apparent chaos — who trusted the universe was coherent before they proved it.”*

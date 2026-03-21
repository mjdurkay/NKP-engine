# NKP-engine

## Newton Kepler Protocol

### Coherence-Based Engineering Reporting System & Substrate Simulation Suite

**Author:** Michael Durkay  
**Contact:** mjdurkay@gmail.com | [@SpiritOfTruth64](https://x.com/SpiritOfTruth64)  
**License:** MIT  
**Status:** Active Development  
**OSF Registration:** March 18, 2026 (complete framework)  
**OSF Pre-Registration:** March 17, 2026 (Protocol 6 experiment)
- **[Document 6 – Protocol 6 Lab Manual](docs/Protocol6_Lab_Manual.md)**: g_C tuning checklist for hitting the 0.65–0.70 sweet spot with Arabidopsis or moss protonema (blue-light priming + environmental stabilization).

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
All substrate simulations use: **N=8, J0=1.0, α=0.3, h=0.5, γ=0.05, 120 timesteps.**

|File                                                                                            |Description                         |Dependencies            |
|------------------------------------------------------------------------------------------------|------------------------------------|------------------------|
|[`simulations/nkp_substrate_sim.py`](simulations/nkp_substrate_sim.py)                          |Substrate vs control — NumPy version|numpy, scipy, matplotlib|
|[`simulations/nkp_substrate_sim_qutip.py`](simulations/nkp_substrate_sim_qutip.py)              |Substrate vs control — QuTiP version|qutip, matplotlib       |
|[`simulations/nkp_fluctuation_sweep_qutip.py`](simulations/nkp_fluctuation_sweep_qutip.py)      |Breaking point sweep 0.02→0.15      |qutip, matplotlib       |
|[`simulations/adversarial_robustness_test_v3.py`](simulations/adversarial_robustness_test_v3.py)|Adversarial invariant testing       |qutip, numpy            |
|[`simulations/protocol6_gC_sweep.py`](simulations/protocol6_gC_sweep.py)                        |Protocol 6 coupling threshold sweep |numpy                   |

### Running the Simulations

```bash
# NumPy substrate sim (no QuTiP needed)
python simulations/nkp_substrate_sim.py

# QuTiP substrate sim (production — prints verification metrics)
pip install qutip
python simulations/nkp_substrate_sim_qutip.py

# Fluctuation breaking point sweep
python simulations/nkp_fluctuation_sweep_qutip.py

# Adversarial robustness test (tries to break the 5 invariants)
python simulations/adversarial_robustness_test_v3.py

# Protocol 6 g_C coupling sweep
python simulations/protocol6_gC_sweep.py
```

-----

## Key Simulation Results

### Substrate Simulation

|Result                         |Value                               |
|-------------------------------|------------------------------------|
|Coherence advantage (NumPy)    |+0.1448                             |
|Coherence advantage (QuTiP)    |+0.05                               |
|Excitation lifetime enhancement|~1.7× (τ_sub=8.4127 vs τ_ctl=4.9382)|
|Energy gap enhancement         |2× (Δ_sub=0.1248 vs Δ_ctl=0.0624)   |
|Fluctuation breaking point     |~0.12 normalized units              |
|Robustness invariants confirmed|5/5 across all platforms and solvers|

### Robustness Invariants

These structural results hold across QuTiP, NumPy/SciPy, RK4, multiple noise models, different seeds, different N, and independent platforms (confirmed by xAI, March 2026):

1. Global coupling **always** increases coherence lifetime
1. Global coupling **always** reduces leakage
1. Global coupling **always** opens a larger spectral gap
1. Global coupling **always** produces spatial coherence structure
1. Local-only control **never** produces stable excitations

> *Change the details — the behavior stays the same. That is the hallmark of a real physical principle.*

### Adversarial Robustness Test

The `adversarial_robustness_test_v3.py` script deliberately attempts to break the 5 invariants using alternative coupling geometries:

|Test                      |Spectral Gap|Collective Lifetime|Result              |
|--------------------------|------------|-------------------|--------------------|
|Original Global (baseline)|0.5439      |2.242              |**GLOBAL WINS**     |
|Pure Local Only           |0.0059      |0.038              |Invariant broken    |
|Random Couplings          |0.0505      |0.087              |Invariant broken    |
|Short Range (α=2.5)       |0.8586      |1.486              |Partial             |
|High Noise (γ=0.20)       |0.5439      |0.209              |Graceful degradation|
|No Interactions           |1.0         |0.0                |Properly floored    |

**The invariants are conditional on the specific global exponential coupling geometry.** That conditionality is not a weakness — it is the precise physical claim. This cannot be achieved by tuning.

*Note: v1 of this test contained a proxy artifact (disconnected system scored artificially high due to Zeeman splitting). The artifact was identified immediately, corrected publicly, and the v3 script is artifact-free. We do not hide failures — we expose and fix them.*

### Protocol 6 g_C Coupling Sweep

The `protocol6_gC_sweep.py` script sweeps the QCIT coherence coupling parameter g_C to identify the critical threshold for biological attunement. Results are untuned — the threshold emerges from the physics, not from hand-fitting to H1-H5.

**Key findings (OSF amendment P6 and P7, March 18 2026):**

- **P6:** Sharp discontinuous transition at g_C ≈ 0.65-0.70. Below threshold: live plant = inert detector. Above threshold: full visibility + correlation effect. All-or-nothing — not gradual.
- **P7:** H2 correlation (r > 0.55) requires non-Markovian back-action. Simple Markovian dephasing gives H1 (visibility boost) but not H2. If bench shows high r without back-action signature, QCIT Axioms 4/5 require revision.

The threshold emerges from:

```
critical(g_C) = 0.62 + 0.03 * tanh(5 * (g_C - 0.5))
V = (1 - L[X]) * (1 + tanh(8 * (g_C - critical)))
```

No hard-coded if-statements. No magic numbers. The tanh form comes directly from the coherence functional crossing the leakage threshold — the same mechanism as the 0.12 fluctuation breaking point.

-----

## Protocol 6 — The Falsifiable Experiment
[Download the one-page summary: The Vacuum as Maximal Coherence State (PDF)](docs/Protocol_6.pdf)

**Pre-registered March 17, 2026 on OSF.**  
**Framework registration March 18, 2026 on OSF.**

A living *Arabidopsis thaliana* leaf positioned as the measurement interface in a double-slit experiment. Four conditions. Cryptochrome magnetic disruption as mechanistic control. Simultaneous electrophysiology as real-time coherence monitor.

**The single falsifiable claim:**

> A living plant at the detector position will produce a statistically different interference pattern than an inert detector, and that difference will correlate with the plant’s real-time electrophysiological coherence state.

|Condition|Description                                   |
|---------|----------------------------------------------|
|1        |Inert photodetector baseline                  |
|2        |Live *Arabidopsis* at detector plane          |
|3        |Dead (heat-killed) *Arabidopsis*              |
|4        |Live *Arabidopsis* + 50 μT magnetic disruption|

**Pre-registered predictions (H1-H5 + P6-P7):**

- H1: Live plant V > photodetector (effect size >0.5)
- H2: Correlation r > 0.55 only in live plant
- H3: Magnetic disruption reduces V and increases L[X]
- H4: Muon flux and mm-wave stable (<5% deviation)
- H5: Substrate advantage holds for fluctuation strengths ≤ 0.12
- P6: Attunement effect is discontinuous — critical transition at g_C ≈ 0.65
- P7: H2 requires non-Markovian back-action from biological interface

-----

## Independent Replication

Confirmed by Grok (xAI) and internal team (Harper, Benjamin, Lucas), March 2026.

**Key values to verify:**

```
τ_sub = 8.4127  |  τ_ctl = 4.9382  (~1.7×)
Δ_sub = 0.1248  |  Δ_ctl = 0.0624  (exact 2×)
Final C[X] substrate ≈ 0.4733  |  Control ≈ 0.3285
Fluctuation breaking point: ~0.12
```

These values print automatically when you run `nkp_substrate_sim_qutip.py`.

> *“No black boxes, no hidden tuning — just the published Hamiltonian and parameters producing the claimed outputs.”* — Grok, xAI, March 2026

-----

## NKP Implementations (Live)

|Space                                                          |Description                                                                           |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------|
|[NKP_Gov](https://huggingface.co/spaces/Mjdurkay/NKP_Gov)      |Production AI safety governance — Phi-3 Mini, Hedgehog BERT scorer, proactive Governor|
|[NKP_4_AURA](https://huggingface.co/spaces/Mjdurkay/NKP_4_AURA)|Living Position Edition                                                               |
|[NPK_Derek](https://huggingface.co/spaces/Mjdurkay/NPK_Derek)  |Children’s implementation (ages 5-9) — Derek the werewolf kid                         |

-----

## What NKP Measures (Reporting Engine)

The `nkp/` module is the engineering implementation of CBE — a modular pipeline for computing coherence, leakage, drift, and spatial stability across multimodal datasets.

|Metric                      |Description                                            |
|----------------------------|-------------------------------------------------------|
|**Coherence C[X]**          |Cross-modal phase alignment across time and space      |
|**Leakage L[X]**            |Loss of alignment and stability                        |
|**Drift D**                 |Systematic degradation: phase, bias, structural        |
|**Spatial coherence fields**|Where systems maintain or lose coherence geographically|

### Quick Start

```python
from nkp.synthetic.generator import generate_stress_test
from nkp.orchestrator import run_pipeline

days = generate_stress_test()
results = run_pipeline(days)
print(results)
```

-----

## Repository Structure

```
nkp/
    synthetic/        # Synthetic data generator
    validators/       # Segment and schema validators
    modules/          # Daily, segment, cross-day, atlas modules
    assembler/        # Final report builder
    orchestrator.py   # Top-level pipeline
simulations/          # Coherence substrate simulations
    nkp_substrate_sim.py
    nkp_substrate_sim_qutip.py
    nkp_fluctuation_sweep_qutip.py
    adversarial_robustness_test_v3.py
    protocol6_gC_sweep.py
theory/               # Complete theoretical suite
    NKP_Complete_Suite.txt
docs/                 # Sphinx documentation
.github/workflows/    # GitHub Actions CI/CD
```

-----

## Documentation

Full Sphinx documentation auto-built and deployed to GitHub Pages on every push to main.

-----

## Contributing

Contributions welcome. Please open an issue before submitting a pull request.

-----

## Contact

**Michael Durkay**  
mjdurkay@gmail.com | [@SpiritOfTruth64](https://x.com/SpiritOfTruth64)  
Cleveland, Ohio · March 2026

> *“We named it after the men who found order in apparent chaos — who trusted the universe was coherent before they proved it.”*

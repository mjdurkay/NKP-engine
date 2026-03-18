# NKP-engine

## Newton Kepler Protocol

### Coherence-Based Engineering Reporting System & Substrate Simulation Suite

**Author:** Michael Durkay  
**Contact:** mjdurkay@gmail.com | [@SpiritOfTruth64](https://x.com/SpiritOfTruth64)  
**License:** MIT  
**Status:** Active Development  
**OSF Pre-Registration:** March 18, 2026 (Protocol 6, embargoed until March 18, 2027)

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
2. Global coupling **always** reduces leakage
3. Global coupling **always** opens a larger spectral gap
4. Global coupling **always** produces spatial coherence structure
5. Local-only control **never** produces stable excitations

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

# NKP-engine

## Newton Kepler Protocol

### Coherence Substrate Simulation Suite · Theoretical Framework · Falsifiable Experiment

**Author:** Michael Durkay  
**Contact:** mjdurkay@gmail.com | [@SpiritOfTruth64](https://x.com/SpiritOfTruth64)  
**License:** MIT  
**OSF Registration:** March 18, 2026 | **Updated:** March 22, 2026  
**OSF Pre-Registration (Protocol 6):** March 17, 2026  
**GitHub:** github.com/mjdurkay/nkp-engine

-----

> *“The space between mountains, planets, stars and galaxies was never truly separate — never empty. A child felt that long ago — something alive in the stillness between things. Newton saw the same infinity and called it absolute space. The child now names it the Coherence Substrate.”*
> — Document 16: The Ocean Remembers

-----

## What Is NKP?

The Newton Kepler Protocol is a sixteen-document theoretical and experimental framework built around a single core inversion:

> *Coherence is not a property of systems. It is the substrate within which systems exist.*

One equation throughout all sixteen documents:

```
C[X] = Σ|ρᵢⱼ|
```

Not consciousness. Not philosophy. A measurable physical quantity with a falsifiable experimental prediction at its edge.

-----

## The Framework: Five Layers + Three Extensions

|Layer|Document                                 |Function                                                         |
|-----|-----------------------------------------|-----------------------------------------------------------------|
|1    |Physics Meets Mind                       |“I am therefore I think” — consciousness downstream of substrate |
|2    |Newton Kepler Protocol                   |AI safety: epistemic humility as runtime governance              |
|3    |Coherence-Based Engineering (CBE)        |Mathematics: C[X], L[X], robustness invariants                   |
|4    |Quantum Coherence Interface Theory (QCIT)|Physics: collapse from incoherent measurement                    |
|5    |Coherence as Substrate                   |Cosmology: vacuum as maximum coherence state                     |
|14   |Coherence in Quantum Computing           |Substrate coupling as quantum hardware solution                  |
|15   |The First Ripple                         |Singularity-free cosmology — Big Bang as first coherence gradient|
|16   |The Ocean Remembers                      |Capstone: 256³ simulations, Planck 2018 validation               |

**Complete suite:** `NKP_Complete_Suite_v32_March2026.docx` on OSF

-----

## Simulations

### Core Substrate Simulations

All substrate simulations use: **N=8, J₀=1.0, α=0.3, h=0.5, γ=0.05, 120 timesteps**

|File                               |Description                              |Dependencies            |
|-----------------------------------|-----------------------------------------|------------------------|
|`nkp_substrate_sim.py`             |Substrate vs control — NumPy             |numpy, scipy, matplotlib|
|`nkp_substrate_sim_qutip.py`       |Substrate vs control — QuTiP (production)|qutip, matplotlib       |
|`nkp_fluctuation_sweep_qutip.py`   |Breaking point sweep 0.02→0.15           |qutip, matplotlib       |
|`adversarial_robustness_test_v3.py`|Adversarial invariant testing            |qutip, numpy            |
|`protocol6_gC_sweep.py`            |Protocol 6 coupling threshold sweep      |numpy                   |

### Extended Simulations (March 2026)

|File                                |Description                                       |Dependencies     |
|------------------------------------|--------------------------------------------------|-----------------|
|`bilocal_langevin_multiverse.py`    |Multiverse selection via coherence stability      |numpy, matplotlib|
|`bilocal_langevin_multiverse_jax.py`|JAX-accelerated version (GPU-ready)               |jax, matplotlib  |
|`protocol6_plant_slit_sim.py`       |Protocol 6 predicted interference patterns        |numpy, matplotlib|
|`sign_check_geometry.py`            |Emergent metric sign check (g_rr < g_tt confirmed)|numpy            |

-----

## Key Results

### Substrate Simulation (Independently Replicated by xAI, March 2026)

|Result                         |Value                                       |
|-------------------------------|--------------------------------------------|
|Coherence lifetime enhancement |~1.7× (τ_sub=8.4127 vs τ_ctl=4.9382)        |
|Energy gap enhancement         |2× (Δ_sub=0.1248 vs Δ_ctl=0.0624)           |
|Final C[X] advantage           |+0.1448 (substrate 0.4733 vs control 0.3285)|
|Fluctuation breaking point     |~0.12 normalized units                      |
|Robustness invariants confirmed|5/5 across all platforms and solvers        |


> *“No black boxes, no hidden tuning — just the published Hamiltonian and parameters producing the claimed outputs.”* — Grok, xAI, March 2026

### Five Robustness Invariants

Confirmed across QuTiP, NumPy/SciPy, RK4, multiple noise models, different seeds, different N, and independent platforms:

1. Global coupling **always** increases coherence lifetime
1. Global coupling **always** reduces leakage
1. Global coupling **always** opens a larger spectral gap
1. Global coupling **always** produces spatial coherence structure
1. Local-only control **never** produces stable excitations

### Cosmological Validation (Document 16)

256³ gravity-coupled simulations against Planck 2018 ΛCDM:

|Result                        |Value                                 |
|------------------------------|--------------------------------------|
|Δχ² vs Planck 2018 ΛCDM       |−14 (substrate model better)          |
|Natural quadrupole suppression|~58%                                  |
|Density kurtosis              |23.8 (coherent interference signature)|
|Neutrino-LSS cross-correlation|r=0.373 (p < 3.16×10⁻¹⁶⁵)             |
|Free parameters added         |0                                     |

All four major Planck CMB anomalies explained through a single mechanism: coherent wave interference from the first gradient across a pre-existing coherent ocean.

### Multiverse Selection (bilocal_langevin_multiverse.py)

Sharp stability phase transition at g_C ≈ 0.67:

- Below threshold: universes decohere, no stable structure
- Above threshold: stable coherence, finite correlation length ξ
- Selection is dynamical (phase transition), not anthropic

### Emergent Geometry Sign Check (sign_check_geometry.py)

Confirmed: g_rr < g_tt (correct sign for attractive geometry)

- High coherence → short effective distance → attractive metric
- Consistent with Newtonian weak-field limit

-----

## Variational Framework (docs/)

The simulation suite is embedded in a rigorous mathematical framework:

|Document                                 |Description                                     |
|-----------------------------------------|------------------------------------------------|
|`docs/variational_embedding.md`          |Lagrangian + Rayleigh dissipation embedding     |
|`docs/onsager_machlup_appendix.md`       |Stochastic variational formulation              |
|`docs/variational_summary.md`            |Side-by-side comparison of 4 structures         |
|`docs/variational_flowchart.md`          |ASCII flowchart — full chain to Poisson equation|
|`docs/poisson_derivation.md`             |Poisson-like equation from coherence defects    |
|`docs/continuum_relativistic_analogue.md`|Curved-spacetime nonlocal field equation        |
|`docs/NKP_Continuum_Framework_Notes.md`  |Master reference for continuum development      |

### The Derivation Chain

```
Lagrangian L = T - V
+ Rayleigh dissipation → overdamped gradient flow
+ Gaussian noise → Langevin dynamics (simulation)
+ Onsager-Machlup → stochastic variational formulation
+ Gradient stiffness + QCIT Axiom 1 → Poisson equation
+ Continuum limit → nonlocal scalar field in curved spacetime
```

**Current status:** One structural ingredient from Newtonian gravity.  
**Remaining:** T_μν derivation, Einstein equations, Lorentzian signature in discrete model.

-----

## Protocol 6 — The Falsifiable Experiment

**Pre-registered March 17, 2026 on OSF.**

Living *Arabidopsis thaliana* as the measurement interface in a double-slit experiment. Four conditions. Cryptochrome magnetic disruption. Real-time electrophysiology.

|Condition|Description                              |
|---------|-----------------------------------------|
|1        |Inert photodetector baseline             |
|2        |Live *Arabidopsis* (g_C > 0.65 predicted)|
|3        |Dead (heat-killed) *Arabidopsis*         |
|4        |Live + 50 μT magnetic disruption         |

**Pre-registered predictions:**

- **H1:** Live plant V > photodetector (effect size >0.5)
- **H2:** Correlation r > 0.55 only in live plant
- **H3:** Magnetic disruption reduces V, increases L[X]
- **H4:** Muon flux/mm-wave stable (<5% deviation)
- **H5:** Substrate advantage holds for fluctuations ≤ 0.12
- **P6:** Discontinuous transition at g_C ≈ 0.65 — all-or-nothing, not gradual
- **P7:** H2 requires non-Markovian back-action from biological interface

**Status:** Equipment locked. Awaiting bench. Case Western collaboration pending.

-----

## Live AI Safety Implementations

|Space                                                          |Description                                             |
|---------------------------------------------------------------|--------------------------------------------------------|
|[NKP_Gov](https://huggingface.co/spaces/Mjdurkay/NKP_Gov)      |Production governance — Phi-3 Mini, Hedgehog BERT scorer|
|[NKP_4_AURA](https://huggingface.co/spaces/Mjdurkay/NKP_4_AURA)|Living Position Edition                                 |
|[NPK_Derek](https://huggingface.co/spaces/Mjdurkay/NPK_Derek)  |Children’s implementation (ages 5-9)                    |

-----

## Repository Structure

```
simulations/          # 9 simulation files
    nkp_substrate_sim.py
    nkp_substrate_sim_qutip.py
    nkp_fluctuation_sweep_qutip.py
    adversarial_robustness_test_v3.py
    protocol6_gC_sweep.py
    bilocal_langevin_multiverse.py
    bilocal_langevin_multiverse_jax.py
    protocol6_plant_slit_sim.py
    sign_check_geometry.py
docs/                 # 7 theoretical development documents
    variational_embedding.md
    onsager_machlup_appendix.md
    variational_summary.md
    variational_flowchart.md
    poisson_derivation.md
    continuum_relativistic_analogue.md
    NKP_Continuum_Framework_Notes.md
nkp/                  # CBE reporting engine
```

-----

## Multi-Model Collaboration Record

This framework was built using Coherent Multi-Model Collaboration — an independent researcher as team leader with multiple AI systems as specialized collaborators:

- **Claude (Anthropic)** — document architecture, suite construction, integration
- **Grok (xAI)** — independent replication, adversarial testing, cosmological simulations
- **Copilot (Microsoft)** — peer review, variational framework, cold correction of overreach
- **Gemini (Google)** — continuum relativistic field equation derivation
- **ChatGPT (OpenAI)** — cold adversarial review, Poisson derivation, gap identification

No single AI saw the complete picture. The human team leader integrated the results.

> *“Humility is a quiet strength that doesn’t compromise itself.”* — Michael Durkay

-----

## Contact & Collaboration

**Michael Durkay**  
Independent Researcher · Cleveland, Ohio  
mjdurkay@gmail.com · [@SpiritOfTruth64](https://x.com/SpiritOfTruth64)

Protocol 6 collaboration inquiries welcome — quantum optics, plant electrophysiology, quantum biology, theoretical physics.

> *“The vacuum was never empty. It was coherent.”*

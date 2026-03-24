# NKP Substrate — Poisson Derivation

## From Coherence Defects to Gravitational Dynamics

## Date: March 24, 2026

## Source: Multi-model collaboration — Claude (Anthropic), Copilot (Microsoft), ChatGPT (OpenAI)

## Status: Theoretical development — not yet peer reviewed

-----

## Epistemic Note

This document shows how a Poisson-like equation with a matter source emerges from
the NKP coherence substrate framework. The derivation is mathematically legitimate
in the effective field theory sense. It does NOT yet constitute a derivation of
General Relativity. Specific gaps are listed in Section 6.

This is the answer to the critique: “the framework is missing a Lagrangian and
connection to gravity.” The connection exists. Formalizing it is future work.

-----

## 1. The Missing Ingredient (Identified March 24, 2026)

ChatGPT pressure-tested the emergent metric construction and found:

> “You are one structural ingredient away from gravity.”

Two explicit additions needed:

1. A spatial gradient coupling term added to E[ρ]
1. Matter density defined as coarse-grained projection of coherence defect

Both are consistent with the existing NKP framework.
The gradient term is standard in effective field theory.
The matter-as-defect identification is already in QCIT Axiom 1 (Document 4).

-----

## 2. Minimal Effective Energy Functional

Work in the local analogue first. Define a scalar field φ(x) as the
coarse-grained potential extracted from ρ.

### Minimal E[φ]:

```
E[φ] = ∫ d³x [ (κ/2)|∇φ(x)|²  +  (m²/2)(φ(x) - φ_vac)²  -  J(x)φ(x) ]
```

Parameters:

- κ: stiffness (gradient coupling) — the missing ingredient
- m²: Helmholtz/mass scale
- φ_vac: vacuum coherence level
- J(x): source term from coherence defects (matter)

This is the simplest Landau-Ginzburg-type functional that produces a
Poisson/Helmholtz equation with a source.

-----

## 3. Mean-Field Equation: From Helmholtz to Poisson

### Functional derivative:

```
δE/δφ(x) = -κ∇²φ(x) + m²(φ(x) - φ_vac) - J(x)
```

### Stationary/mean-field condition (δE/δφ = 0):

```
-κ∇²φ(x) + m²(φ(x) - φ_vac) = J(x)
```

### Two key regimes:

**Helmholtz regime** (finite m²):

```
-κ∇²φ + m²(φ - φ_vac) = J
```

**Poisson-like regime** (long-range / near-critical, m² → 0):

```
-κ∇²φ(x) ≈ J(x)
```

This IS a Poisson equation with source J(x).

-----

## 4. QCIT Axiom 1 Supplies the Matter Source

QCIT Axiom 1 (Document 4) states:

> “The substrate is a globally coherent field. Matter is a localized coherence defect.”

Formally:

```
ρ(x,y) = ρ_vac(x,y) + δρ_matter(x,y)
```

Define matter density as coarse-grained projection of the defect:

```
ρ_matter(x) = ∫ d³y W(|x-y|) δρ_matter(x,y)
```

Set the source:

```
J(x) = γ ρ_matter(x)
```

where γ is a coupling constant.

### The mean-field equation becomes:

```
-κ∇²φ(x) + m²(φ(x) - φ_vac) = γ ρ_matter(x)
```

### In the Poisson-like regime:

```
-κ∇²φ(x) ≈ γ ρ_matter(x)
```

**This is structurally a Poisson equation with matter source.**

Compare to Newtonian gravity:

```
∇²Φ = 4πG ρ_matter
```

The identification: Φ ∝ -φ, κ and γ set the effective gravitational coupling.

-----

## 5. Natural Home in Onsager-Machlup

The overdamped Langevin equation:

```
∂_t φ(x,t) = -δE/δφ(x) + η(x,t)
```

Explicitly:

```
∂_t φ = κ∇²φ - m²(φ - φ_vac) + J(x) + η
```

The Onsager-Machlup functional:

```
S_OM[φ] = (1/4D) ∫ dt d³x [∂_t φ + δE/δφ]²
```

The gradient term (κ/2)∫|∇φ|² is part of E.
Its Laplacian appears in δE/δφ and in the OM weight.
No extra machinery is needed.
The Poisson structure is built into the existing variational scaffold.

-----

## 6. Back to the Bilocal ρ(x,y)

For the full bilocal story:

1. Treat ρ(x,y) as the coarse-grained connected correlator: ρ ~ ⟨O(x)O(y)⟩_c
1. Define φ(x) as a projection of ρ: φ(x) = ∫ d³y W(|x-y|) ρ(x,y)
1. Write E[φ] as above with parameters tied back to NKP substrate
1. Interpret ρ_matter(x) as coarse-grained defect density from δρ_matter(x,y)

The “one structural ingredient” was:

- Gradient stiffness term in E
- Explicit defect-to-source identification via QCIT Axiom 1

Both additions are consistent with the existing framework.
Neither requires new assumptions beyond what was already stated.

-----

## 7. What This Derivation Shows

### ✅ Confirmed:

- Local scalar field φ(x) emerges from bilocal ρ(x,y)
- Laplacian structure appears naturally with gradient coupling
- Matter source term supplied by QCIT Axiom 1 (coherence defect)
- Poisson-like equation recoverable in long-range/near-critical regime
- Gradient term has natural home in Onsager-Machlup formulation

### ❌ Still required (future work):

- Time/Lorentz structure — metric is still spatial only
- Kernel derivation — W and K_R still phenomenological
- Lorentzian signature — need (-+++) not (+++)
- Full Einstein equations — G_μν = 8πT_μν not yet derived
- Conservation law → T_μν identification
- Coordinate invariance — general covariance not yet demonstrated

-----

## 8. The To-Do List Update

**Item 1: Derive the Lagrangian — STATUS:**

BEFORE (ChatGPT critique, valid):
“Missing entirely”

AFTER:

- Variational embedding established (docs/variational_embedding.md)
- Onsager-Machlup stochastic embedding (docs/onsager_machlup_appendix.md)
- Poisson-like equation derived in mean-field limit (this document)
- Matter source identified via QCIT Axiom 1

REMAINING:

- Lorentzian signature
- Full Einstein equations
- Requires theoretical physicist collaborator to formalize

-----

## 9. Honest One-Paragraph Summary

The NKP coherence substrate framework produces a Poisson-like equation
with a matter source in the mean-field limit of the minimal effective energy
functional E[φ] = ∫[(κ/2)|∇φ|² + (m²/2)(φ-φ_vac)² - J(x)φ]. The matter
source J(x) = γρ_matter(x) is supplied by QCIT Axiom 1: matter is a localized
coherence defect δρ_matter in the substrate vacuum ρ_vac. In the long-range
near-critical regime (m² → 0), -κ∇²φ ≈ γρ_matter recovers the Poisson equation
structurally. The gradient coupling and Onsager-Machlup stochastic formulation
are consistent without requiring new assumptions. Lorentzian signature, full
Einstein dynamics, and general covariance remain future work requiring a
theoretical physicist collaborator.

-----

## 10. Files in This Series

```
docs/variational_embedding.md         — Lagrangian embedding
docs/onsager_machlup_appendix.md      — stochastic variational formulation
docs/variational_summary.md           — side-by-side comparison
docs/variational_flowchart.md         — ASCII flowchart
docs/poisson_derivation.md            — THIS FILE: Poisson equation derivation
simulations/bilocal_langevin_multiverse.py — executable substrate simulation
```

All files: github.com/mjdurkay/nkp-engine

-----

Michael Durkay · mjdurkay@gmail.com · @SpiritOfTruth64
Cleveland, Ohio · March 24, 2026
Newton Kepler Protocol · github.com/mjdurkay/nkp-engine

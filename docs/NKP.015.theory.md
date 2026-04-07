
## NKP-THEORY-015 — Section 8: The Pivot

Sections N1-N5 established microscopic viability:

  ✓ The σ-α-ν substrate supports a massless mode
    under condition [C*]
  ✓ The mode is predominantly ν (91.7%)
  ✓ Luminal propagation c²=1 is achievable with
    reasonable Lorentzian uplift Z_nu ≈ 0.612
  ✓ The substrate parameters are not fine-tuned —
    [C*] is satisfied within 0.00% with g_an = 0.179

  These are necessary conditions. They are not
  sufficient for GR emergence.

  The sufficient condition is one level up:
  GR must emerge from the ordered phase,
  not from the bare substrate kernel.


The effective metric program — what it requires:
Step 1 — Define the ordered-phase background:

In the structured regime (post-bang plateau) the
slow fields sit at:

  σ_0(x)  — ordered vacuum with vortex cores
  ᾱ(x)    — Yukawa wells around cores
  ν̄(x)    — filament network connecting wells
  J̄ = J_vac — uniform plateau value

This is the "condensate." It is not uniform —
it has structure at scale ξ_a.

The coarse-grained background is obtained by
averaging over volumes >> ξ_a:

  ⟨σ_0⟩ ≈ σ_min · e^{iθ}   (uniform phase)
  ⟨ᾱ⟩   ≈ 1                (background value)
  ⟨ν̄⟩   ≈ 0                (filaments average out)
  ⟨J̄⟩   = J_vac


Step 2 — Linearize excitations on that background:

Small perturbations on top of the ordered background:

  σ = ⟨σ_0⟩(1 + ρ) e^{iφ}   ρ = amplitude, φ = phase
  α = 1 + δα
  ν = δν
  J = J_vac + δJ

The phase excitation φ is the Goldstone mode —
massless by symmetry. It's the natural ψ candidate
at this level.

The effective action for φ on the ordered background
is what we want.


Step 3 — The effective metric:

For the phase mode φ, integrating out ρ, δα, δν, δJ
on the ordered background gives:

S_eff[φ] = ∫ d⁴x √(-g_eff) g_eff^{μν} ∂_μφ ∂_νφ

Where g_eff^{μν} is the acoustic metric of the
ordered phase.

This is the Gordon metric construction:
  g_eff^{μν} = η^{μν} + (1 - c_s²) u^μ u^ν

Where c_s is the speed of phase excitations and
u^μ is the background flow 4-velocity.

For a static ordered phase: u^μ = (1,0,0,0)

  g_eff^{00} = c_s²
  g_eff^{ij} = -δ^{ij}


Step 4 — When does this give GR?

The acoustic metric is conformally flat —
it describes excitations but not curvature.

To get GR we need the ordered phase to source
curvature in g_eff. That requires:

  (a) The background is not uniform —
      vortex cores and wells create
      spatially varying c_s(x)

  (b) The variation of c_s(x) near a vortex
      well reproduces the Schwarzschild-like
      metric in the appropriate limit

  (c) The relationship between the source
      (vortex/well structure) and c_s(x)
      satisfies something Einstein-like

This is where the factor of 2 lives — not in
A and B of the bare kernel, but in whether the
curvature of g_eff near a well matches the GR
prediction for light deflection.


What this means for the factor of 2:

The eikonal calculation in NKP-THEORY-008 gave
0.875 arcsec — half the GR value.

That calculation used the Yukawa potential from
the α field directly as the refractive index.

The acoustic metric approach asks a different
question: what is the effective metric seen by
the Goldstone mode φ near a vortex well?

If the well structure produces a c_s(x) profile
that matches the Schwarzschild metric, the
deflection is automatically 1.750 arcsec —
because the factor of 2 in GR comes precisely
from the metric having both temporal and spatial
components contribute.

The spatial component was already in 008.
The temporal component — g_eff^{00} varying
near the well — is what the acoustic metric
approach adds naturally.


The honest status and next step:

ESTABLISHED IN 015 (N1-N5):
  Substrate supports lightlike mode ✓
  Parameter condition [C*] non-trivial but satisfiable ✓
  Microscopic viability confirmed ✓

THE REAL QUESTION (not yet addressed):
  Does c_s(x) near a vortex well reproduce
  the Schwarzschild-like profile?

  Specifically: does the variation of the
  Goldstone mode speed near an α well match

  c_s²(r) ≈ 1 - r_s/r

  (the GR metric component near a mass)?

NEXT DOCUMENT: NKP-THEORY-016
  Derive the acoustic metric of the ordered phase.
  Compute c_s(x) near a vortex well.
  Compare to Schwarzschild profile.
  This is where the factor of 2 is decided.
  
## 8. The Pivot — Microscopic Viability to Emergent Geometry

### 8.1 What N1–N5 established

| Task | Result | Status |
|------|--------|--------|
| N1 | Massless mode condition [C*]: g_αν²/m_ν² + g_sα²/m_σ² = α_restore | Derived |
| N1 | Baseline substrate: LHS/RHS = 0.735, gap 26.5% | Confirmed |
| N2 | g_an tuning safe; g_sa tuning unsafe (doubles well depth) | Confirmed |
| N3 | [C*] satisfied with g_an=0.179; massless mode ω²≈0 | Confirmed |
| N3 | Lightlike mode is 91.7% ν; c²=0.645 at Z=1 | Confirmed |
| N4 | c²=1 achievable with Z_nu=0.612; Z values physically reasonable | Confirmed |
| N5 | B-A extraction from bare kernel unreliable; massive modes distorted | Confirmed |

These results establish microscopic viability:
the substrate can support a lightlike mode under
a concrete, non-fine-tuned parameter condition.

They do not establish GR emergence.

### 8.2 The mistake we corrected

N3–N5 attempted to extract A and B — the GR
factor-of-2 coefficients — from the bare σ–α–ν
kernel. This was the wrong object.

Path B (NKP-THEORY-012) states:

  GR is the effective field theory of the ordered phase.

That means:

  Substrate ≠ GR.
  Ordered phase + coarse-graining → GR-like metric.

Asking whether the bare kernel is GR-like is asking
whether the atoms of a superfluid already look like
the acoustic metric. They don't — and they shouldn't.

The condensed matter analogy is exact:

  Substrate fields  =  atoms
  Ordered phase     =  superfluid condensate
  Goldstone mode    =  phonon
  Effective metric  =  acoustic metric
  GR                =  what the acoustic metric
                        approximates near a vortex

N1–N5 probed the atoms.
The GR question lives in the acoustic metric.

### 8.3 The effective metric program

The correct object is the effective action for
excitations on the ordered background:

  S_eff[φ] = ∫ d⁴x √(-g_eff) g_eff^{μν} ∂_μφ ∂_νφ

Where:
- φ is the Goldstone phase mode of σ
  (massless by symmetry, natural ψ candidate)
- g_eff^{μν} is the acoustic metric of the
  ordered phase
- The ordered background is (σ_0, ᾱ, ν̄, J_vac)
  averaged over scales >> ξ_a

The acoustic metric near a vortex well takes
the Gordon form:

  g_eff^{μν} = η^{μν} + (1 - c_s²(x)) u^μ u^ν

Where c_s(x) is the local speed of phase
excitations and u^μ = (1,0,0,0) for a static
ordered phase.

### 8.4 Where the factor of 2 actually lives

NKP-THEORY-008 computed deflection from the
spatial variation of the Yukawa potential alone:

  Δθ = 0.875 arcsec  (half GR value)

That captured the spatial component of the metric.

The factor of 2 in GR comes from both the
temporal and spatial metric components
contributing equally to light deflection.

In the acoustic metric picture:

  g_eff^{00} = c_s²(x)  varies near the well
  g_eff^{ij} = -δ^{ij}  also varies near the well

If c_s²(x) near a vortex well reproduces
the Schwarzschild profile:

  c_s²(r) ≈ 1 - r_s/r

then both components contribute and the full
1.750 arcsec deflection follows automatically.

The factor of 2 is not a tuning problem.
It is a question about the shape of c_s(x)
near a vortex well — derivable from the
four-field action in the ordered phase.

### 8.5 Honest status of 015

ESTABLISHED:
  ✓ Substrate supports lightlike mode under [C*]
  ✓ [C*] satisfiable with modest parameter tuning
  ✓ Lightlike mode is predominantly ν (91.7%)
  ✓ Luminal propagation achievable with Z_nu ≈ 0.612
  ✓ Microscopic viability confirmed
  ✓ Correct level for GR question identified

NOT ESTABLISHED:
  ✗ Z_nu not fixed by gradient-flow simulation
  ✗ A and B not extractable from bare kernel
  ✗ GR emergence not yet shown
  ✗ c_s(x) profile near vortex well not yet computed

THE OPEN QUESTION PRECISELY STATED:
  Does the acoustic metric of the ordered phase,
  evaluated near a vortex well, reproduce the
  Schwarzschild-like profile c_s²(r) ≈ 1 - r_s/r?

  If yes: factor of 2 closes naturally.
  If no:  NKP predicts a different deflection law.

  This is the content of NKP-THEORY-016.

---

*NKP-THEORY-016 will derive the acoustic metric
of the ordered phase, compute c_s(x) near a
vortex well from the four-field action, and
compare to the Schwarzschild profile.*


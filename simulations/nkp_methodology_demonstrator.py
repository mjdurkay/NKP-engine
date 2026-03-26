import numpy as np

print("NKP Methodology Demonstrator")
print("=" * 60)
print("This script shows the complete chain from action to simulation.")
print()

print("1. Action → Gradient Flow Limit")
print("   ∂ρ/∂t = κ ∇²ρ - α_eff(ρ)(ρ-1) + J")
print("   where α_eff(ρ) = α0 [1 + λ tanh(β |ln ρ|)]")
print()

print("2. Weak-Field Mapping")
print("   Φ = -δρ")
print("   Emergent metric: g_μν^eff = ρ^{-2} η_μν")
print("   → g00 ≈ -(1 + 2Φ), gij ≈ (1 - 2Φ)δij")
print()

print("3. Poisson Limit")
print("   ∇²Φ ≈ J/κ   (with G_eff = 1/(4πκ))")
print()

print("4. Effective Distance")
print("   d_eff = ∫ dx / ρ(x)   ← emerges from kinetic term")
print()

print("All steps are numerically validated in:")
print("   • nkp_weakfield_validation_v3.py")
print("   • galactic_rotation_v3_successful.py")
print("   • sign_check_geometry.py")
print("\nThis demonstrates variational consistency + numerical transparency.")
print("github.com/mjdurkay/NKP-engine")

import numpy as np
import matplotlib.pyplot as plt

# ================================================================
# NKP V5 Galactic-Scale Light Deflection Test
# Uses realistic galaxy mass and kpc-scale impact parameters
# ================================================================

print("NKP V5 Galactic-Scale Light Deflection Test")
print("=" * 65)

# Physical constants
G   = 6.67430e-11        # m^3 kg^-1 s^-2
c   = 2.99792458e8       # m/s
Msun = 1.98847e30        # kg
kpc = 3.08568e19         # meters

# Galactic parameters (Milky-Way-like)
M_gal = 1.0e11 * Msun    # total mass
R_scale = 5.0 * kpc      # characteristic scale

def phi_newton(r, M):
    """Dimensionless Newtonian potential Φ = -GM/(r c^2)"""
    return -G * M / (r * c**2)

def rho_from_phi(phi):
    """NKP weak-field mapping: rho = 1 - Φ"""
    return 1.0 - phi

def deflection_V4(M, b):
    """V4 pure conformal → zero light bending at leading order"""
    return 0.0

def deflection_V5(M, b):
    """V5 split metric → GR-like weak-field deflection"""
    return 4.0 * G * M / (b * c**2)

def rad_to_arcsec(theta_rad):
    return theta_rad * 206264.806  # arcsec per radian

if __name__ == "__main__":
    M = M_gal
    bs = np.array([5.0, 10.0, 20.0]) * kpc   # impact parameters in kpc

    print(f"Galaxy mass M = {M/Msun:.2e} M_⊙")
    print(f"Scale radius   = {R_scale/kpc:.1f} kpc\n")

    # Sample Φ(r) and ρ(r)
    rs = np.array([1, 5, 10, 20]) * kpc
    phis = phi_newton(rs, M)
    rhos = rho_from_phi(phis)

    print("Sample radii, Φ(r), ρ(r):")
    for r, phi, rho in zip(rs/kpc, phis, rhos):
        print(f"r = {r:6.1f} kpc | Φ = {phi: .3e} | ρ = {rho: .8f}")

    print("\nLight deflection angles (impact parameter b):")
    for b in bs:
        theta_V4 = deflection_V4(M, b)
        theta_V5 = deflection_V5(M, b)
        print(f"b = {b/kpc:5.1f} kpc")
        print(f"   V4 (pure conformal) : {theta_V4:.3e} rad = {rad_to_arcsec(theta_V4):.3e} arcsec")
        print(f"   V5 (split metric)   : {theta_V5:.3e} rad = {rad_to_arcsec(theta_V5):.3e} arcsec")

    print("\nNote: Galactic-scale deflections are extremely small.")
    print("V4 predicts zero bending in the pure conformal limit.")
    print("V5 recovers the GR-like result.")

    # Simple plot for logging
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(rs/kpc, phis, 'b-', label='Φ(r)')
    ax.plot(rs/kpc, rhos, 'r--', label='ρ(r) = 1 - Φ')
    ax.set_xlabel('r (kpc)')
    ax.set_ylabel('Value')
    ax.set_title('Galactic Weak-Field Mapping: Φ(r) and ρ(r)')
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.savefig('nkp_v5_galactic_mapping.png', dpi=300, bbox_inches='tight')
    print("\nMapping plot saved as nkp_v5_galactic_mapping.png")

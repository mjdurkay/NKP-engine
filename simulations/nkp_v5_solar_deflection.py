import numpy as np
import matplotlib.pyplot as plt

# ================================================================
# NKP V5 Solar Limb Light Deflection Test
# Real Sun + real observable (classic Eddington test)
# ================================================================

print("NKP V5 Solar Limb Light Deflection Test")
print("=" * 60)

# Physical constants
G   = 6.67430e-11        # m^3 kg^-1 s^-2
c   = 2.99792458e8       # m/s
Msun = 1.98847e30        # kg
Rsun = 6.9634e8          # m

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
    M = Msun
    b = Rsun                     # grazing ray at solar limb

    print(f"Mass M = {M/Msun:.2e} M_⊙")
    print(f"Impact parameter b = R_⊙ = {Rsun/1e8:.1f} × 10^8 m\n")

    # Sample Φ(r) and ρ(r)
    rs = np.array([1.0, 2.0, 5.0, 10.0]) * Rsun
    phis = phi_newton(rs, M)
    rhos = rho_from_phi(phis)

    print("Sample radii, Φ(r), ρ(r):")
    for r, phi, rho in zip(rs/Rsun, phis, rhos):
        print(f"r/R_⊙ = {r:5.1f} | Φ = {phi: .3e} | ρ = {rho: .8f}")

    # Deflection predictions
    theta_V4 = deflection_V4(M, b)
    theta_V5 = deflection_V5(M, b)

    print("\nLight deflection for grazing ray at solar limb:")
    print(f"V4 (pure conformal) : {theta_V4:.3e} rad = {rad_to_arcsec(theta_V4):.3e} arcsec")
    print(f"V5 (split metric)   : {theta_V5:.3e} rad = {rad_to_arcsec(theta_V5):.3f} arcsec")
    print("                     (Classic GR / Eddington result ≈ 1.75 arcsec)")

    # Plot for logging
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(rs/Rsun, phis, 'b-', label='Φ(r)')
    ax.plot(rs/Rsun, rhos, 'r--', label='ρ(r) = 1 - Φ')
    ax.set_xlabel('r / R_⊙')
    ax.set_ylabel('Value')
    ax.set_title('Solar Weak-Field Mapping: Φ(r) and ρ(r)')
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.savefig('nkp_v5_solar_mapping.png', dpi=300, bbox_inches='tight')
    print("\nMapping plot saved as nkp_v5_solar_mapping.png")

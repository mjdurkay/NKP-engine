import numpy as np
import matplotlib.pyplot as plt

# ================================================================
# NKP V5 Ray Comparison Plot
# Visualizes V4 (straight) vs V5 (bent) null geodesics
# ================================================================

print("Generating V4 vs V5 ray comparison plot...")

# Load trajectories from previous run
# (Run nkp_v5_light_deflection.py first to generate this file)
data = np.load("nkp_v4_v5_geodesics.npz", allow_pickle=True)

impact_params = data["b"]
r_V4 = data["r_V4"]
phi_V4 = data["phi_V4"]
r_V5 = data["r_V5"]
phi_V5 = data["phi_V5"]

def to_xy(r, phi):
    """Convert polar (r, phi) to Cartesian (x, y)"""
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return x, y

plt.figure(figsize=(9, 9))

for i, b in enumerate(impact_params):
    # V4: straight rays
    x4, y4 = to_xy(r_V4[i], phi_V4[i])
    plt.plot(x4, y4, '--', color='blue', alpha=0.7, label=f'V4 (b={b:.1f})' if i == 0 else "")

    # V5: bent rays
    x5, y5 = to_xy(r_V5[i], phi_V5[i])
    plt.plot(x5, y5, '-', color='red', linewidth=2, label=f'V5 (b={b:.1f})' if i == 0 else "")

# Defect center marker
plt.scatter([0], [0], color='black', s=100, marker='o', label='Defect center')

plt.title('NKP Null Geodesics: V4 (straight) vs V5 (bent)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig('nkp_v4_v5_ray_comparison.png', dpi=300, bbox_inches='tight')
print("Plot saved as nkp_v4_v5_ray_comparison.png")
plt.show()

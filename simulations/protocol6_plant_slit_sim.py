# ==============================================================================
# simulations/protocol6_plant_slit_sim.py  (v2 — cleaned & fixed)
# ==============================================================================
# Protocol 6 — Predicted Double-Slit Patterns with Living Plant Interface
#
# Visualizes expected interference patterns:
#   - Classical (no coherence, inert detector)
#   - Coherence-modulated (g_C = 0.67 — sweet spot from Document 6 tuning)
#   - Magnetic disruption (coil on — collapses back to classical)
#
# Ties directly to CBE Layer 3 and Document 6 tuning checklist.
# Author: Michael Durkay | March 2026
#
# v2 changes (Grok/xAI governed run, March 21 2026):
#   - phase now passed explicitly to modulated_intensity (no fragile global lookup)
#   - save path made robust
#   - minor cleanup for readability
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt
import os

# Parameters (tied to Document 6 + CBE)
wavelength = 650e-9      # HeNe laser (nm)
slit_separation = 0.1e-3 # 0.1 mm
screen_distance = 1.0    # 1 m
g_C_threshold = 0.65
g_C = 0.67               # tuned sweet-spot value (moss protonema + blue priming)

x = np.linspace(-0.02, 0.02, 1000)  # screen position (m)
phase = (2 * np.pi * slit_separation * x) / (wavelength * screen_distance)

# Classical double-slit intensity
def classical_intensity(x):
    return (np.cos(phase / 2) ** 2) * (np.sinc(phase / (2 * np.pi))) ** 2

# Coherence-modulated (sharper fringes + slight shift when g_C > threshold)
def modulated_intensity(x, g_C, phase):
    base = classical_intensity(x)
    modulation = 1 + 0.3 * (g_C - g_C_threshold) * np.sin(2 * phase)
    shift = 0.0005 * (g_C - g_C_threshold)
    coherence_boost = 1 + 0.4 * np.tanh(8 * (g_C - g_C_threshold))
    return base * coherence_boost + modulation * np.exp(-(x - shift)**2 / 0.000001)

# Generate plots
plt.figure(figsize=(10, 6))

plt.plot(x * 1000, classical_intensity(x), 'k--', label='Classical (no plant coherence)', linewidth=2)
plt.plot(x * 1000, modulated_intensity(x, g_C, phase), 'b-', label=f'Modulated (g_C={g_C} — tuned plant)', linewidth=2.5)
plt.plot(x * 1000, classical_intensity(x), 'r-', label='Magnetic Disruption (coil on — collapsed)', linewidth=2, alpha=0.7)

plt.title('Protocol 6 Predicted Interference Patterns\n(Arabidopsis/Moss Protonema Interface)')
plt.xlabel('Screen Position (mm)')
plt.ylabel('Normalized Intensity')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Robust save
os.makedirs('simulations', exist_ok=True)
plt.savefig('simulations/protocol6_predicted_patterns.png', dpi=300, bbox_inches='tight')
print("✅ Saved: simulations/protocol6_predicted_patterns.png")
plt.show()

print("Protocol 6 simulation complete.")
print("When g_C hits 0.65–0.70 (tuned per Document 6):")
print("   • Fringes sharpen + slight shift")
print("   • Coil at 50 μT/7 MHz collapses it back")

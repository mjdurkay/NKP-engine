# run_pipeline.py
"""
Master orchestrator for the 3D coherence substrate simulation.

Runs:
    1. Field initialization
    2. Phase 1 ordering
    3. Phase 2 active dynamics
    4. Convergence checks
    5. Final analysis
"""

import numpy as np

from fields import initialize_fields
from phase1_order import run_phase1
from phase2_active import run_phase2
from convergence import check_convergence
from analysis import analyze_results
from annihilation import compute_phase_gradient, log_annihilation  # optional utilities


def main():
    print("\n=== NKP ENGINE: 3D SUBSTRATE SIMULATION ===\n")

    # ---------------------------------------------------------
    # 1. INITIALIZE FIELDS
    # ---------------------------------------------------------
    print("Initializing fields...")
    alpha, sigma, nu, J, lap3, count_vortices_3d, params = initialize_fields()

    # ---------------------------------------------------------
    # 2. PHASE 1: ORDERING
    # ---------------------------------------------------------
    print("\n--- Running Phase 1 (ordering) ---")
    A, alpha, sigma, vort_history_p1, stop_step_p1 = run_phase1(
        alpha, sigma, lap3, count_vortices_3d, params
    )

    # ---------------------------------------------------------
    # 3. PHASE 2: ACTIVE DYNAMICS
    # ---------------------------------------------------------
    print("\n--- Running Phase 2 (active dynamics) ---")
    alpha_prev = alpha.copy()
    sigma_prev = sigma.copy()
    nu_prev = nu.copy()
    J_prev = J.copy()

    vort_history_p2 = []

    for step in range(20000):

        alpha, sigma, nu, J, vort_hist = run_phase2(
            alpha, sigma, nu, J, lap3, count_vortices_3d, params,
            max_steps=1,  # run one step at a time
            log_interval=999999  # suppress spam
        )

        vort_history_p2.extend(vort_hist)

        # Convergence check every 200 steps
        if step % 200 == 0 and step > 0:
            converged, metrics = check_convergence(
                alpha, sigma, nu, J,
                alpha_prev, sigma_prev, nu_prev, J_prev,
                vort_history_p2
            )

            print(
                f"[Convergence check @ step {step}] "
                f"d_sigma={metrics['d_sigma']:.6f}, "
                f"vort_var={metrics['vort_var']:.4f}, "
                f"converged={metrics['converged']}"
            )

            alpha_prev = alpha.copy()
            sigma_prev = sigma.copy()
            nu_prev = nu.copy()
            J_prev = J.copy()

            if converged:
                print("\nPhase 2 converged.")
                break

    # ---------------------------------------------------------
    # 4. ANALYSIS
    # ---------------------------------------------------------
    print("\n--- Running Analysis ---")
    results = analyze_results(
        A, alpha, sigma, nu, J,
        vort_history_p1 + vort_history_p2
    )

    print("\n=== Simulation Complete ===")
    print("Topological memory mean:", results["A_stats"]["A_mean"])
    print("Final vortex count:", results["vortex_summary"]["vort_final"])


if __name__ == "__main__":
    main()

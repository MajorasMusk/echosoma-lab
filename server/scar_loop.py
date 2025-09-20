import numpy as np

def run_scar_loop(seed: str):
    np.random.seed(len(seed))
    Phi = np.random.randn(32, 32)
    G = np.ones((32, 32))
    grad_x, grad_y = np.gradient(Phi)
    grad_sq = grad_x**2 + grad_y**2
    κ = np.corrcoef(G.flatten(), grad_sq.flatten())[0, 1]
    return {
        "seed": seed,
        "κ": float(κ),
        "MSI": abs(float(κ)),
        "ΔΦ": "guided_exploration"
    }

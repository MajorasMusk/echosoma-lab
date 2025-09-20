import numpy as np

def run_sigil(text: str, env: dict):
    seed_val = sum(ord(c) for c in text) % 1000 / 1000.0
    mean_state = np.tanh(seed_val * 10)
    std_state = abs(np.sin(seed_val * np.pi))
    scar_val = mean_state * (1 + 0.1 * std_state)
    return {
        "input_text": text,
        "seed_val": seed_val,
        "mean_state": mean_state,
        "std_state": std_state,
        "scar_val": scar_val,
        "env": env
    }

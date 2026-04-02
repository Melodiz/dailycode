# HW7: Superposition Geometry + SAE Recovery

Toy model learns to compress F features into d dimensions (superposition).
Then a vanilla SAE tries to recover the original features from hidden states.
Main finding: EV (reconstruction quality) is almost always >0.97 but feature
recovery can be terrible — you need directional metrics like weighted MMCS.

Report: `LLMR_HW7/report.pdf`

## How to run

```bash
# full sweep (takes a while on CPU)
python run_experiments.py

# or a single config
python -c "
from configs import ToyModelConfig, SAEConfig
from run_experiments import run_single
import torch
cfg = ToyModelConfig(F=50, d=5, train_steps=2000)
sae = SAEConfig(F_sae=100, train_steps=4000)
r = run_single(cfg, sae, 'results/test', torch.device('cpu'))
print(r)
"
```

## Files

```
hw7/
├── configs.py           # ToyModelConfig, SAEConfig dataclasses
├── toy_model.py         # ReLU autoencoder (W W^T f + b), data generation
├── sae.py               # sparse autoencoder + training loop
├── metrics.py           # EV, MMCS, weighted MMCS, feature dimensionality, etc
├── visualize.py         # all the plotting functions
├── run_experiments.py   # parameter sweeps, saves CSVs + plots to results/
├── checkpoint_1.py      # sanity check: toy model
├── checkpoint_2.py      # sanity check: SAE
├── checkpoint_3.py      # sanity check: metrics
├── results/             # experiment outputs (CSVs + per-run plots)
│   ├── 1a_alpha/        # alpha sweep [0.5, 1.0, 1.5, 2.0]
│   ├── 1b_F/            # F sweep [10, 20, 50, 100] at d=5
│   ├── 1c_d/            # d sweep [2, 5, 10] at F=50
│   ├── 1d_polytope_F/   # d=2 polytope vis, F=[4,5,6,8,10]
│   ├── 2a_l0_coeff/     # L1 coeff sweep
│   ├── 2b_F_sae/        # dictionary size sweep
│   └── 2e_d10_l0/       # d=10 operating point fix
└── LLMR_HW7/            # report (tex + figures + pdf)
```

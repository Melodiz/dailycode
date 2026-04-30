# HW11: Layer-wise Analysis of VLM Features via Logit Lens

Logit lens analysis of Qwen2-VL-2B-Instruct across five visual feature
categories (color, shape, counting, spatial, binding).

## Reproduction

Full sweep — Colab T4, ~7 min:

```bash
pip install "transformers>=4.52" torch accelerate pillow qwen-vl-utils tqdm pandas
python code/stage3_colab.py
```

Analysis + plots from the cached CSV:

```bash
python code/stage4_analysis.py
```

`stage4_analysis.py` finds `results/logit_lens_results.csv` automatically
when run from the repo root and writes its outputs to the cwd.

## Results

- **Report**: [report/main.pdf](report/main.pdf)
- **Raw data**: `results/logit_lens_results.csv` (36,250 rows)
- **Figures**: `figures/`

## Key findings

| Finding | Evidence |
|---|---|
| Sharp phase transition at L22→L23 | P(color) jumps 0.001 → 0.413 in one layer |
| Binding is compositional | Pair accuracy 0% → 100% at L24, distractor ≈ 0 |
| Counting collapses at n≥4 | 100% of n=4 errors produce "three" |
| "Below" actively suppressed | P(below) rises then decays; all errors → "right" |

## Model

Qwen2-VL-2B-Instruct, 28 layers, fp16, T4 GPU.

# HW13 FrozenLake VLM World Models

Testing whether a VLM world model can support planning in deterministic FrozenLake.

## Files

- [Report](assets/HW13_Report.pdf)
- [HW assignment](assets/HW13_assigment.pdf)
- Raw results: [Google Drive](https://drive.google.com/drive/folders/1ef6OJBjtRyewjiDig_E-9gVwmH-wa6xK?usp=sharing), [Yandex Disk](https://disk.yandex.ru/d/17WQYir_oSzCSA)

Raw results contain the dataset/images, SFT adapters, eval predictions/metrics, planning traces, final tables/plot, and small diagnostics.

## Setup

```bash
pip install -r requirements_colab.txt
```

Lightweight checks run on CPU. Qwen inference and SFT runs are intended for a GPU runtime.

## Main Commands

```bash
python run_a1_smoke.py
python run_a2_reactive_vlm.py --backend fake
python collect_data.py
python train_sft.py --condition image_text
python train_sft.py --condition image_only
python eval_world_model.py --condition image_text
python eval_world_model.py --condition image_only
python run_planning.py
python plot_results.py
```

```bash
python run_a2_reactive_vlm.py --parser-smoke
python eval_world_model.py --mode parser-smoke
python run_planning.py --mode parser-smoke
python -m py_compile *.py
```

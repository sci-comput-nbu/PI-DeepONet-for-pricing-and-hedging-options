# PI-DeepONet for for pricing and hedging options

Numerical data, research programs and trained models for time-fractional Black--Scholes pricing and parameter calibration, with matched PI-DeepONet, L1-FDM and fPINN comparisons. This public repository distributes data and code only.

## Download and verify

Download `TFBS_data_code_only_v1.0.1_20261009.zip` and its `.sha256` companion from [release v1.0.1](https://github.com/sci-comput-nbu/PI-DeepONet-for-for-pricing-and-hedging-options/releases/tag/v1.0.1). Verify the ZIP digest and extract it. `MANIFEST.sha256` inside the ZIP identifies every supplied file. Run `python verify_archive.py <extracted-directory>` to check the manifest.

## Contents

- `experiments/forward_comparison.py`: matched offline training and forward evaluation, with 83,841 parameters per network.
- `experiments/unified_operator.py`: shared L1-FDM and boundary utilities; its standalone historical cohort is separate from the current comparison.
- `experiments/forward_comparison_results/labels.npz`: 320 training and 48 validation parameter/state pairs on 120-space/120-time grids.
- `PI-DeepONet.pt`, `fPINN.pt`, configuration, histories, forward arrays, refined numerical references, metrics and timing samples in the same results folder.
- `market_reconstructed_quotes.csv`: 16 archived market observations. `market_transcription_audit.json` retains the vector coordinates, affine transforms and original source hash. The original PDF is not distributed.
- `experiments/inverse_comparison.py`: common bounded three-start, 35-step projected damped Gauss--Newton calibration.
- `experiments/inverse_comparison_results/`: 252 contract-level observation rows, full-precision noise/observation arrays, 126 primary method-level calibrations, six refined FDM checks, optimizer histories, conditioning and fidelity diagnostics, and numerical audits.
- Plotting and audit programs regenerate diagnostic graphics from the supplied numerical arrays; no pre-rendered manuscript figures are distributed.

## Reproduction

The saved environment used Python 3.12, NumPy 2.3.5, PyTorch 2.14.1+cpu, four PyTorch CPU threads, float64 FDM/evaluation and float32 training. Dependency versions are in `experiments/requirements.txt`.

Inspect the saved CSV/JSON/NPZ files without retraining. Back up results before running programs that overwrite outputs. From the extracted root:

```text
python experiments/extract_market_vector.py
python experiments/forward_comparison.py --evaluate-only
python experiments/evaluate_market_quotes.py
python experiments/audit_forward_comparison.py
python experiments/time_market_application.py
python experiments/inverse_comparison.py
python experiments/audit_inverse_comparison.py
```

For fresh matched training, run `python experiments/forward_comparison.py` without `--evaluate-only`. Offline checkpoints are selected using forward validation only. The public market reconstruction checks saved coordinates against archived quotes without requiring a PDF. The public inverse audit verifies numerical observations, checkpoints, objectives and aggregates without a LaTeX source dependency. Numerical solver, training and optimization implementations are unchanged.

## Data provenance and scope

Synthetic observations are refined 480-by-480 FDM states, not exact continuum solutions. Both inverse designs reuse frozen forward models and paired observations. Six true parameter pairs and three noise repetitions per noisy design support local comparisons, not global identifiability. FDM has smaller displayed mean parameter errors; PI-DeepONet provides inexpensive reuse and better noisy short-design recovery than the matched fPINN. Throughput does not establish equal-accuracy cost or single-query latency.

The 16 CSI 300 ETF observations were transcribed from an archived supplied vector figure. The original exchange/vendor export, return series and bid--ask records were not supplied. Saved coordinates verify geometric reconstruction only. Historical volatility is inherited; raw neural outputs are retained without positivity clipping. No hedging backtest or validated trading strategy is included.

Copyright and third-party rights remain with their holders. No additional software or data licence is granted by this deposit.

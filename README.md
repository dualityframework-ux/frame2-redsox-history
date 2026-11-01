> **Legacy snapshot — use [frame2_mvp](https://github.com/dualityframework-ux/frame2_mvp) for maintained development.**
> Dataset, methodology and deployment documentation now lives in the
> [history guide](https://github.com/dualityframework-ux/frame2_mvp/blob/main/docs/HISTORY_GUIDE.md).
> The original documentation below is retained for reference and may describe
> unimplemented features or outdated rules. Publish the canonical fixes first.

# frame² — Red Sox Franchise History

[![CI](https://github.com/dualityframework-ux/frame2-redsox-history/actions/workflows/ci.yml/badge.svg)](https://github.com/dualityframework-ux/frame2-redsox-history/actions/workflows/ci.yml)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)
[![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

frame² explains the mechanism behind sports outcomes. Most platforms show statistics; frame² explains why the season went the way it did, using one idea: **result = process + variance**.

> A self-contained analytics platform covering 58 seasons of Boston Red Sox history (1967–2024).  
> 7 macro-eras · 7 World Series appearances (4 wins) · wins, run-differential, OPS, ERA, and process tags for every season.

---

## Deploy in 2 minutes — Streamlit Community Cloud (free)

1. **Fork this repo** on GitHub
2. Go to **[share.streamlit.io](https://share.streamlit.io)** → "New app"
3. Set the fields:

   | Field | Value |
   |---|---|
   | Repository | `<your-username>/frame2-redsox-history` |
   | Branch | `main` |
   | Main file path | `app/app.py` |

4. Click **Deploy** — Streamlit Cloud auto-installs `requirements.txt` and `packages.txt`
5. Your app is live at `https://your-app-name.streamlit.app`

---

## Deploy on Railway (free tier available)

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

Railway reads the `Procfile` automatically:
```
web: streamlit run app/app.py --server.port=$PORT --server.address=0.0.0.0
```

---

## Deploy on Render

1. Create a new **Web Service** at [render.com](https://render.com)
2. Connect your GitHub repo
3. Set:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `streamlit run app/app.py --server.port=$PORT --server.address=0.0.0.0`

---

## Run Locally

```bash
git clone https://github.com/dualityframework-ux/frame2-redsox-history.git
cd frame2-redsox-history

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

streamlit run app/app.py
# Opens at http://localhost:8501
```

---

## Project Structure

```
frame2-redsox-history/
│
├── app/
│   ├── app.py                              # Streamlit entry point
│   └── pages/
│       ├── 01_home.py                      # Home
│       ├── 02_era_comparison.py            # Era comparison dashboard
│       ├── 03_redsox_tilt_intelligence.py  # Tilt (process vs result) signals
│       ├── 04_redsox_history_home.py       # History landing dashboard
│       ├── 05_redsox_season_explorer.py    # Season-by-season explorer
│       ├── 06_redsox_process_vs_result.py  # Process vs result analysis
│       ├── 07_redsox_era_board.py          # Era leaderboard
│       ├── 08_redsox_history_post_generator.py  # Social post generator
│       ├── 09_redsox_franchise_timeline.py # Main timeline + exports
│       ├── 10_redsox_core_pipeline_explorer.py  # Core + pipeline explorer
│       └── 12_redsox_live_game.py          # Live game module (MLB Stats API)
│
├── storage/parquet/
│   ├── redsox_history.csv                  # 58 rows, 14 columns incl. key_players
│   └── redsox_core_pipeline.csv
│
├── adapters/                               # Data loaders
├── intelligence/                           # Signal/noise engine
├── content_engine/                         # Post generator
├── config/                                 # Settings, styles, utils
├── tests/                                  # pytest suite (214 tests)
│
├── export_era_comparison_pdf.py            # Era comparison PDF (10 pages)
├── build_timeline_slideshow.py             # 17-slide PPTX
├── generate_web_timeline.py                # Desktop HTML timeline
├── generate_mobile_timeline.py             # Mobile-responsive HTML
│
├── .streamlit/config.toml                  # Dark Red Sox theme + server config
├── requirements.txt                        # Python dependencies
├── packages.txt                            # System packages (Streamlit Cloud)
├── Procfile                                # Railway / Render start command
└── .gitignore
```

---

## Data Schema

`storage/parquet/redsox_history.csv` — 58 rows × 14 columns

| Column | Type | Description |
|---|---|---|
| season | int | 1967–2024 |
| wins / losses | int | Regular season record |
| run_diff | int | Team run differential |
| playoff_result | str | "world series", "lost alcs", "missed playoffs", etc. |
| team_ops / obp / slg | float | Offensive triple-slash |
| team_era / fip | float | Pitching metrics |
| manager | str | Primary season manager |
| era_label | str | Short contextual label |
| mechanism_summary | str | 1-sentence process narrative |
| key_players | str | Comma-separated key contributors |

---

## Macro-Eras

| Era | Years | Avg W | Avg RD | WS | Playoff% |
|---|---|---|---|---|---|
| Yaz Era | 1967–1976 | 87.3 | +50 | 2 | 20% |
| Rice & Lynn | 1977–1986 | 85.8 | +66 | 1 | 20% |
| Boggs & Clemens | 1987–1996 | 80.0 | +18 | 0 | 30% |
| Pedro & Manny | 1997–2006 | 89.8 | +96 | 1 | 50% |
| Francona Dynasty | 2007–2013 | 90.1 | +119 | 2 | 57% |
| Betts Emergence | 2014–2019 | 87.8 | +86 | 1 | 50% |
| Rebuild & Now | 2020–2024 | 70.6 | −6 | 0 | 20% |

---

## Export Tools (CLI)

```bash
# Era comparison PDF (10 pages)
python export_era_comparison_pdf.py [output.pdf]

# Franchise timeline PPTX (17 slides)
python build_timeline_slideshow.py [output.pptx]

# Desktop interactive HTML
python generate_web_timeline.py [output.html]

# Mobile-responsive HTML
python generate_mobile_timeline.py [output.html]
```

All four are also available as **in-app download buttons** on the timeline and era comparison pages.

---

## Process Tags

Each season's record is compared with the wins its run differential was worth (81 + run diff ÷ 10), both scaled to 162 games so shortened seasons compare fairly. Luck is the gap.

| Tag | Rule |
|---|---|
| **Overperformed** | Win pace at least 4 wins above expected |
| **Underperformed** | Win pace at least 4 wins below expected |
| **Signal** | 95+ win pace within 4 wins of expected: elite process matched an elite record |
| **Balanced** | Everything else |

The band is `LUCK_BAND` in `config/settings.py`. The app, the timelines and the exports all use this one rule.

---|---|
| **Signal** | ≥95 W + ≥80 RD — elite process matched elite result |
| **Balanced** | Wins and run-differential roughly aligned |
| **Overperformed** | Wins outran the run-differential expectation |
| **Underperformed** | Run-differential was stronger than the win total |

---

## Requirements

Python 3.10+. Dependencies are listed in [`requirements.txt`](requirements.txt). Streamlit Community Cloud installs the system fonts in `packages.txt` automatically.

---

## Tests

```bash
pip install -r requirements.txt pytest
PYTHONPATH=. pytest -q
```

The suite covers the data adapters, settings, data integrity (58 seasons, 1967–2024, 7 World Series appearances), the history and signal/noise engines, the orchestrator and the post generator. GitHub Actions runs it on every push to `main`.

---

## Version History

| Version | Key Addition |
|---|---|
| v1–v4 | Core app, data pipeline, home/explorer pages |
| v5 | Timeline era filters, multiselect, shaded bands |
| v6 | Era comparison page — 7 Plotly charts |
| v7 | PDF export (`export_era_comparison_pdf.py`) |
| v8 | PPTX slideshow (`build_timeline_slideshow.py`, 17 slides) |
| v9 | Desktop interactive HTML (`generate_web_timeline.py`) |
| v10 | Mobile-responsive HTML · `.streamlit/config.toml` · `packages.txt` · `Procfile` |

---

*frame² analytics · Red Sox Franchise History · 1967–2024*

## License

MIT — see [LICENSE](LICENSE).

# 30-Year Mortgage Rate Today — Live Freddie Mac PMMS Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit-mortgage-rate-today.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Data: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Dataset DOI](https://img.shields.io/badge/Dataset%20DOI-10.6084%2Fm9.figshare.32332290-blue)](https://doi.org/10.6084/m9.figshare.32332290)

**Free, interactive Streamlit dashboard for the US 30-year fixed mortgage rate** — live data from the Freddie Mac Primary Mortgage Market Survey (PMMS) via FRED, plus 50-year history, 15-year fixed comparison, and 10-year US Treasury yield overlay for spread analysis.

🔗 **Live app**: <https://streamlit-mortgage-rate-today.streamlit.app/>

## What this dashboard shows

- **Current 30-year fixed mortgage rate** — Freddie Mac PMMS, updated each Thursday
- **Current 15-year fixed mortgage rate**
- **All-time high** (October 1981 — 18.63% — peak Volcker-era rate hikes)
- **All-time low** (January 2021 — 2.65% — COVID-era policy easing)
- **50-year average** of weekly PMMS observations (1976-2026)
- **50-year history chart** — 30Y vs 15Y fixed, interactive zoom
- **30Y mortgage vs 10Y Treasury overlay** with current spread vs historical average

## Data sources (all primary, CC BY 4.0)

- **30-year fixed mortgage rate**: [FRED MORTGAGE30US](https://fred.stlouisfed.org/series/MORTGAGE30US) (Freddie Mac PMMS, weekly since April 1971)
- **15-year fixed mortgage rate**: [FRED MORTGAGE15US](https://fred.stlouisfed.org/series/MORTGAGE15US) (Freddie Mac PMMS, since 1991)
- **10-year US Treasury constant maturity yield**: [FRED DGS10](https://fred.stlouisfed.org/series/DGS10) (US Treasury, since 1962)

Mirrored verbatim from the primary publishers — no transformations, smoothing, or imputations. CSV comment headers preserve source URL, retrieval timestamp, and license.

## Companion ecosystem

This Streamlit app is part of the **CalcFi Open Data** project — 34 free CC BY 4.0 financial and macroeconomic time series mirrored verbatim from primary sources (FRED, BLS, Freddie Mac, US Treasury, BEA, World Bank, Federal Reserve, FDIC, EIA).

### Use the same data

- **Python**: `pip install calcfidata` ([PyPI](https://pypi.org/project/calcfidata/) · [Anaconda](https://anaconda.org/jeresalmisto/calcfidata) · [conda-forge PR](https://github.com/conda-forge/staged-recipes/pull/33436))
- **R**: `install.packages("calcfidata")` (under CRAN review)
- **Go**: `go get gitlab.com/jere.salmisto/calcfi-open-data/go`
- **Node/JS/TS**: `npm install calcfidata`
- **Julia**: `Pkg.add("CalcFiData")` (Julia General registry pending)
- **dbt package**: [hub.getdbt.com/jeresalmisto/calcfi_open_data](https://hub.getdbt.com/jeresalmisto/calcfi_open_data/latest/) (pending merge)

### Query surfaces

- **Live SQL (Datasette)**: <https://calcfi-open-data.vercel.app/>
- **BigQuery Public Datasets**: [Analytics Hub listing](https://console.cloud.google.com/bigquery/analytics-hub/discovery/projects/1099067620437/locations/us/dataExchanges/calcfi_open_data_exchange/listings/calcfi_open_data)
- **AWS S3 Public Bucket**: <https://calcfi-open-data.s3.us-east-1.amazonaws.com/>
- **data.world**: <https://data.world/jerehere/calcfi-open-data>
- **MotherDuck (cloud DuckDB)**: `ATTACH 'md:_share/calcfi_open_data_share/92e4b6ab-46e0-42f4-8ebb-9e7ab22eae00'`
- **DoltHub (git-for-data)**: <https://www.dolthub.com/repositories/jerehere/calcfi-open-data>
- **Hugging Face Datasets**: <https://huggingface.co/datasets/iizy/calcfi-open-data>

### Documentation

- [calcfidata.readthedocs.io](https://calcfidata.readthedocs.io/) — full reference
- [calcfi-open-data-4a2bc1.gitlab.io](https://calcfi-open-data-4a2bc1.gitlab.io/) — documentation hub
- [Methodology paper (under SSRN review)](https://calcfi-open-data-4a2bc1.gitlab.io/methodology.html)

### Permanent DOIs

[Figshare](https://doi.org/10.6084/m9.figshare.32332290) · [Zenodo](https://doi.org/10.5281/zenodo.20302283) · [OSF](https://doi.org/10.17605/OSF.IO/PUMKT) · [Kaggle](https://doi.org/10.34740/kaggle/dsv/16356447) · [Mendeley Data](https://data.mendeley.com/datasets/jsnwhy6vjn/1)

## Free mortgage payment calculator

To compute your own mortgage payment (with state-specific tax, PMI, refi comparison), use the free [**CalcFi mortgage payment calculator**](https://calcfi.app/calculators/mortgage-payment) — 300+ tools built on the same primary-source data layer, all cited.

## Run locally

```bash
git clone https://github.com/jeresalmisto/streamlit-mortgage-rate-today.git
cd streamlit-mortgage-rate-today
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy on Streamlit Community Cloud

1. Fork this repo to your GitHub
2. Sign in at <https://share.streamlit.io>
3. Click "New app", pick this repo, branch `main`, file `streamlit_app.py`
4. Deploy — app lives at `https://<your-username>-streamlit-mortgage-rate-today.streamlit.app/`

## License

- **Code**: MIT
- **Data**: CC BY 4.0 — attribution requested to CalcFi (https://calcfi.app) and Freddie Mac PMMS

## Author

**Jere Salmisto** — Independent researcher, founder of [calcfi.app](https://calcfi.app). ORCID: [0009-0000-0916-8684](https://orcid.org/0009-0000-0916-8684).

## Citation

```bibtex
@dataset{salmisto_2026_calcfi_open_data,
  author    = {Salmisto, Jere},
  title     = {CalcFi Open Data: 34 Free CC-BY Financial and Macro Time Series Mirrored from Primary Sources},
  year      = 2026,
  publisher = {Figshare},
  doi       = {10.6084/m9.figshare.32332290}
}
```

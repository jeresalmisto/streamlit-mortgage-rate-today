"""
30-Year Mortgage Rate Today — Live Freddie Mac PMMS + 50-Year History

A free interactive Streamlit dashboard built on CalcFi Open Data.
https://calcfidata.readthedocs.io/
"""
import calcfidata as cf
import pandas as pd
import streamlit as st
import altair as alt

# ============================================================
# Page config — title, description, favicon, layout
# ============================================================
st.set_page_config(
    page_title="30-Year Mortgage Rate Today — Live Freddie Mac PMMS & 50-Year History | CalcFi Open Data",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://calcfidata.readthedocs.io/",
        "Report a bug": "https://github.com/jeresalmisto/streamlit-mortgage-rate-today/issues",
        "About": (
            "**30-Year Mortgage Rate Today** — Live US 30-year and 15-year fixed mortgage rates "
            "from the Freddie Mac Primary Mortgage Market Survey (PMMS) via FRED. "
            "50-year history (1976-2026). 2,600+ weekly observations. "
            "Powered by [CalcFi Open Data](https://calcfidata.readthedocs.io/) — "
            "34 free CC BY 4.0 financial and macroeconomic time series mirrored verbatim "
            "from primary sources. Maintained by [Jere Salmisto](https://orcid.org/0009-0000-0916-8684), "
            "founder of [calcfi.app](https://calcfi.app)."
        ),
    },
)

# ============================================================
# Inject SEO meta tags + Schema.org Dataset JSON-LD via HTML
# ============================================================
st.markdown(
    """
<!-- SEO meta tags -->
<meta name="description" content="Live 30-year fixed mortgage rate from Freddie Mac PMMS. 50-year history (1976-2026). Free, CC BY 4.0, primary-source data. Includes 15-year fixed + 10-year Treasury overlay. Updated weekly Thursdays.">
<meta name="keywords" content="mortgage rate today, 30 year mortgage rate, 15 year mortgage rate, Freddie Mac PMMS, mortgage rate history, FRED MORTGAGE30US, 10 year Treasury yield, mortgage Treasury spread, refinance rates, housing market, CC BY 4.0">
<meta name="author" content="Jere Salmisto">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="https://streamlit-mortgage-rate-today.streamlit.app/">

<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:title" content="30-Year Mortgage Rate Today — Live Freddie Mac PMMS & 50-Year History">
<meta property="og:description" content="Live US mortgage rates + 50-year history. Free, CC BY 4.0, sourced from Freddie Mac PMMS via FRED.">
<meta property="og:url" content="https://streamlit-mortgage-rate-today.streamlit.app/">
<meta property="og:image" content="https://calcfi.app/og/mortgage-rate.png">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="30-Year Mortgage Rate Today — Live Freddie Mac PMMS">
<meta name="twitter:description" content="Live US mortgage rates from Freddie Mac PMMS + 50-year history. Free CC BY 4.0.">

<!-- Schema.org Dataset + WebApplication JSON-LD -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "30-Year Mortgage Rate Today",
  "description": "Live US 30-year fixed mortgage rate from Freddie Mac PMMS, with 50-year history (1976-2026), 15-year fixed comparison, and 10-year Treasury yield overlay. Free, CC BY 4.0.",
  "url": "https://streamlit-mortgage-rate-today.streamlit.app/",
  "applicationCategory": "FinanceApplication",
  "operatingSystem": "Web",
  "isAccessibleForFree": true,
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "creator": {
    "@type": "Person",
    "name": "Jere Salmisto",
    "identifier": "https://orcid.org/0009-0000-0916-8684",
    "url": "https://calcfi.app/about",
    "sameAs": [
      "https://orcid.org/0009-0000-0916-8684",
      "https://github.com/jeresalmisto",
      "https://gitlab.com/jere.salmisto",
      "https://huggingface.co/iizy"
    ]
  },
  "isBasedOn": {
    "@type": "Dataset",
    "name": "CalcFi Open Data",
    "url": "https://calcfidata.readthedocs.io/",
    "sameAs": [
      "https://doi.org/10.6084/m9.figshare.32332290",
      "https://huggingface.co/datasets/iizy/calcfi-open-data"
    ]
  },
  "keywords": "mortgage rate today, 30 year mortgage, 15 year mortgage, Freddie Mac PMMS, FRED, mortgage history, Treasury yield, housing market, refinance"
}
</script>
""",
    unsafe_allow_html=True,
)

# ============================================================
# Sidebar — navigation + companion clients + data sources
# ============================================================
with st.sidebar:
    st.markdown("### 🏠 Mortgage Rate Today")
    st.markdown(
        "Free interactive dashboard. Data: **Freddie Mac PMMS** via FRED "
        "(MORTGAGE30US, MORTGAGE15US) + US Treasury 10-year (DGS10). "
        "Updated each Thursday."
    )
    st.divider()
    st.markdown("### Data sources (primary)")
    st.markdown(
        """
- [FRED MORTGAGE30US (Freddie Mac PMMS 30Y)](https://fred.stlouisfed.org/series/MORTGAGE30US)
- [FRED MORTGAGE15US (Freddie Mac PMMS 15Y)](https://fred.stlouisfed.org/series/MORTGAGE15US)
- [FRED DGS10 (US Treasury 10Y)](https://fred.stlouisfed.org/series/DGS10)
"""
    )
    st.divider()
    st.markdown("### Use the data")
    st.markdown(
        """
- 🐍 **Python**: `pip install calcfidata` ([PyPI](https://pypi.org/project/calcfidata/))
- 📦 **Conda**: `conda install -c jeresalmisto calcfidata` ([Anaconda](https://anaconda.org/jeresalmisto/calcfidata))
- 📊 **R**: `install.packages("calcfidata")` (CRAN pending)
- 🟢 **Node**: `npm install calcfidata` ([npm](https://www.npmjs.com/package/calcfidata))
- 🐹 **Go**: `go get gitlab.com/jere.salmisto/calcfi-open-data/go`
- 🟣 **Julia**: `Pkg.add("CalcFiData")` (pending)
"""
    )
    st.divider()
    st.markdown("### Query surfaces")
    st.markdown(
        """
- [📊 Live SQL (Datasette)](https://calcfi-open-data.vercel.app/)
- [☁️ BigQuery Public Datasets](https://console.cloud.google.com/bigquery/analytics-hub/discovery/projects/1099067620437/locations/us/dataExchanges/calcfi_open_data_exchange/listings/calcfi_open_data)
- [🪣 AWS S3 Public](https://calcfi-open-data.s3.us-east-1.amazonaws.com/)
- [🌐 data.world](https://data.world/jerehere/calcfi-open-data)
- [🦆 MotherDuck](https://app.motherduck.com/share/92e4b6ab-46e0-42f4-8ebb-9e7ab22eae00)
- [🌳 DoltHub (versioned)](https://www.dolthub.com/repositories/jerehere/calcfi-open-data)
"""
    )
    st.divider()
    st.markdown("### Calculate your payment")
    st.markdown(
        "Use the free [**CalcFi mortgage payment calculator**](https://calcfi.app/calculators/mortgage-payment) — "
        "compute total cost, principal vs interest split, refi savings."
    )
    st.divider()
    st.caption(
        "Built by [Jere Salmisto](https://orcid.org/0009-0000-0916-8684), founder of [calcfi.app](https://calcfi.app). "
        "[Documentation](https://calcfidata.readthedocs.io/) · [Methodology](https://calcfi-open-data-4a2bc1.gitlab.io/methodology.html) · "
        "[DOI](https://doi.org/10.6084/m9.figshare.32332290)"
    )

# ============================================================
# Title + hero
# ============================================================
st.title("🏠 30-Year Mortgage Rate Today")
st.markdown(
    "Free interactive dashboard. Live **30-year fixed** and **15-year fixed** US mortgage rates "
    "from the **Freddie Mac Primary Mortgage Market Survey (PMMS)** via FRED, with **50-year history (1976-2026)** "
    "and **10-year Treasury yield** overlay for spread analysis. "
    "All data CC BY 4.0, sourced verbatim from primary publishers."
)

# ============================================================
# Load data
# ============================================================
@st.cache_data(ttl=3600)
def load_all():
    df30 = cf.load("30-year-fixed").rename(columns={"value": "30Y Fixed"})
    df15 = cf.load("15-year-fixed").rename(columns={"value": "15Y Fixed"})
    df10 = cf.load("10-year-treasury").rename(columns={"value": "10Y Treasury"})
    return df30, df15, df10


with st.spinner("Loading 50 years of Freddie Mac PMMS + Treasury data…"):
    df30, df15, df10 = load_all()

# ============================================================
# KPIs row
# ============================================================
latest_30 = df30.iloc[-1]
latest_15 = df15.iloc[-1]
all_time_high_30 = df30.loc[df30["30Y Fixed"].idxmax()]
all_time_low_30 = df30.loc[df30["30Y Fixed"].idxmin()]
fifty_yr_avg_30 = df30["30Y Fixed"].mean()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(
        label="Current 30Y rate",
        value=f"{latest_30['30Y Fixed']:.2f}%",
        help=f"As of {latest_30['date'].strftime('%Y-%m-%d')} — Freddie Mac PMMS",
    )
with col2:
    st.metric(
        label="Current 15Y rate",
        value=f"{latest_15['15Y Fixed']:.2f}%",
        help=f"As of {latest_15['date'].strftime('%Y-%m-%d')} — Freddie Mac PMMS",
    )
with col3:
    st.metric(
        label="All-time high (30Y)",
        value=f"{all_time_high_30['30Y Fixed']:.2f}%",
        help=f"{all_time_high_30['date'].strftime('%B %Y')} — peak inflation era",
    )
with col4:
    st.metric(
        label="50-yr average (30Y)",
        value=f"{fifty_yr_avg_30:.2f}%",
        help="1976-2026 mean of weekly PMMS observations",
    )

st.divider()

# ============================================================
# Chart 1: 50-year history
# ============================================================
st.subheader("50-year US mortgage rate history (Freddie Mac PMMS, 1976-2026)")
combined = (
    df30[["date", "30Y Fixed"]]
    .merge(df15[["date", "15Y Fixed"]], on="date", how="outer")
    .melt(id_vars="date", var_name="Series", value_name="Rate (%)")
)
chart = (
    alt.Chart(combined)
    .mark_line()
    .encode(
        x=alt.X("date:T", title="Year"),
        y=alt.Y("Rate (%):Q", title="Rate (%)"),
        color=alt.Color(
            "Series:N",
            scale=alt.Scale(range=["#0a66c2", "#e57373"]),
            legend=alt.Legend(title=None),
        ),
        tooltip=["date:T", "Series:N", alt.Tooltip("Rate (%):Q", format=".2f")],
    )
    .properties(height=420)
    .interactive()
)
st.altair_chart(chart, use_container_width=True)

# ============================================================
# Chart 2: Mortgage-Treasury spread
# ============================================================
st.subheader("30-year mortgage vs 10-year US Treasury — current spread")
spread = df30[["date", "30Y Fixed"]].merge(
    df10[["date", "10Y Treasury"]], on="date", how="inner"
)
spread["Spread (pp)"] = (spread["30Y Fixed"] - spread["10Y Treasury"]).round(3)

col_a, col_b = st.columns([3, 1])
with col_a:
    melted = spread.melt(
        id_vars="date",
        value_vars=["30Y Fixed", "10Y Treasury"],
        var_name="Series",
        value_name="Rate (%)",
    )
    overlay = (
        alt.Chart(melted)
        .mark_line()
        .encode(
            x=alt.X("date:T", title="Year"),
            y=alt.Y("Rate (%):Q", title="Rate (%)"),
            color=alt.Color("Series:N", scale=alt.Scale(range=["#0a66c2", "#fbb040"])),
            tooltip=["date:T", "Series:N", alt.Tooltip("Rate (%):Q", format=".2f")],
        )
        .properties(height=320)
        .interactive()
    )
    st.altair_chart(overlay, use_container_width=True)
with col_b:
    current_spread = spread.iloc[-1]["Spread (pp)"]
    avg_spread = spread["Spread (pp)"].mean()
    st.metric("Current spread", f"{current_spread:.2f}pp")
    st.metric("Historical avg", f"{avg_spread:.2f}pp")
    st.caption(
        "The 30Y mortgage rate typically runs **~1.7pp above** the 10Y Treasury. "
        "Wide spread = lender risk premium high; narrow = competitive market."
    )

# ============================================================
# About / methodology
# ============================================================
st.divider()
with st.expander("📚 Methodology + citation"):
    st.markdown(
        """
**Data sources** (all primary, CC BY 4.0):

- **30-year fixed mortgage rate**: [Freddie Mac PMMS](https://www.freddiemac.com/pmms) via [FRED MORTGAGE30US](https://fred.stlouisfed.org/series/MORTGAGE30US) — weekly, since April 1971.
- **15-year fixed mortgage rate**: [Freddie Mac PMMS](https://www.freddiemac.com/pmms) via [FRED MORTGAGE15US](https://fred.stlouisfed.org/series/MORTGAGE15US) — weekly, since 1991.
- **10-year US Treasury constant maturity yield**: [US Treasury](https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics) via [FRED DGS10](https://fred.stlouisfed.org/series/DGS10) — daily, since 1962.

All values mirrored **verbatim** from the primary publishers — no transformations, smoothing, or imputations. CSV comment headers preserve source URL, retrieval timestamp, and license.

**Refresh cadence**: weekly Thursday morning (when Freddie Mac publishes new PMMS reading). Cached for 1 hour in this app.

**Cite this dataset**:
> Salmisto, J. (2026). *CalcFi Open Data: 34 Free CC-BY Financial and Macro Time Series Mirrored from Primary Sources* [Dataset]. Figshare. [10.6084/m9.figshare.32332290](https://doi.org/10.6084/m9.figshare.32332290)

[Full methodology paper](https://calcfi-open-data-4a2bc1.gitlab.io/methodology.html) (under review at SSRN).
"""
    )

st.caption(
    "Built with [Streamlit](https://streamlit.io/) + [Altair](https://altair-viz.github.io/) + "
    "[`pip install calcfidata`](https://pypi.org/project/calcfidata/). "
    "Source: [github.com/jeresalmisto/streamlit-mortgage-rate-today](https://github.com/jeresalmisto/streamlit-mortgage-rate-today). "
    "License: MIT (code) + CC BY 4.0 (data)."
)

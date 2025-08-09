# Data Collection and Web Scraping

This repository contains data collection and web scraping projects for AI Saturdays Lagos Cohort 9.

## 📁 Project Structure

```
data_collection_web_scraping/
├── finance_data/
│   ├── scrape_script.py       # Finance data collection using yfinance
│   └── data/                  # Generated CSV files (excluded from git)
├── agricultural_data/
│   └── (future projects)
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd data_collection_web_scraping
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## 📈 Finance Data Collection

### Features

- Collect historical currency pair data using Yahoo Finance
- Support for multiple currency pairs
- Configurable date ranges
- Automatic CSV export with timestamps
- Data quality analysis

### Supported Currency Pairs

- EUR/USD (`EURUSD=X`)
- GBP/USD (`GBPUSD=X`)
- USD/JPY (`USDJPY=X`)
- USD/CAD (`USDCAD=X`)
- AUD/USD (`AUDUSD=X`)



## 📋 Requirements

```
yfinance>=0.2.18
pandas>=1.5.0
pathlib
typing
```
# Financial Market Data Pipeline

A Python-MySQL data analysis pipeline for collecting, storing, and analyzing financial market data. Built as a project-based-learning. 

## Project Overview

This project implements an end-to-end data pipeline that:
- Fetches historical stock market data from financial APIs
- Stores data efficiently in a MySQL database
- Performs quantitative analysis and calculates key metrics
- Generates visualizations and insights for investment analysis

## Features

- **Data Collection**: Automated fetching of stock data (OHLCV) from Yahoo Finance API
- **Database Management**: Structured MySQL schema for efficient time-series data storage
- **Data Processing**: Calculate returns, moving averages, volatility, and correlations
- **Analysis Engine**: Generate financial metrics and risk indicators
- **Visualization**: Interactive charts for price trends and comparative analysis
- **Portfolio Analysis**: Basic portfolio allocation and performance tracking

## Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher
- Basic understanding of Python and SQL
- Git for version control

## Tech Stack

- **Python Libraries**:
  - `pandas` - Data manipulation and analysis
  - `numpy` - Numerical computations
  - `mysql-connector-python` - MySQL database connectivity
  - `yfinance` - Yahoo Finance API wrapper
  - `matplotlib` / `plotly` - Data visualization
  - `python-dotenv` - Environment variable management

- **Database**: MySQL 8.0+
- **Version Control**: Git & GitHub

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/Financial-Market-Data-Pipeline.git
cd financial-market-pipeline
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up MySQL database**
```bash
mysql -u root -p < database/schema.sql
```

5. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your MySQL credentials
```

## Project Structure

```
financial-market-data-pipeline/
│
├── data/                      # Raw and processed data files
│   ├── raw/                   # Raw data from APIs
│   └── processed/             # Cleaned and processed data
│
├── database/                  # Database related files
│   ├── schema.sql            # MySQL database schema
│   └── queries.sql           # Common SQL queries
│
├── src/                       # Source code
│   ├── __init__.py
│   ├── data_collector.py     # API data fetching
│   ├── database.py           # Database operations
│   ├── analyzer.py           # Data analysis functions
│   └── visualizer.py         # Visualization functions
│
├── notebooks/                 # Jupyter notebooks for exploration
│   └── exploratory_analysis.ipynb
│
├── tests/                     # Unit tests
│   └── test_data_collector.py
│
├── config/                    # Configuration files
│   └── config.py
│
├── .env.example              # Example environment variables
├── .gitignore                # Git ignore file
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── main.py                   # Main entry point
```

## Quick Start

1. **Fetch stock data**
```bash
python main.py --fetch --symbols AAPL MSFT GOOGL --period 1y
```

2. **Load data to database**
```bash
python main.py --load
```

3. **Run analysis**
```bash
python main.py --analyze --symbols AAPL MSFT
```

4. **Generate visualizations**
```bash
python main.py --visualize --symbols AAPL
```

## Database Schema

### Tables

**stocks**
- `stock_id` (Primary Key)
- `symbol` (Ticker symbol)
- `company_name`
- `sector`
- `industry`

**prices**
- `price_id` (Primary Key)
- `stock_id` (Foreign Key)
- `date`
- `open`, `high`, `low`, `close`
- `volume`
- `adj_close`

**metrics**
- `metric_id` (Primary Key)
- `stock_id` (Foreign Key)
- `date`
- `daily_return`
- `volatility`
- `sma_20`, `sma_50`

## Usage Examples

### Fetch data for multiple stocks
```python
from src.data_collector import StockDataCollector

collector = StockDataCollector()
data = collector.fetch_stocks(['AAPL', 'MSFT', 'GOOGL'], period='1y')
```

### Calculate returns and volatility
```python
from src.analyzer import FinancialAnalyzer

analyzer = FinancialAnalyzer()
returns = analyzer.calculate_returns('AAPL')
volatility = analyzer.calculate_volatility('AAPL', window=30)
```

## Learning Objectives

This project helps build skills in:
- Time-series data management
- Financial data APIs and data quality
- Database design for financial applications
- Quantitative analysis techniques
- Python for financial engineering

## Roadmap

- [x] Project setup and documentation
- [ ] Week 1: Data collection from Yahoo Finance API
- [ ] Week 2: MySQL database design and data loading
- [ ] Week 3: Financial metrics calculation
- [ ] Week 4: Visualization and reporting
- [ ] Week 5: Portfolio analysis features
- [ ] Week 6: Basic backtesting framework


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Yahoo Finance API for providing free financial data
- The quantitative finance community for inspiration

---

**Note**: This project is for educational purposes only. Not financial advice.

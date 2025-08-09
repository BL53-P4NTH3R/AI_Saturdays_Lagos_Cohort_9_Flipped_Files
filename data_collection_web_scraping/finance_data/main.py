from pathlib import Path
from datetime import datetime, timedelta
from scrape_script import Finance


# Currency pairs
currency_pairs = ['EURUSD=X', 'GBPUSD=X', 'USDJPY=X', 'USDCAD=X', 'AUDUSD=X']

# dates
end_date = datetime.now()
start_date = end_date - timedelta(days=10*365)

# location
location = './datasets'

# Finance data
finance = Finance(currency_pairs, start_date, end_date, location)
finance.get_data()
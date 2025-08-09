# Import packages
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
from typing import List

# TODO: Create a function to get the currency pair from a within a particular time
# TODO: Save the data into a csv location


class Finance:
    def __init__(self, currency_pairs: List[str], start_date: datetime, end_date: datetime, location: Path):
        """
        
        """
        self.currency_pairs = currency_pairs
        self.start_date = start_date
        self.end_date = end_date
        self.location = location

    def get_data(self):
        """Get the currency pairs from yfinance and saved it as a csv in the specified location"""
        currency_data = yf.download(
            self.currency_pairs,
            start=self.start_date.strftime('%Y-%m-%d'),
            end=self.end_date.strftime('%Y-%m-%d')
        )
        currency_data.to_csv(f'{self.location}/finance_data.csv', index=False)

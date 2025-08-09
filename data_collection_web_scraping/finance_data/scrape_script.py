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
        Initialize Finance class for currency data collection
        
        Args:
            currency_pairs: List of currency pairs (e.g., ['EURUSD=X', 'GBPUSD=X'])
            start_date: Start date for data collection
            end_date: End date for data collection
            location: Path to save the CSV file
        """
        self.currency_pairs = currency_pairs
        self.start_date = start_date
        self.end_date = end_date
        self.location = Path(location)

        # Create directory if it doesn't exist
        self.location.mkdir(parents=True, exist_ok=True)
    def get_data(self):
        """Get the currency pairs from yfinance and saved it as a csv in the specified location"""
        try:
            currency_data = yf.download(
                self.currency_pairs,
                start=self.start_date.strftime('%Y-%m-%d'),
                end=self.end_date.strftime('%Y-%m-%d')
            )

            # Save with timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"finance_data_{timestamp}.csv"
            filepath = self.location / filename

            currency_data.to_csv(filepath, index=False)
            print(f"Data saved successfully to: {filepath}")
            return currency_data
        
        except Exception as e:
            print(f"Error downloading data: {e}")
            return None
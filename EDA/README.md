
# Airline Flights EDA

## Overview
This project contains a detailed exploratory data analysis (EDA) of an airline flights dataset. The analysis was performed in the notebook `airlines_flights_eda.ipynb` and covers data structure, missing values, and key categorical distributions.

## Dataset Description
The dataset contains 300,152 rows and the following columns:

- `source_city`: City of departure
- `destination_city`: City of arrival
- `departure_time`: Scheduled departure time
- `arrival_time`: Scheduled arrival time
- `class`: Flight class (e.g., Economy, Business)
- `airline`: Airline operating the flight

## Data Quality
- **Number of Rows:** 300,152
- **Missing Values:** No empty values in any column (all columns are complete)

## Top 5 Value Counts

### Source City
1. Delhi: 61,343
2. Mumbai: 60,896
3. Bangalore: 52,061
4. Kolkata: 46,347
5. (Add 5th city if available)

### Destination City
1. Mumbai: 59097
2. Delhi: 57360
3. Bangalore: 52061
4. Kolkata: 46347
5. Hyderabad: 40806

### Departure Time (Most Common)
1. Morning: 71146
2. Early Morning: 66790
3. Evening: 65102
4. Night: 48015
5. Afternoon: 47794

### Arrival Time (Most Common)
1. Night: 91538
2. Evening: 78323
3. Morning: 62735
4. Afternoon: 38139
5. Early_Morning: 15417

### Class Distribution
- Economy: 206666
- Business: 93487

### Airline Distribution
(Replace with actual values from your analysis)
- Vistara: 127859
- Air India: 80892
- Indigo: 43120
import pandas as pd

# Save the Excel file as csv in the location of this .py file
# Reading the csv file.
df = pd.read_csv('jane street SettlementExercise.csv')

# Setting column "Trade date" to pandas datetime type.
df['Trade date'] = pd.to_datetime(df['Trade date'])

# Calculating Expected Settlement Date
df['Expected Settlement Date'] = df.apply(
    lambda row: row['Trade date'] + pd.DateOffset(days=2) if row.CSD == 'CREST' else row['Trade date'] + pd.DateOffset(
        days=3), axis=1)
print(df)
# Sort by Expected Settlement Date
df = df.sort_values(by='Expected Settlement Date')

# Initialize company stocks (position 0 is CREST, 1 is DTC, 2 is Strate)
AAPL_stocks = [100, 100, 100]
IBM_stocks = [100, 100, 100]
HTC_stocks = [100, 100, 100]
CSD_index = {'CREST': 0, 'DTC': 1, 'Strate': 2}

# Calculate stocks
for row in range(len(df)):
    csd = df.iloc[row]['CSD']
    security = df.iloc[row]['Security']
    if df.iloc[row]['Buy/Sell'] == 'B':
        command = f"{security}_stocks[CSD_index['{csd}']] += df.iloc[row]['Quantity']"
        exec(command)
    elif df.iloc[row]['Buy/Sell'] == 'S':
        command = f"{security}_stocks[CSD_index['{csd}']] -= df.iloc[row]['Quantity']"
        exec(command)

    # Output the stocks for each Security at each CSD at the end of each day
    if row == len(df) - 1 or df.iloc[row]['Expected Settlement Date'] != df.iloc[row + 1]['Expected Settlement Date']:
        print(f"-----Stocks for {df.iloc[row]['Expected Settlement Date']}-----")
        print(f'AAPL-> CREST={AAPL_stocks[0]}   DTC={AAPL_stocks[1]}   Strate={AAPL_stocks[2]}')
        print(f'IBM-> CREST={IBM_stocks[0]}   DTC={IBM_stocks[1]}   Strate={IBM_stocks[2]}')
        print(f'HTC-> CREST={HTC_stocks[0]}   DTC={HTC_stocks[1]}   Strate={HTC_stocks[2]}')

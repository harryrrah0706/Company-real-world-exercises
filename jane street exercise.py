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

# Group by security and sort by CSD
AAPL = df[df['Security'] == 'AAPL']
AAPL = AAPL.sort_values(by='CSD')
IBM = df[df['Security'] == 'IBM']
IBM = IBM.sort_values(by='CSD')
HTC = df[df['Security'] == 'HTC']
HTC = HTC.sort_values(by='CSD')

# Group by 22nd August
AAPL_22 = AAPL[AAPL['Expected Settlement Date'] == '2018-8-22']
IBM_22 = IBM[IBM['Expected Settlement Date'] == '2018-8-22']
HTC_22 = HTC[HTC['Expected Settlement Date'] == '2018-8-22']

# Group by 23th August
AAPL_23 = AAPL[AAPL['Expected Settlement Date'] == '2018-8-23']
IBM_23 = IBM[IBM['Expected Settlement Date'] == '2018-8-23']
HTC_23 = HTC[HTC['Expected Settlement Date'] == '2018-8-23']

# Group by 24th August
AAPL_24 = AAPL[AAPL['Expected Settlement Date'] == '2018-8-24']
IBM_24 = IBM[IBM['Expected Settlement Date'] == '2018-8-24']
HTC_24 = HTC[HTC['Expected Settlement Date'] == '2018-8-24']

# Initialize company stocks (position 0 is CREST, 1 is DTC, 2 is Strate)
AAPL_stocks = [100, 100, 100]
IBM_stocks = [100, 100, 100]
HTC_stocks = [100, 100, 100]
CSD_index = {'CREST': 0, 'DTC': 1, 'Strate': 2}

# Calculating stocks for AAPL, IBM and HTC on """August 22nd"""
for index in range(len(AAPL_22)):
    csd = AAPL_22.iloc[index]['CSD']
    if AAPL_22.iloc[index]['Buy/Sell'] == 'B':
        AAPL_stocks[CSD_index[csd]] += AAPL_22.iloc[index]['Quantity']
    elif AAPL_22.iloc[index]['Buy/Sell'] == 'S':
        AAPL_stocks[CSD_index[csd]] -= AAPL_22.iloc[index]['Quantity']

for index in range(len(IBM_22)):
    csd = IBM_22.iloc[index]['CSD']
    if IBM_22.iloc[index]['Buy/Sell'] == 'B':
        IBM_stocks[CSD_index[csd]] += IBM_22.iloc[index]['Quantity']
    elif IBM_22.iloc[index]['Buy/Sell'] == 'S':
        IBM_stocks[CSD_index[csd]] -= IBM_22.iloc[index]['Quantity']

for index in range(len(HTC_22)):
    csd = HTC_22.iloc[index]['CSD']
    if HTC_22.iloc[index]['Buy/Sell'] == 'B':
        HTC_stocks[CSD_index[csd]] += HTC_22.iloc[index]['Quantity']
    elif HTC_22.iloc[index]['Buy/Sell'] == 'S':
        HTC_stocks[CSD_index[csd]] -= HTC_22.iloc[index]['Quantity']
print('-----August 22-----')
print(f'AAPL-> CREST={AAPL_stocks[0]}   DTC={AAPL_stocks[1]}   Strate={AAPL_stocks[2]}')
print(f'IBM-> CREST={IBM_stocks[0]}   DTC={IBM_stocks[1]}   Strate={IBM_stocks[2]}')
print(f'HTC-> CREST={HTC_stocks[0]}   DTC={HTC_stocks[1]}   Strate={HTC_stocks[2]}')

# Calculating stocks for AAPL, IBM and HTC on """August 23th"""
for index in range(len(AAPL_23)):
    csd = AAPL_23.iloc[index]['CSD']
    if AAPL_23.iloc[index]['Buy/Sell'] == 'B':
        AAPL_stocks[CSD_index[csd]] += AAPL_23.iloc[index]['Quantity']
    elif AAPL_23.iloc[index]['Buy/Sell'] == 'S':
        AAPL_stocks[CSD_index[csd]] -= AAPL_23.iloc[index]['Quantity']

for index in range(len(IBM_23)):
    csd = IBM_23.iloc[index]['CSD']
    if IBM_23.iloc[index]['Buy/Sell'] == 'B':
        IBM_stocks[CSD_index[csd]] += IBM_23.iloc[index]['Quantity']
    elif IBM_23.iloc[index]['Buy/Sell'] == 'S':
        IBM_stocks[CSD_index[csd]] -= IBM_23.iloc[index]['Quantity']

for index in range(len(HTC_23)):
    csd = HTC_23.iloc[index]['CSD']
    if HTC_23.iloc[index]['Buy/Sell'] == 'B':
        HTC_stocks[CSD_index[csd]] += HTC_23.iloc[index]['Quantity']
    elif HTC_23.iloc[index]['Buy/Sell'] == 'S':
        HTC_stocks[CSD_index[csd]] -= HTC_23.iloc[index]['Quantity']
print('-----August 23-----')
print(f'AAPL-> CREST={AAPL_stocks[0]}   DTC={AAPL_stocks[1]}   Strate={AAPL_stocks[2]}')
print(f'IBM-> CREST={IBM_stocks[0]}   DTC={IBM_stocks[1]}   Strate={IBM_stocks[2]}')
print(f'HTC-> CREST={HTC_stocks[0]}   DTC={HTC_stocks[1]}   Strate={HTC_stocks[2]}')

# Calculating stocks for AAPL, IBM and HTC on """August 24th"""
for index in range(len(AAPL_24)):
    csd = AAPL_24.iloc[index]['CSD']
    if AAPL_24.iloc[index]['Buy/Sell'] == 'B':
        AAPL_stocks[CSD_index[csd]] += AAPL_24.iloc[index]['Quantity']
    elif AAPL_24.iloc[index]['Buy/Sell'] == 'S':
        AAPL_stocks[CSD_index[csd]] -= AAPL_24.iloc[index]['Quantity']

for index in range(len(IBM_24)):
    csd = IBM_24.iloc[index]['CSD']
    if IBM_24.iloc[index]['Buy/Sell'] == 'B':
        IBM_stocks[CSD_index[csd]] += IBM_24.iloc[index]['Quantity']
    elif IBM_24.iloc[index]['Buy/Sell'] == 'S':
        IBM_stocks[CSD_index[csd]] -= IBM_24.iloc[index]['Quantity']

for index in range(len(HTC_24)):
    csd = HTC_24.iloc[index]['CSD']
    if HTC_24.iloc[index]['Buy/Sell'] == 'B':
        HTC_stocks[CSD_index[csd]] += HTC_24.iloc[index]['Quantity']
    elif HTC_24.iloc[index]['Buy/Sell'] == 'S':
        HTC_stocks[CSD_index[csd]] -= HTC_24.iloc[index]['Quantity']
print('-----August 24-----')
print(f'AAPL-> CREST={AAPL_stocks[0]}   DTC={AAPL_stocks[1]}   Strate={AAPL_stocks[2]}')
print(f'IBM-> CREST={IBM_stocks[0]}   DTC={IBM_stocks[1]}   Strate={IBM_stocks[2]}')
print(f'HTC-> CREST={HTC_stocks[0]}   DTC={HTC_stocks[1]}   Strate={HTC_stocks[2]}')

import pandas as pd
import os

# By using pandas, read the "Data" sheet from the excel file and ignore the first two rows.
data = pd.read_excel('settlements_data_JS.xlsx', sheet_name="Data", skiprows=2)

# Total number of orders including Order and Shipment
number_of_orders = len(data)

# ------------------------------------------ Question 1A -------------------------------------------
# Initialize the Inventory Date column
inventory_dates = []

# Iterate through every row in the dataframe
for order in range(number_of_orders):
    # Get the current row's activity type, activity date and location of outlet.
    activity_type = data.loc[order, "Activity Type"]
    activity_date = data.loc[order, "Activity Date"]
    dee_location = data.loc[order, "Dee's Location"]
    # Add the days to activity date:
    #   the inventory for:
    #       - Order: add two days to activity date
    #       - Shipment: add one day to activity date if location of outlet is 1JS or 2WS
    #                   add two days to activity date if location of outlet is 3PUFF
    # Append the inventory date to the end of the list "inventory_date"
    if activity_type == "Order":
        inventory_dates.append(activity_date + pd.DateOffset(2))
    elif activity_type == "Shipment":
        if dee_location == "1JS" or dee_location == "2WS":
            inventory_dates.append(activity_date + pd.DateOffset(1))
        elif dee_location == "3PUFF":
            inventory_dates.append(activity_date + pd.DateOffset(2))

# Store the values of "inventory_dates" in the column "Inventory date"
data["Inventory Date"] = inventory_dates

# Convert the format of dates to MM-DD-YYYY.
data['Activity Date'] = data['Activity Date'].dt.strftime('%m/%d/%Y')
data['Inventory Date'] = data['Inventory Date'].dt.strftime('%m/%d/%Y')

# ------------------------------------------- Question 1B ------------------------------------------
# Create a sorted version of the dataframe "data" that is sorted by Inventory date.
sorted_data = data.sort_values(by='Inventory Date', ignore_index=True)
# Create the list of dates that we want to track the inventory, for this answer sheet we onlyzXZ
# have 08/22/2020 - 08/24/2020. If needed, we can add 08/25/2020 to "dates" as a string and
# the output will calculate the inventories for 25th of August as well.
dates = ['08/22/2020', '08/23/2020', '08/24/2020']

# Initialize the values for all outlets and all bakeries.
values = [[500, 500, 500],
          [500, 500, 500],
          [500, 500, 500]]

# I'll be using a while loop later to iterate through each row, here I initialize the row to zero.
row = 0

# The logic is that for each of the date in "dates", I will be creating a separate dataframe. The
# values of the new dataframe will be the set to the values of the previous dataframe. For
# example, dataframe for 08/22/2020 will use the initial values, and dataframe for 08/23/2020
# will use the values of dataframe for 08/22/2020. The dictionary "dataframes" contains the key (
# dates) and values of each dataframe.
dataframes = {}

# This is the index for dataframes, starting at zero. For example, index for dataframe 08/22/2020
# is 0, index for dataframe 08/23/2020 is 1...
index = 0

# Iterate through the date in "dates"
for date in dates:
    # Create the dataframe for the current date.
    # The column index are the name for each bakery
    # The row index are the location of outlets
    current_date = pd.DataFrame(values, columns=['AAPL', 'BBRD', 'CCC'])
    current_date.index = ["1JS", "2WS", "3PUFF"]

    # Perform operation of the dataframe "sorted_data" if the current inventory date is same as
    # the current date and "row" does not exceed the total number of orders.
    while sorted_data.loc[row, "Inventory Date"] == date and row < number_of_orders - 1:
        # Get the current row's inventory date, bakery, activity type, location of outlet and
        # quantity.
        inventory_date = sorted_data.loc[row, "Inventory Date"]
        bakery = sorted_data.loc[row, "Bakery Item"]
        activity_type = sorted_data.loc[row, "Activity Type"]
        dee_location = sorted_data.loc[row, "Dee's Location"]
        quantity = sorted_data.loc[row, "Quantity"]
        # If the activity type is Order, we subtract the original value by "quantity"
        # If the activity type is Shipment, we add the original value by "quantity"
        # I can access the specific element in the dataframe using row and column index.
        if activity_type == "Order":
            current_date.loc[dee_location][bakery] -= quantity
        elif activity_type == "Shipment" and inventory_date in dates:
            current_date.loc[dee_location][bakery] += quantity
        # Increment "row"
        row += 1
    # When the inventory date is not the same as the current date anymore, in other words,
    # if the current dataframe is 08/22/2020, and after I've finished operation on all orders on
    # 08/22/2020, and the inventory for next order is 08/23/2020 I jump out of the while loop and
    # store the current dataframe in the dictionary "dataframes" The two lines of code below
    # first makes a copy of the dataframe "current_date" and store it in the variable named
    # frame_number_0, and then store this variable in the dictionary with date as key and
    # dataframe as value.
    exec(f'frame_number_{index} = current_date.copy()')
    exec(f'dataframes[date] = frame_number_{index}')
    # Update the values for the next dataframe
    values = current_date.values
    # Increment the index
    index += 1

# Concatenate all dataframes into one dataframe horizontally. This final dataframe uses multi-index.
answers_sheet = pd.concat(dataframes.values(), axis=1, keys=dataframes.keys())

# Create a new excel file called "solution.xlsx" to store the answers.
directory = rf"{os.getcwd()}\solution.xlsx"
writer = pd.ExcelWriter(directory, engine='xlsxwriter')
# Write the dataframe called "data" in Question 1A to the sheet named "Data"
data.to_excel(writer, sheet_name='Data', index=False)
# Write the final answers for inventory tracking of each date in the sheet called "Answers sheet"
answers_sheet.to_excel(writer, sheet_name='Answers sheet')
# Write the sorted data to a new sheet called Sorted data, this is simply a sorted version of the
# "data"
sorted_data.to_excel(writer, sheet_name='Sorted data', index=False)

# ------------------------------------------- Question 2 -------------------------------------------
bakery_count_at_each_outlet = data.groupby("Dee's Location")["Bakery Item"].value_counts()
bakery_count_at_each_outlet.to_excel(writer, sheet_name='Orders per outlet')


writer.save()

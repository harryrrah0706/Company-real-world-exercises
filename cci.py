import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

df=pd.read_csv('2022 Data Case Study- NG Fundamental Test.csv')
df=df[['Month','Supply (Bcf/day)','Demand (Bcf/day)','Inventory (Bcf)','EDD','Price']]
# separate dataframe into train and test data sets
# use all data before 9/30/2022 to train the model
# and all the rest of the data to obtain predicted result
train=df[:104]
test=df[104:]
print(type(df.iloc[30:,1:5]))

# Creating the linear regression model called regr
regr = linear_model.LinearRegression()

# Separate the train dataset into x and y variables
# where x is EDD and y is Demand
train_x = train[['EDD']]
train_y = train[['Demand (Bcf/day)']]

# Fitting the training data into the regr model.
regr.fit(train_x, train_y)

# Examining the coefficient and intercept of the regr model.
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

# Plot the population graph of EDD versus Demand
plt.scatter(train.EDD, train['Demand (Bcf/day)'],  color='blue')

# Add the line of best fit into the population graph
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.xlabel("EDD")
plt.ylabel("Demand")
plt.show()

# using the build in function of the linear regression library
# to predict the demand using the EDD values in the test dataset
test_y_ = regr.predict(test[['EDD']])
print('Predicted Demand: ',test_y_)

# according to the equation of inventory level given case study sheet
# I created a for loop that goes through every row in the test dataset
# For every row, we obtain the total inventory and append it to the "predicted_inventory"
for i in range (104,len(df)):
    df['Demand (Bcf/day)'][i] = test_y_[i-104][0]
    df['Inventory (Bcf)'][i] = ( (df.iloc[i][1]) - df.iloc[i][2] ) * int( df.iloc[i][0][-7:-5] ) + df.iloc[i-1][3]
print(df[['Demand (Bcf/day)','Inventory (Bcf)']][104:])





df['surplus'] = df['Supply (Bcf/day)'] - df['Demand (Bcf/day)']
train=df[:104]
test=df[104:]
# Predict price with demand
train_x = train[['Demand (Bcf/day)']]
train_y = train[['Price']]
regr.fit(train_x, train_y)
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)
plt.scatter(train['Demand (Bcf/day)'], train.Price, color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.xlabel("Demand")
plt.ylabel("Price")
plt.show()
x = regr.predict(test[['Demand (Bcf/day)']])
print('Predicted Price with demand: ',x)






# Predict price with inventory
train_x = train[['Inventory (Bcf)']]
train_y = train[['Price']]
regr.fit(train_x, train_y)
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)
plt.scatter(train['Inventory (Bcf)'], train.Price, color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.xlabel("Inventory")
plt.ylabel("Price")
plt.show()
x = regr.predict(test[['Inventory (Bcf)']])
print('Predicted Price with inventory: ',x)





# Predict price with surplus
train_x = df[['surplus']][:104]
regr.fit(train_x, train_y)
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)
plt.scatter(train_x, train.Price, color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.xlabel("Surplus")
plt.ylabel("Price")
plt.show()
x = regr.predict(test[['surplus']])
print('Predicted Price with surplus: ',x)




df.to_csv('result.csv')
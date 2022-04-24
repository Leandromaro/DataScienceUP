import pandas as pd

print("--- Cleaning Data ---")

# Reading files.
print("0. Reading files")
df = pd.read_csv('../res/city_temperature.csv', low_memory=False)
country_naming_df = pd.read_csv('../res/country_naming.csv', low_memory=False)
city_naming_df = pd.read_csv('../res/city_naming.csv', low_memory=False)

##########################
# 1. Renaming the values #
##########################
print("1. Renaming")
# Getting the list of countries.
countries_key_list = list(df['Country'])
# Getting the list of cities.
cities_key_list = list(df['City'])
# Creating a lookup dictionary to get a value from the country_naming_df based on the list of counties of df.
countries_dict_lookup = dict(zip(country_naming_df['Country'], country_naming_df['Translation']))
region_dict_lookup = dict(zip(country_naming_df['Country'], country_naming_df['Continent']))
city_dict_lookup = dict(zip(city_naming_df['City'], city_naming_df['Translation']))

df['Region'] = [region_dict_lookup[item] for item in countries_key_list]
df['Country'] = [countries_dict_lookup[item] for item in countries_key_list]
df['City'] = [city_dict_lookup[item] for item in cities_key_list]

# Replacing nan values by a -
df['State'] = df['State'].fillna("-")


############################
# 2. Fahrenheit to Celsius #
############################
print("2. Fahrenheit to Celsius")
df['AvgTemperature'] = df['AvgTemperature'].apply(lambda x: float(round((x - 32) * 5 / 9, 2)))


###############################
# 3. Remove incomplete months #
###############################
print("3. Removing incomplete months")
ACCEPTABLE_NUMBER_OF_DAYS = 28

for i in range(0, ACCEPTABLE_NUMBER_OF_DAYS):
	# Creating a temp helper column to know which is the country of the previous row.
	df['Country_s'] = df['Country'].shift(-1)
	df['State_s'] = df['State'].shift(-1)
	# Creating a temp helper column to validate if the month is incomplete.
	countries_with_states = (df['Country'] == df['Country_s']) & (df['State'] != df['State_s'])
	countries_without_states = (df['Country'] != df['Country_s'])
	day_number = df['Day'].apply(lambda x: x < ACCEPTABLE_NUMBER_OF_DAYS)
	df['to_remove'] = (countries_without_states | countries_with_states) & day_number
	# Pandas deals with booleans in a really neat, straightforward manner
	# When you're filtering dataframes using df[...], you often write some function that returns
	# a boolean value (like df.x > 2). But in this case, since the column is already a boolean,
	# you can just put df.to_remove in on its own, which will get you all the rows that are True.
	# If you want to get the opposite you could use the ~, which inverts the booleans.
	df = df.loc[~df.to_remove, :]

# Removing the temp helper columns created to filter the data.
df = df.drop(['Country_s', 'State_s', 'to_remove'], axis=1)


# Saving file.
file_name = '../res/city_temperature_clean.csv'
print("4. Saving to file: " + file_name)
df.to_csv(file_name, index=False)

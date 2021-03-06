import os
import pandas as pd

dirname = os.path.dirname(__file__)
CITY_TEMPERATURE_PATH = os.path.join(dirname, '../res/city_temperature.csv')
COUNTRY_NAMING_PATH = os.path.join(dirname, '../res/country_naming.csv')
CITY_NAMING_PATH = os.path.join(dirname, '../res/city_naming.csv')
CITY_TEMPERATURE_CLEAN_PATH = os.path.join(dirname, '../res/clean/city_temperature_clean.csv')
ACCEPTABLE_NUMBER_OF_DAYS = 28

df = None
country_naming_df = None
city_naming_df = None


def clean_data():
	global df
	global country_naming_df
	global city_naming_df

	print('0. Reading files')
	df = pd.read_csv(CITY_TEMPERATURE_PATH, low_memory=False)
	country_naming_df = pd.read_csv(COUNTRY_NAMING_PATH, low_memory=False)
	city_naming_df = pd.read_csv(CITY_NAMING_PATH, low_memory=False)

	print('1. Renaming')
	rename_data()

	print('2. Removing rows with wrong temperatures (= -99)')
	df = df[df.AvgTemperature != -99.0]

	print('3. Fahrenheit to Celsius')
	df['AvgTemperature'] = df['AvgTemperature'].apply(lambda x: float(round((x - 32) * 5 / 9, 2)))

	print('4. Removing incomplete months')
	remove_incomplete_months()

	print('5. Saving to file: ' + CITY_TEMPERATURE_CLEAN_PATH)
	df.to_csv(CITY_TEMPERATURE_CLEAN_PATH, index=False)


def rename_data():
	global df
	global country_naming_df
	global city_naming_df
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
	df['State'] = df['State'].fillna('-')


def remove_incomplete_months():
	global df
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

import os
import pandas as pd

dirname = os.path.dirname(__file__)
CITY_TEMPERATURE_CLEAN_PATH = os.path.join(dirname, '../res/clean/city_temperature_clean.csv')
CITY_TEMPERATURE_GROUP_BY_MONTH_PATH = os.path.join(dirname, '../res/group/city_temperature_by_month.csv')
CITY_TEMPERATURE_GROUP_BY_YEAR_PATH = os.path.join(dirname, '../res/group/city_temperature_by_year.csv')
CITY_TEMPERATURE_GROUP_ARGENTINA_BY_MONTH_PATH = os.path.join(dirname, '../res/group/argentina_temperature_by_month.csv')
CITY_TEMPERATURE_GROUP_ARGENTINA_BY_YEAR_PATH = os.path.join(dirname, '../res/group/argentina_temperature_by_year.csv')


def group_data():
	print('1. Grouping countries data by month')
	group_countries_by_month()
	print('2. Grouping countries data by year')
	group_countries_by_year()
	print('3. Grouping Argentina data by month')
	group_argentina_by_month()
	print('4. Grouping Argentina data by month')
	group_argentina_by_year()


def group_countries_by_month():
	df = pd.read_csv(CITY_TEMPERATURE_CLEAN_PATH, low_memory=False)
	df = df.groupby(['Month', 'Year', 'Country', 'City']) \
		.agg({'AvgTemperature': 'mean'}) \
		.rename(columns={'AvgTemperature': 'MonthAvgTemperature'}) \
		.reset_index()
	print('Saving to file: ' + CITY_TEMPERATURE_GROUP_BY_MONTH_PATH)
	df.to_csv(CITY_TEMPERATURE_GROUP_BY_MONTH_PATH, index=False)


def group_countries_by_year():
	df = pd.read_csv(CITY_TEMPERATURE_GROUP_BY_MONTH_PATH, low_memory=False)
	df = df.groupby(['Year', 'Country', 'City']) \
		.agg({'MonthAvgTemperature': 'mean'}) \
		.rename(columns={'MonthAvgTemperature': 'YearAvgTemperature'}) \
		.reset_index()
	print('Saving to file: ' + CITY_TEMPERATURE_GROUP_BY_YEAR_PATH)
	df.to_csv(CITY_TEMPERATURE_GROUP_BY_YEAR_PATH, index=False)


def group_argentina_by_month():
	df = pd.read_csv(CITY_TEMPERATURE_GROUP_BY_MONTH_PATH, low_memory=False)
	is_argentina = df['Country'] == 'Argentina'
	df = df[is_argentina]
	print('Saving to file: ' + CITY_TEMPERATURE_GROUP_ARGENTINA_BY_MONTH_PATH)
	df.to_csv(CITY_TEMPERATURE_GROUP_ARGENTINA_BY_MONTH_PATH, index=False)


def group_argentina_by_year():
	df = pd.read_csv(CITY_TEMPERATURE_GROUP_BY_YEAR_PATH, low_memory=False)
	is_argentina = df['Country'] == 'Argentina'
	df = df[is_argentina]
	print('Saving to file: ' + CITY_TEMPERATURE_GROUP_ARGENTINA_BY_YEAR_PATH)
	df.to_csv(CITY_TEMPERATURE_GROUP_ARGENTINA_BY_YEAR_PATH, index=False)





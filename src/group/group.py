import pandas as pd
import src.constants as c


def group_data():
	print('1. Grouping countries data by month')
	group_countries_by_month()
	print('2. Grouping countries data by year')
	group_countries_by_year()
	print('3. Grouping Argentina data by month')
	group_argentina_by_month()
	print('4. Grouping Argentina data by month')
	group_argentina_by_year()
	print('5. Counting quantity of countries per continent')
	count_continents()
	print('6. Grouping data by continent by day')
	group_by_continent_by_day()
	print('7. Grouping data by continent by month')
	group_by_continent_by_month()
	print('8. Grouping data by continent by year')
	group_by_continent_by_year()


def group_countries_by_month():
	df = pd.read_csv(c.CITY_TEMPERATURE_CLEAN_PATH, low_memory=False)
	df = df.groupby(['Month', 'Year', 'Region', 'Country', 'City']) \
		.agg({'AvgTemperature': 'mean'}) \
		.round(2) \
		.rename(columns={'AvgTemperature': 'MonthAvgTemperature'}) \
		.reset_index()
	print('Saving to file: ' + c.CITY_TEMPERATURE_GROUP_BY_MONTH_PATH)
	df.to_csv(c.CITY_TEMPERATURE_GROUP_BY_MONTH_PATH, index=False)


def group_countries_by_year():
	df = pd.read_csv(c.CITY_TEMPERATURE_GROUP_BY_MONTH_PATH, low_memory=False)
	df = df.groupby(['Year', 'Region', 'Country', 'City']) \
		.agg({'MonthAvgTemperature': 'mean'}) \
		.round(2) \
		.rename(columns={'MonthAvgTemperature': 'YearAvgTemperature'}) \
		.reset_index()
	print('Saving to file: ' + c.CITY_TEMPERATURE_GROUP_BY_YEAR_PATH)
	df.to_csv(c.CITY_TEMPERATURE_GROUP_BY_YEAR_PATH, index=False)


def group_argentina_by_month():
	df = pd.read_csv(c.CITY_TEMPERATURE_GROUP_BY_MONTH_PATH, low_memory=False)
	is_argentina = df['Country'] == 'Argentina'
	df = df[is_argentina]
	print('Saving to file: ' + c.GROUP_ARGENTINA_BY_MONTH_PATH)
	df.to_csv(c.GROUP_ARGENTINA_BY_MONTH_PATH, index=False)


def group_argentina_by_year():
	df = pd.read_csv(c.CITY_TEMPERATURE_GROUP_BY_YEAR_PATH, low_memory=False)
	is_argentina = df['Country'] == 'Argentina'
	df = df[is_argentina]
	print('Saving to file: ' + c.GROUP_ARGENTINA_BY_YEAR_PATH)
	df.to_csv(c.GROUP_ARGENTINA_BY_YEAR_PATH, index=False)


def count_continents():
	df = pd.read_csv(c.CITY_TEMPERATURE_CLEAN_PATH, low_memory=False)
	df = pd.DataFrame({'Percentage': df.groupby('Region').size() / len(df) * 100}) \
		.reset_index() \
		.rename(columns={"Index": "Percent"})
	print('Saving to file: ' + c.GROUP_ARGENTINA_BY_YEAR_PATH)
	df.to_csv(c.COUNTRIES_PERCENTAGE_GROUP_PATH, index=False)


def group_by_continent_by_day():
	filter_by_continent_by_day('África', c.GROUP_AFRICA_BY_DAY_PATH)
	filter_by_continent_by_day('Asia', c.GROUP_ASIA_BY_DAY_PATH)
	filter_by_continent_by_day('Oceanía', c.GROUP_OCEANIA_BY_DAY_PATH)
	filter_by_continent_by_day('Europa', c.GROUP_EUROPA_BY_DAY_PATH)
	filter_by_continent_by_day('América del Sur', c.GROUP_SOUTH_AMERICA_BY_DAY_PATH)
	filter_by_continent_by_day('América Central y el Caribe', c.GROUP_CENTRAL_AMERICA_BY_DAY_PATH)
	filter_by_continent_by_day('América del Norte', c.GROUP_NORTH_AMERICA_BY_DAY_PATH)


def group_by_continent_by_month():
	filter_by_continent_by_month('África', c.GROUP_AFRICA_BY_MONTH_PATH)
	filter_by_continent_by_month('Asia', c.GROUP_ASIA_BY_MONTH_PATH)
	filter_by_continent_by_month('Oceanía', c.GROUP_OCEANIA_BY_MONTH_PATH)
	filter_by_continent_by_month('Europa', c.GROUP_EUROPA_BY_MONTH_PATH)
	filter_by_continent_by_month('América del Sur', c.GROUP_SOUTH_AMERICA_BY_MONTH_PATH)
	filter_by_continent_by_month('América Central y el Caribe', c.GROUP_CENTRAL_AMERICA_BY_MONTH_PATH)
	filter_by_continent_by_month('América del Norte', c.GROUP_NORTH_AMERICA_BY_MONTH_PATH)


def group_by_continent_by_year():
	filter_by_continent_by_year('África', c.GROUP_AFRICA_BY_YEAR_PATH)
	filter_by_continent_by_year('Asia', c.GROUP_ASIA_BY_YEAR_PATH)
	filter_by_continent_by_year('Oceanía', c.GROUP_OCEANIA_BY_YEAR_PATH)
	filter_by_continent_by_year('Europa', c.GROUP_EUROPA_BY_YEAR_PATH)
	filter_by_continent_by_year('América del Sur', c.GROUP_SOUTH_AMERICA_BY_YEAR_PATH)
	filter_by_continent_by_year('América Central y el Caribe', c.GROUP_CENTRAL_AMERICA_BY_YEAR_PATH)
	filter_by_continent_by_year('América del Norte', c.GROUP_NORTH_AMERICA_BY_YEAR_PATH)


def filter_by_continent_by_day(continent, path):
	df = pd.read_csv(c.CITY_TEMPERATURE_CLEAN_PATH, low_memory=False)
	df = df[df['Region'] == continent]
	df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
	df = df.sort_values(['Year', 'Month', 'Day'])
	print('Saving to file: ' + path)
	df.to_csv(path, index=False)


def filter_by_continent_by_month(continent, path):
	df = pd.read_csv(c.CITY_TEMPERATURE_GROUP_BY_MONTH_PATH, low_memory=False)
	df = df[df['Region'] == continent]
	df['Date'] = df['Year'].astype(str) + '-' + df['Month'].astype(str)
	df = df.sort_values(by='Date')
	print('Saving to file: ' + path)
	df.to_csv(path, index=False)


def filter_by_continent_by_year(continent, path):
	df = pd.read_csv(c.CITY_TEMPERATURE_GROUP_BY_YEAR_PATH, low_memory=False)
	df = df[df['Region'] == continent]
	print('Saving to file: ' + path)
	df.to_csv(path, index=False)

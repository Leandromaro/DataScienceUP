import pandas as pd


def getCSVByMonth():
    df = pd.read_csv("../res/city_temperature_clean.csv", low_memory=False)
    df = df.groupby(['Region', 'Country', 'City', 'Month', 'Year']) \
        .agg({'AvgTemperature': 'mean'}) \
        .rename(columns={'AvgTemperature': 'MonthAvgTemperature'}) \
        .reset_index()
    df.to_csv("../res/city_temperatureByMonth.csv", index=False)


def getCSVByYear():
    df = pd.read_csv("../res/city_temperatureByMonth.csv", low_memory=False)
    df = df.groupby(['Region', 'Country', 'City', 'Month', 'Year']) \
        .agg({'MonthAvgTemperature': 'mean'}) \
        .rename(columns={'MonthAvgTemperature': 'YearAvgTemperature'}) \
        .reset_index()
    df.to_csv("../res/city_temperatureByYear.csv", index=False)


getCSVByMonth()
getCSVByYear()

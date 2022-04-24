import pandas as pd


def getCSVByMonth():
    df = pd.read_csv("../res/city_temperature_clean.csv", low_memory=False)
    df = df.groupby(['Month', 'Year', 'Country', 'City']) \
        .agg({'AvgTemperature': 'mean'}) \
        .rename(columns={'AvgTemperature': 'MonthAvgTemperature'}) \
        .reset_index()
    df.to_csv("../res/city_temperatureByMonth.csv", index=False)
    print(df)


def getCSVByYear():
    df = pd.read_csv("../res/city_temperatureByMonth.csv", low_memory=False)
    df = df.groupby(['Year', 'Country', 'City']) \
        .agg({'MonthAvgTemperature': 'mean'}) \
        .rename(columns={'MonthAvgTemperature': 'YearAvgTemperature'}) \
        .reset_index()
    df.to_csv("../res/city_temperatureByYear.csv", index=False)


def getArgentinaCSVByYear():
    df = pd.read_csv("../res/city_temperatureByYear.csv", low_memory=False)
    is_argentina = df['Country'] == 'Argentina'
    df = df[is_argentina]
    df.to_csv("../res/argentina_temperatureByYear.csv", index=False)


def getArgentinaCSVByMonth():
    df = pd.read_csv("../res/city_temperatureByMonth.csv", low_memory=False)
    is_argentina = df['Country'] == 'Argentina'
    df = df[is_argentina]
    df.to_csv("../res/argentina_temperatureByMonth.csv", index=False)


getCSVByMonth()
getCSVByYear()
getArgentinaCSVByMonth()
getArgentinaCSVByYear()
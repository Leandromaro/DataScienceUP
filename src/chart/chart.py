import matplotlib.pyplot as plt
import os

import numpy as np
import pandas as pd

dirname = os.path.dirname(__file__)
COUNTRIES_PERCENTAGE_GROUP_PATH = os.path.join(dirname, '../res/group/countries_percentage.csv')
CITY_TEMPERATURE_GROUP_ARGENTINA_BY_YEAR_PATH = os.path.join(dirname, '../res/group/argentina_temperature_by_year.csv')


def pie_chart():
    df = pd.read_csv(COUNTRIES_PERCENTAGE_GROUP_PATH, low_memory=False)
    labels = df.Region
    sizes = df.Percentage
    explode = (0, 0, 0, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.savefig('countries_cake.png')
    plt.show()


def pie_plot():
    df = pd.read_csv(CITY_TEMPERATURE_GROUP_ARGENTINA_BY_YEAR_PATH, low_memory=False)
    x = df.Year

    y = df.YearAvgTemperature

    fig = plt.figure(figsize=(12, 6))
    plt.xlabel("Years")
    plt.ylabel("Temperature Average")
    ax = fig.add_subplot(111)
    ax.bar(np.arange(len(x)), y)
    ax.set_xticks(np.arange(len(x)))
    ax.set_xticklabels(x, rotation=15, zorder=100)

    plt.savefig('argentina_plot.png')
    plt.show()

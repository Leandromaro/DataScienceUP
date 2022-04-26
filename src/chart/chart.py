import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dirname = os.path.dirname(__file__)
COUNTRIES_PERCENTAGE_GROUP_PATH = os.path.join(dirname, '../res/group/countries_percentage.csv')
CITY_TEMPERATURE_GROUP_ARGENTINA_BY_YEAR_PATH = os.path.join(dirname, '../res/group/argentina_temperature_by_year.csv')

COUNTRIES_PIE_CHART = os.path.join(dirname, '../img/countries_pie_chart.png')
ARGENTINA_BOX_PLOT = os.path.join(dirname, '../img/argentina_box_plot.png')
ARGENTINA_LINE_PLOT = os.path.join(dirname, '../img/argentina_line_plot.png')


def create_charts():
	pie_chart()
	bar_plot()
	argentina_line_plot()


def pie_chart():
	df = pd.read_csv(COUNTRIES_PERCENTAGE_GROUP_PATH, low_memory=False)
	labels = df.Region
	sizes = df.Percentage
	explode = (0, 0, 0, 0, 0, 0, 0)
	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
	ax1.axis('equal')

	plt.savefig(COUNTRIES_PIE_CHART)
	plt.show()


def bar_plot():
	df = pd.read_csv(CITY_TEMPERATURE_GROUP_ARGENTINA_BY_YEAR_PATH, low_memory=False)
	x = df.Year
	y = df.YearAvgTemperature

	plt.bar(x, y)
	plt.xlabel("Años")
	plt.ylabel("Temperatura Promedio")
	plt.title("Temperatura promedio por año en Argentina")

	plt.savefig(ARGENTINA_BOX_PLOT)
	plt.show()


def argentina_line_plot():
	df = pd.read_csv(CITY_TEMPERATURE_GROUP_ARGENTINA_BY_YEAR_PATH, low_memory=False)
	x1 = df.Year
	y1 = df.YearAvgTemperature

	plt.plot(x1, y1)
	plt.xlabel('Año')
	plt.ylabel('Temperatura Promedio')
	plt.title('Temperatura promedio por año en Argentina')

	plt.savefig(ARGENTINA_LINE_PLOT)
	plt.show()

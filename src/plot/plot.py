import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import src.constants as c

def create_plots():
	continents_pie_chart()
	argentina_bar_plot()
	argentina_line_plot()
	plot_continents()


def continents_pie_chart():
	df = pd.read_csv(c.COUNTRIES_PERCENTAGE_GROUP_PATH, low_memory=False)
	labels = df.Region
	sizes = df.Percentage
	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
	ax1.axis('equal')

	plt.savefig(c.COUNTRIES_PIE_CHART)
	plt.show()


def plot_continents():
	africa_scatter_plot()
	oceania_line_plot()
	south_america_multi_scatter()


def africa_scatter_plot():
	df = pd.read_csv(c.GROUP_AFRICA_BY_DAY_PATH, low_memory=False)

	plt.figure(figsize=(14, 8))
	g = sns.scatterplot(data=df, x='Date', y='AvgTemperature', hue='Country')

	plt.xlabel('Fecha')
	plt.ylabel('Temperatura Promedio')
	plt.title('Temperaturas de África')
	box = g.get_position()
	g.set_position([box.x0, box.y0, box.width * 0.85, box.height])
	g.legend(loc='center right', bbox_to_anchor=(1.28, 0.5), ncol=1)

	plt.savefig(c.AFRICA_SCATTER_PLOT_BY_DAY)
	plt.show()


def oceania_line_plot():
	df = pd.read_csv(c.GROUP_OCEANIA_BY_MONTH_PATH, low_memory=False)

	plt.figure(figsize=(14, 6))
	g = sns.lineplot(data=df, x='Date', y='MonthAvgTemperature', hue='Country')

	ticks = list(df['Date'])
	plt.xticks([ticks[i] for i in range(len(ticks)) if i % 30 == 0], rotation='vertical')
	plt.xlabel('Fecha')
	plt.ylabel('Temperatura Promedio')
	plt.title('Temperaturas de Oceanía')
	box = g.get_position()
	g.set_position([box.x0, box.y0, box.width * 0.85, box.height])
	g.legend(loc='center right', bbox_to_anchor=(1.28, 0.5), ncol=1)

	plt.savefig(c.OCEANIA_LINE_PLOT_BY_MONTH)
	plt.show()


def south_america_multi_scatter():
	df = pd.read_csv(c.GROUP_SOUTH_AMERICA_BY_MONTH_PATH, low_memory=False)

	plt.figure(figsize=(14, 10))
	grid = sns.FacetGrid(df, col="Country", hue="Country", col_wrap=5, height=4, aspect=1.25)
	grid.map(sns.scatterplot, "Year", "MonthAvgTemperature")
	grid.add_legend()

	grid.set_titles("{col_name}")
	grid.set_xticklabels(rotation=90)
	grid.set_xlabels('Fecha')
	grid.set_ylabels('Temperatura Promedio')

	plt.savefig(c.SOUTH_AMERICA_MULTI_SCATTER_PLOT_BY_MONTH)
	plt.show()


def argentina_bar_plot():
	df = pd.read_csv(c.GROUP_ARGENTINA_BY_YEAR_PATH, low_memory=False)
	x = df.Year
	y = df.YearAvgTemperature

	plt.bar(x, y)
	plt.xlabel('Años')
	plt.ylabel('Temperatura Promedio')
	plt.title('Temperatura promedio por año en Argentina')

	plt.savefig(c.ARGENTINA_BOX_PLOT)
	plt.show()


def argentina_line_plot():
	df = pd.read_csv(c.GROUP_ARGENTINA_BY_YEAR_PATH, low_memory=False)
	x1 = df.Year
	y1 = df.YearAvgTemperature

	plt.plot(x1, y1)
	plt.xlabel('Año')
	plt.ylabel('Temperatura Promedio')
	plt.title('Temperatura promedio por año en Argentina')

	plt.savefig(c.ARGENTINA_LINE_PLOT)
	plt.show()


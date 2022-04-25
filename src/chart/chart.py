import matplotlib.pyplot as plt


def pie_chart():
	# Pie chart, where the slices will be ordered and plotted counter-clockwise:
	labels = 'África', 'Asia', 'Europa', 'Oceania', 'América del Sur', 'América del Norte', 'América Central y el Caribe'
	sizes = [15, 30, 45, 10, 1, 1, 1]
	explode = (0, 0.1, 0, 0, 0, 0, 0)

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

	plt.show()

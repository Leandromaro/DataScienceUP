from timeit import default_timer as timer
from clean import clean_data
from group import group_data
from plot import create_plots

if __name__ == '__main__':
	start = timer()
	print('--- Cleaning Data ---')
	clean_data()
	end_clean_data = timer()
	first = end_clean_data - start
	print('Took: ' + str(first) + ' seconds')

	print('-- Grouping Data ---')
	group_data()
	end_group_data = timer()
	second = end_group_data - end_clean_data
	print('Took: ' + str(second) + ' seconds')

	print('-- Creating Plots ---')
	create_plots()
	end_create_plots = timer()
	third = end_create_plots - end_group_data
	print('Took: ' + str(third) + ' seconds')

	total = first + second + third
	print('The whole process took: ' + str(total) + ' seconds')

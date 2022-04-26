from timeit import default_timer as timer
from clean import clean_data
from group import group_data
from chart import create_charts

if __name__ == '__main__':
	start = timer()
	print("--- Cleaning Data ---")
	clean_data()
	end_clean_data = timer()
	print("Took: " + str(end_clean_data - start) + " seconds")

	print("-- Grouping Data ---")
	group_data()
	end_group_data = timer()
	print("Took: " + str(end_group_data - end_clean_data) + " seconds")

	print("-- Creating Charts ---")
	create_charts()
	end_create_charts = timer()
	print("Took: " + str(end_create_charts - end_group_data) + " seconds")


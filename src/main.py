from timeit import default_timer as timer
from clean import clean_data
from group import group_data
from chart import pie_chart

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
	pie_chart()


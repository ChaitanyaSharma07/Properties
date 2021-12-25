import csv
import plotly.figure_factory as ff
import pandas as pd
import statistics

df = pd.read_csv("performance.csv")

height_list = df["readingscore"].to_list()

#finding mean of both arrays
height_mean = statistics.mean(height_list)


#finding median for both arrays
height_median = statistics.median(height_list)


#finding mode for both arrays
height_mode = statistics.mode(height_list)


#Printing mean, median and mode to validate
print("Mean, Median and Mode of height is {}, {} and {} respectively".format(height_mean, height_median, height_mode))

#finding standard deviation for arrays
height_stddev = statistics.stdev(height_list)

#finding first second and third standard deviation
height_first_stddev_start, height_first_stddev_end = height_mean - height_stddev, height_mean + height_stddev

#finding second standard deviation
height_second_stddev_start, height_second_stddev_end = height_mean -(2 * height_stddev), height_mean + (2 * height_stddev)
#finding third standard deviation
height_third_stddev_start, height_third_stddev_end = height_mean -(3 * height_stddev), height_mean + (3 * height_stddev)
#Percentage of data within 1, 2 and 3 Standard Deviations for Height
height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_first_stddev_start and result < height_first_stddev_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_second_stddev_start and result < height_second_stddev_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_third_stddev_start and result < height_third_stddev_end]

#Printing data for height and weight (Standard Deviation)
print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))
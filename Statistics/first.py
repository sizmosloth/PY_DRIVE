# Program to demonstrate the use of statistics module in Python

import statistics
import math

# Sample data
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Data:", data)

# Mean
mean = sum(data) / len(data)
print("Mean:", mean)
print("Mean using statistics module:", statistics.mean(data))

# Median
median = statistics.median(data)
print("Median:", median)

# Mode
# Note: Mode will raise an exception if there is no unique mode
try:
    mode = statistics.mode(data)
    print("Mode:", mode)
except statistics.StatisticsError as e:
    print("Mode: No unique mode found. Error:", e)

# Variance
variance = statistics.variance(data)
print("Variance:", variance)

# Standard Deviation
std_dev = statistics.stdev(data)
print("Standard Deviation:", std_dev)

# Range
data_range = max(data) - min(data)
print("Range:", data_range)
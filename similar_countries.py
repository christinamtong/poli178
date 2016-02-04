########################
# Expected input is name of file containing data 
# in the format <string int>, where
# the string is the name of the country and
# the int is the GDP.
#
########################
import sys
import numpy as np
import scipy.stats as stats

# open input file
input = open(sys.argv[1], 'r')

print "\n================================================"
file_path = sys.argv[1].split('/')
file_name = file_path[len(file_path)-1]
print "Reading from", file_name

# put all data into dictionary
gdp = []
for line in input:
	this_line = line.split(',')
	gdp.append((float)(this_line[1].replace("\n", "")))

# clean up - close file
input.close()

# calculate statistical information
n = len(gdp)
mean = np.mean(gdp)
median = np.median(gdp)
q1 = np.percentile(gdp, 25)
q3 = np.percentile(gdp, 75)
iqr = q3-q1
lower_inner_fence = q1 - 1.5*iqr
upper_inner_fence = q3 + 1.5*iqr
lower_outer_fence = q1 - 3*iqr
upper_outer_fence = q3 + 3*iqr

# print stats info
print "\nn =", n
print "Mean", mean
print "Median", median
print "Min", min(gdp)
print "Max", max(gdp)
print "IQR of", iqr, "is from", q1, "to", q3
print "Fences for outliers:"
print "\tUpper, extreme", upper_outer_fence
print "\tUpper, mild", upper_inner_fence
print "\tLower, extreme", lower_outer_fence
print "\tLower, mild", lower_inner_fence

# Deciles
print "\nDeciles: "
print np.percentile(gdp, 10)
print np.percentile(gdp, 20)
print np.percentile(gdp, 30)
print np.percentile(gdp, 40)
print np.percentile(gdp, 50)
print np.percentile(gdp, 60)
print np.percentile(gdp, 70)
print np.percentile(gdp, 80)
print np.percentile(gdp, 90)

print "\nDecile differences: "
print np.percentile(gdp, 10) - np.percentile(gdp,0)
print np.percentile(gdp, 20) - np.percentile(gdp,10)
print np.percentile(gdp, 30) - np.percentile(gdp,20)
print np.percentile(gdp, 40) - np.percentile(gdp,30)
print np.percentile(gdp, 50) - np.percentile(gdp,40)
print np.percentile(gdp, 60) - np.percentile(gdp,50)
print np.percentile(gdp, 70) - np.percentile(gdp,60)
print np.percentile(gdp, 80) - np.percentile(gdp,70)
print np.percentile(gdp, 90) - np.percentile(gdp,80)
print np.percentile(gdp, 100) - np.percentile(gdp,90)


print "\nPercentile of Singapore:", stats.percentileofscore(gdp,427.8748221,kind='strict')

# determine if outliers exist
mild_outliers_low = []
mild_outliers_high = []
extreme_outliers_low = []
extreme_outliers_high = []
for x in gdp:
	if x < lower_outer_fence:
		extreme_outliers_low.append(x)
	elif x < lower_inner_fence:
		mild_outliers_low.append(x)
	elif x > upper_outer_fence:
		extreme_outliers_high.append(x)
	elif x > upper_inner_fence:
		mild_outliers_high.append(x)

# print outlier results
n = float(n)
print "Results for outliers:"
print "\tUpper, extreme", len(extreme_outliers_high), float(len(extreme_outliers_high))/n*100, "%"
print "\tUpper, mild", len(mild_outliers_high), float(len(mild_outliers_high))/n*100, "%"
print "\tLower, extreme", len(extreme_outliers_low), float(len(extreme_outliers_low))/n*100, "%"
print "\tLower, mild", len(mild_outliers_low), float(len(mild_outliers_low))/n*100, "%"
print "================================================\n"
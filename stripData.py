# ###############################
#
# Input: path to file in the csv format given by the world bank.
# In the .csv file, you must manually delete all the rows before 
# the country data begins (including the row with dates).
#
# Output: csv file with rows for high income OECD, high income non-OECD,
# countries with similar GDP to singapore in 1960, countries in SE or S
# Asia with similar area, population, or population density to GDP.
# Columns correspond to years 1960 to 2014.
#
# Can account for simple changes in input format (i.e. number of columns)
# by changing the "lower" and "upper" variables.
# 
# @author Christina Tong, 2/3/15
# for Political Economy of Development Paper 1 (comparative stats)
#
# ###############################
from sets import Set
import csv
import sys

# country groups
hi_OECD = Set(['Australia','Italy','Austria','Japan','Belgium',\
	'Korea, Rep.','Canada','Luxembourg','Chile','Netherlands',\
	'Czech Republic','New Zealand','Denmark','Norway','Estonia',\
	'Poland','Finland','Portugal','France','Slovak Republic',\
	'Germany','Slovenia','Greece','Spain','Hungary','Sweden',\
	'Iceland','Switzerland','Ireland','United Kingdom','Israel',\
	'United States'])

hi_nonOECD = Set(['Andorra','Lithuania','Antigua and Barbuda',\
	'Macao SAR, China','Argentina','Malta','Aruba','Monaco',\
	'Bahamas, The','New Caledonia','Bahrain','Northern Mariana Islands',\
	'Barbados','Oman','Bermuda','Puerto Rico','Brunei Darussalam',\
	'Qatar','Cayman Islands','Russian Federation','Channel Islands',\
	'San Marino','Croatia','Saudi Arabia','Curacao','Seychelles',\
	'Cyprus','Equatorial Guinea','Sint Maarten (Dutch part)',\
	'Faeroe Islands','St. Kitts and Nevis','French Polynesia',\
	'St. Martin (French part)','Greenland','Taiwan, China','Guam',\
	'Trinidad and Tobago','Hong Kong SAR, China',\
	'Turks and Caicos Islands','Isle of Man','United Arab Emirates',\
	'Kuwait','Uruguay','Latvia','Venezuela, RB','Liechtenstein',\
	'Virgin Islands (U.S.)'])

similar_gdp = Set(['Suriname','Mexico','Portugal','Panama',\
	'Costa Rica','Spain','South Africa','Jamaica',\
	'Hong Kong SAR, China'])

asian = Set(['Macao SAR, China','Maldives','Hong Kong SAR, China',\
	'Timor-Leste','Sri Lanka','Cambodia','Lao PDR'])

# read from file
fin = open(sys.argv[1], 'r')
csv_reader = csv.reader(fin)

# write subset of data
no_ending = sys.argv[1].split('.')
out_file_name = no_ending[0] + "_output.csv"
fout = open(out_file_name, 'w')
csv_writer = csv.writer(fout, dialect='excel')

# initialize for reading in data
hi_OECD_data = []
hi_nonOECD_data = []
similar_gdp_data = []
asian_data = []
singapore = []
hong_kong = []
hi_OECD_count = 0
hi_nonOECD_count = 0
similar_gdp_count = 0
asian_count = 0

# read in data, remembering only info about countries in the relevant categories
for line in csv_reader:
	if line[0] in hi_OECD:
		hi_OECD_data.append(line)
		hi_OECD_count = hi_OECD_count + 1
	if line[0] in hi_nonOECD:
		hi_nonOECD_data.append(line)
		hi_nonOECD_count = hi_nonOECD_count + 1
	if line[0] in similar_gdp:
		similar_gdp_data.append(line)
		similar_gdp_count = similar_gdp_count + 1
	if line[0] in asian:
		asian_data.append(line)
		asian_count = asian_count + 1
	if line[0] == 'Hong Kong SAR, China':
		hong_kong = line
	if line[0] == 'Singapore':
		singapore = line

# # print out data for individual countries
# for c in hi_OECD_data:
# 	csv_writer.writerow(c)
# csv_writer.writerow([])
# for c in hi_nonOECD_data:
# 	csv_writer.writerow(c)
# csv_writer.writerow([])
# for c in similar_gdp_data:
# 	csv_writer.writerow(c)
# csv_writer.writerow([])
# for c in asian_data:
# 	csv_writer.writerow(c)

# the columns in which the data resides
lower = 4
upper = 60

# calculate and write averages for each country category
hi_OECD_avg = ['High-income OECD']
for x in range(lower,upper):
	count = 0
	the_sum = 0
	for country in hi_OECD_data:
		if country[x] != "":
			the_sum = the_sum + float(country[x])
			count = count + 1
	if count > 0:
		avg = str(the_sum / count)
	else:
		avg = ""
	hi_OECD_avg.append(avg)

hi_nonOECD_avg = ['High-income nonOECD']
for x in range(lower,upper):
	count = 0
	the_sum = 0
	for country in hi_nonOECD_data:
		if country[x] != "":
			the_sum = the_sum + float(country[x])
			count = count + 1
	if count > 0:
		avg = str(the_sum / count)
	else:
		avg = ""
	hi_nonOECD_avg.append(avg)

similar_gdp_avg = ['Baseline peers']
for x in range(lower,upper):
	count = 0
	the_sum = 0
	for country in similar_gdp_data:
		if country[x] != "":
			the_sum = the_sum + float(country[x])
			count = count + 1
	if count > 0:
		avg = str(the_sum / count)
	else:
		avg = ""
	similar_gdp_avg.append(avg)


asian_avg = ['Similar Asian']
for x in range(lower,upper):
	count = 0
	the_sum = 0
	for country in asian_data:
		if country[x] != "":
			the_sum = the_sum + float(country[x])
			count = count + 1
	if count > 0:
		avg = str(the_sum / count)
	else:
		avg = ""
	asian_avg.append(avg)

# remove useless strings from hong kong and singapore data
for x in range (1,4):
	del hong_kong[1]
	del singapore[1]

# print date strip 1960 to 2014
dates = ['']
for d in range(1960,2015):
	dates.append(d)


# write data to file
csv_writer.writerow(dates)
csv_writer.writerow(hi_OECD_avg)
csv_writer.writerow(hi_nonOECD_avg)
csv_writer.writerow(similar_gdp_avg)
csv_writer.writerow(asian_avg)
csv_writer.writerow(hong_kong)
csv_writer.writerow(singapore)

# clean up
fin.close()
fout.close()

# print summative information to console
print hi_OECD_avg
print hi_nonOECD_avg
print similar_gdp_avg
print asian_avg
print hong_kong
print singapore
print "Found", hi_OECD_count, "of", len(hi_OECD), "hi oecd"
print "Found", hi_nonOECD_count, "of", len(hi_nonOECD), "hi non-oecd"
print "Found", similar_gdp_count, "of", len(similar_gdp), "similar gdp"
print "Found", asian_count, "of", len(asian), "asian"
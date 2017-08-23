# read the data
# separate the data to 2015 data (df2015) and 2005-2014(df), this can be done by testing the year part of the date, (boolean masking course 1 week2)
# remove all records from df where day=29 and month=02
# group df by month-day and find the min/max for each group(course 1 week3) (df_r)
# group df2015 by month-day and find max/min for each group (df_r2015)
# compare the maximum temperatures from df_r with the max from df_r2015, find the days/temperatures when df_r2015['max'] is higher than df_r['max']
# repeat step 6 for minimum temperatures; find the days/temperatures when df_r2015['min'] is less than df_r['min']
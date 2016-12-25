import pandas as pd
import 

# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..

#table_dataframe= pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')[0]

data = pd.read_excel('C:\\Users\\leali\\Documents\\GitHub\\DAT210x\\Module2\\Datasets\\basketDATASET.xlsx')


# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..

data.columns = ['RK','PLAYER','TEAM','GP','G','A','PTS','+/-','PIM','PTS/G','SOG','PCT','GWG','G','A','G','A']


# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..

data = data.dropna(axis=0, thresh=4)


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..


# TODO: Get rid of the 'RK' column
#
# .. your code here ..

del data['RK']

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..

data = data.reset_index(drop=True)

# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric

data.dtypes

# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.

len(data)

len(data['PCT'].unique())

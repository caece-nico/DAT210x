import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..

data = pd.read_csv('C:\\Users\\leali\\Documents\\GitHub\\DAT210x\\Module2\\Datasets\\servo.data', sep = ',')
data.columns = ['motor', 'screw', 'pgain', 'vgain', 'class']

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..

data.s = data[data.vgain == 5]
len(data.s)


# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..

data.e = data[(data.motor == "E") & (data.screw == "E")]
len(data.e)

# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..

data.p = data[data.pgain == 4]
data.p.vgain.mean()

# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!


data.dtypes

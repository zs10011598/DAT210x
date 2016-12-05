import pandas as pd

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
df = pd.read_csv('Datasets/servo.data', header=None)

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
sli1 = df[df[3]==5]
print len(sli1) 


# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
sli2 = df[(df[0]=='E') & (df[1]=='E')]
print len(sli2)



# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
sli3 = df[df[2] == 4]
print sli3[3].mean()



# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
print df.dtypes



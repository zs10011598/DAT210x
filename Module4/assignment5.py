import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
samples = []
#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 
from scipy import misc
for i in range(71):
	img = misc.imread('Datasets/ALOI/32/32_r'+str(i*5)+'.png')
	img = img[::2, ::2]
	X = (img).reshape(-1)
	samples = samples + [X]
#print(samples)

#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 
for i in range(12):
	img = misc.imread('Datasets/ALOI/32i/32_i'+str(110+i*10)+'.png')
	img = img[::2, ::2]
	X = (img).reshape(-1)
	samples = samples + [X]

#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 
df = pd.DataFrame(samples)
#print(df)

#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 
from sklearn import manifold
iso = manifold.Isomap(n_neighbors=6, n_components = 3)
iso.fit(df)
T = iso.transform(df)

colors = ['b' for i in range(71)]
for i in range(12):
	colors = colors + ['r']
#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 
import matplotlib
matplotlib.style.use('ggplot')
G = [[T[i][0], T[i][1]] for i in range(82)]
dfG = pd.DataFrame(G)
dfG.plot.scatter(x=0 , y = 1, c =colors)

#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
H = [[T[i][0], T[i][1], T[i][2] ] for i in range(82)]
dfH = pd.DataFrame(H)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('1')
ax.set_ylabel('2')
ax.set_zlabel('3')

ax.scatter(dfH.iloc[:, 0], dfH.iloc[:, 1], dfH.iloc[:, 2], c = colors, marker='o')

plt.show()


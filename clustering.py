""" 
Copyright (C) 2015  Nicola Dileo
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>


Module: clustering.py
--------
"""

from sklearn.cluster import KMeans
from PIL import Image
from pylab import uint8
from sys import argv
from time import clock
import random
import numpy as np

class ImageData:
	def loadfile(self,filename):
		img = Image.open(filename)
		data = np.array(img)
		self.shape = data.shape
		height,width,r = data.shape
		self.data = np.zeros((height*width,r))
		for i in range(0,height):
			for j in range(0,width):
				index = i*width+j
				self.data[index] = data[i,j]

	def savetofile(self,filename):
		deflatted = np.array(self.data)
		deflatted.shape = self.shape
		img = Image.fromarray(uint8(deflatted))
		img.save(filename)


def clusterize(imagedata,n_clust):
	km = KMeans(n_clusters = n_clust,init='random',n_init=1,verbose=1)
	km.fit(imagedata.data)
	size = imagedata.shape[0]*imagedata.shape[1]
	for i in range(size):
		clust_ind = km.labels_[i]                   #recover cluster index for i-th pixel
		clust_val = km.cluster_centers_[clust_ind]  #recover cluster value
		imagedata.data[i] = clust_val               #assign cluster value to i-th pixel
	return imagedata


if __name__ == '__main__':
	img = ImageData()
	print('='*48)
	print('Loading image')	
	img.loadfile(argv[1])
	print('Starting KMeans with k=%d'%(int(argv[2])))
	tic = clock()
	clust = clusterize(img,int(argv[2]))
	toc = clock()
	print('Elapsed time %.4f sec'%(toc-tic))
	print('Saving clustered image')
	clust.savetofile("cluster_%d_%s"%(int(argv[2]),argv[1]))
	print('='*48)

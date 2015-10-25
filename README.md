# IS-A #
Image Segmentation Algorithm using clustering

## Summary ##
This script compute image segmentation using KMeans algorithm for clustering: once a cluster of pixels is computed,
each pixel in cluster receives the color belonging to the centroid.
To run the script type on terminal: "python clustering.py <imagename> number_of_cluster"

## System Requirements ##
This script require:
* Python 2.7.9;
* NumPy library;
* Matplotlib library;
* PIL Image library for Python;
* Scikit-learn library for Machine Learning in Python.

## Demo ##
The first image is the original one while the remaining are obtained by running the KMeans with k equal to 2,4,8 respectively
<a href="url"><img src="https://github.com/nicoladileo/IS-A/blob/master/fruit.jpg" align="center" 
height="250" width="500" ></a>
<a href="url"><img src="https://github.com/nicoladileo/IS-A/blob/master/cluster_2_fruit.jpg" align="center" 
height="250" width="500" ></a>
<a href="url"><img src="https://github.com/nicoladileo/IS-A/blob/master/cluster_4_fruit.jpg" align="center" 
height="250" width="500" ></a>
<a href="url"><img src="https://github.com/nicoladileo/IS-A/blob/master/cluster_8_fruit.jpg" align="center" 
height="250" width="500" ></a>



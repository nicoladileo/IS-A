# IS-A #
Image Segmentation Algorithm using clustering

## Summary ##
This script compute image segmentation using KMeans algorithm for clustering: once a cluster of pixels is computed,
each pixel in cluster receives the color belonging to the centroid.
To run the script type on terminal: 

* python clustering.py \<imagepath\> \<number of cluster\>

## System Requirements ##
This script require:
* Python 2.7.9;
* NumPy library;
* Matplotlib library;
* PIL Image library for Python;
* Scikit-learn library for Machine Learning in Python.

## Demo ##
<div>
    <img src="https://github.com/nicoladileo/IS-A/blob/master/fruit.jpg" align="center" height="350" width="500">
    <p>Original image</p>
</div>

<div>
    <img src="https://github.com/nicoladileo/IS-A/blob/master/cluster_2_fruit.jpg" align="center" height="350" width="500">
    <p>Final image after running KMeans with k = 2</p>
</div>

<div>
    <img src="https://github.com/nicoladileo/IS-A/blob/master/cluster_4_fruit.jpg" align="center" height="350" width="500">
    <p>Final image after running KMeans with k = 4</p>
</div>



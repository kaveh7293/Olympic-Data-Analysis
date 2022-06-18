# Olympic-Data-Analysis
* In this exmple, I tried to analysis the data of different olympic games using python. This data analysis contains information regarding the number of medals that teams obtained during all the previous olympics. I added the average temeprature of differnet countries and their GDP to realize whether there is any pattern between the olympic success and these additional features.

* The data were collected using BeautifulSoup library in python from wikipedia website. The data for number of medals for different countries, the GDP and average temperature were collected separately and then concatenated to obtain a pandas data from. 

* In the first step, I did some visualization to obtain some of the questions that I had about olympic game results stats. In the first graph, I plotted the number of gold medals for both of summer and winter olympic games and the total number of medals (i.e., gold, silver and bronze) during all the olympic games for both of summer and winter olympic games. As shown, the data were only visualized for the best 10 countries in both of summer and winter olympics.  

![](https://github.com/kaveh7293/Olympic-Data-Analysis/blob/main/Summer.png)
![](https://github.com/kaveh7293/Olympic-Data-Analysis/blob/main/Winter.png)

# Cluster Analysis

* In the current data set, I am curious about the relationship between features, and the features which affect the clusters into which countries belong. I used a k-means clustering algorithm. 
* Prior to every step, I did some data cleaning using regular expression in python. Also, I tried to investigate whether there is any missing values so that I can whether remove or find the values which can be used instead of missing values. For example, since Soviet Union does not exist anymore, its corresponding GDP and average weather temperature do not exsit. So, I lumped together the information for Soviet Union and Russia. There was the same problem for Eastern Germany and Western Germany which does not exist anymore. Likewise, I lumped their medal information with the Germany. Further, I did a standard transformation so that all the features have the same variances and the same orders of magnitude.
## Determine the number of clusters
* I used the elbow point of wcss vs. the number of clusters plot to determine the number of clusters in the final clustering model. Based on the figure shown below, betwee seven to eight clusters must be suffiecient to explain most of the variations exists in the data. I continued my clustering with seven clusters.

![](https://github.com/kaveh7293/Olympic-Data-Analysis/blob/main/Cluster_determination.png)

## Principal Component Analysis for Visualization
* With the first two and the first three principle components 85% and 92% of variations in the data can be explained. In the following, the projection of the data on the first and the second proincipal components and the first and the third principal components are shown. Different colors are used to demonstrate data points belong to different clusters.

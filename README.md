# Olympic-Data-Analysis
* In this exmple, I tried to analysis the data of different olympic games using python. This data analysis contains information regarding the number of medals that teams obtained during all the previous olympics. I added the average temeprature of differnet countries and their GDP to realize whether there is any pattern between the olympic success and these additional features. The python code for all of the following data extraction, data cleaning and cluster analysis can be found <a href='https://github.com/kaveh7293/Olympic-Data-Analysis/blob/main/Olympic_Data_Analysis.ipynb'> here</a>.

* The data were collected using BeautifulSoup library in python from wikipedia website. The data for number of medals for different countries, the GDP and average temperature were collected separately and then concatenated to obtain a pandas data from. 

* In the first step, I did some visualization to obtain some of the questions that I had about olympic game results stats. In the first graph, I plotted the number of gold medals for both of summer and winter olympic games and the total number of medals (i.e., gold, silver and bronze) during all the olympic games for both of summer and winter olympic games. As shown, the data were only visualized for the best 10 countries in both of summer and winter olympics.  

![](https://github.com/kaveh7293/Olympic-Data-Analysis/blob/main/Summer.png)
![](https://github.com/kaveh7293/Olympic-Data-Analysis/blob/main/Winter.png)
<h2> Feature Analysis </h2>
<p> In this section, we analyse the relationship between different features using visualization. The first plot shows the relationship between the total number of winter and summer medals vs the countries GDP. As shown the correlation between summer medals and GDP is larger compared to the winter medals and GDP

<img src='https://github.com/kaveh7293/Olympic-Data-Analysis/blob/main/Picture3.png' width='700' height='300'><br>


Similar plots can be obtained for relationship between total medals and the average temeprature. As shown, the average temperature is negetively correlated with the performance of the countries which does make sense for winter olympics.<br>

<img src='https://github.com/kaveh7293/Olympic-Data-Analysis/blob/main/Picture2.png' width='700' height='300'><br>


The relationship between the four features (i.e., the total number of medals in winter, the total number of medals in summer, temperature, and GDP) can be seen also from the following heat map which is in agreement with the scatter plots above: <br>

<img src='https://github.com/kaveh7293/Olympic-Data-Analysis/blob/main/heatMap.png' width='600' height='500'>

<h2> Principal Component Analysis and Clustering </h2><br>
<p> The following steps were used for dimension reduction and cluster analysis </p>
<ol>
<li>Prior to every step, I did some data cleaning using regular expression in python. Also, I tried to investigate whether there is any missing values so that I can whether remove or find the values which can be used instead of missing values. For example, since Soviet Union does not exist anymore, its corresponding GDP and average weather temperature do not exsit. So, I lumped together the information for Soviet Union and Russia. There was the same problem for Eastern Germany and Western Germany which does not exist anymore. Likewise, I lumped their medal information with the Germany. Further, I did a standard transformation so that all the features have the same variances and the same orders of magnitude.</li>

<li> I transformed the data using two principal components. The first two principal components were able to explain 85% of variations in the data. 
In the following, the projection of the data on to the first and the second proincipal components are shown. </li>

<li> I used a k-means clustering algorithm to do clustering for the data projected onto the first two principal components. Based on the plot of within-cluster-sum-of-squares (wcss) vs. number of clusters, between 5 to 6 clusters would be sufficient for this clustering problem. The following plot shows different clusters using a distinct color. <br>
<img src='https://github.com/kaveh7293/Olympic-Data-Analysis/blob/main/Picture1.png' width='1000' height='400'><br>

<li>To better understand which important features have important influence on differntiation of clusters, I plotted the p-loading plots. P-loading plots gives the relationship between direction of principal components and the direction of other features. The important features are located along the principal components. The corresponding plots are shown below. The important information can be extracted from these loading plots are:
<ol>
 <li> Temperature is an important feature which have a very important effect on differentiation of these clusters.</li>
 <li> Temperature and appearance in the olympics are negatively correlated (temperature is at the upper left corner and appearance is in the lower right corner of the P2 vs. P1 plot). As a result, countries with hotter climates have less appearances in the olympic.</li>
 <li> The GDP and the gold medals in the summer olympics are highly correlated. However, the gold medals in the winter olympics and GDP are on the negative and positive sides of P2 plot. Note that only 12% variation is explained by the second principal component. As a result, we cannot conclude that the poor countries mostly won the winter gold medals.</li></ol>
 <li> Since 72% of the variations are explained by the first principal component, the most of differentiations in the clusters are because of the features that are located on the negative side and positive side of the P1 axis.</li>
    

<img src='https://github.com/kaveh7293/Olympic-Data-Analysis/blob/main/loadin_p1_p2.png' width='2000' height='1000'></ol><br>

<p> The flowing results can be concluded based on loading plot and clustering analysis:
 <ol>
 <li> The <strong> black cluster </strong> has one member (i.e. US). Based on the loading plot, this country has <strong> high GDP</strong> and <strong> low temperature </strong>.</li> 
<li> The <strong> red cluster </strong> has two members (i.e., Russia and Germany). Based on the loading plot, this country has <strong> average to high GDP</strong> and <strong> low temperature </strong>.</li> 
<li> The <strong> yellow cluster </strong> members  had <strong> relatively good performance in the winter olympics </strong>, have <strong> low average temperatures </strong>, and have <strong> average to low average GDP</strong>. The countries in this cluster are Australia, Austria, Canada, China, Finland, France,
Hungary, Italy, Japan, Netherlands, Norway, Sweden, and
       Switzerland.</li> 

<li> The <strong> green cluster </strong> members  had <strong> relatively bad performance in the previous olympics </strong>, and have <strong> average temperatures </strong>. The countries in this cluster are Argentina, Belgium, Brazil, Bulgaria, Chile, Denmark, Estonia, Greece, Iceland, India, Iran, Ireland, South Korea, Latvia, Lebanon, Liechtenstein, Luxembourg, Mexico, Mongolia, New Zealand, Poland, Portugal, Romania, Spain, and Turkey.</li> 
<li> The <strong> blue cluster </strong> members  had <strong> relatively bad performance in the previous olympics </strong>,  have <strong> high temperatures </strong>, and a <strong> relatively low average GDP </strong>. The countries in this cluster are Afghanistan, Algeria, Armenia, Azerbaijan, Bahamas, Bahrain, Barbados, Belarus, Botswana, Burkina Faso, Burundi, Cameroon, Colombia, Costa Rica, Ivory Coast, Croatia, Cuba, Cyprus, Czech Republic, Djibouti, Dominican Republic, Ecuador, Egypt, Eritrea, Ethiopia, Fiji, Gabon, Georgia, Ghana, Grenada, Guatemala, Guyana, Haiti, Hong Kong, Indonesia, Iraq, Israel, Jamaica, Jordan, Kazakhstan, Kenya, Kuwait, Kyrgyzstan, Lithuania, Malaysia, Mauritius, Moldova, Montenegro, Morocco, Mozambique, Namibia, Niger, Nigeria, Pakistan, Panama, Paraguay, Peru, Philippines, Qatar, San Marino, Saudi Arabia, Samoa, Senegal, Serbia, Singapore, Slovakia, Slovenia, South Africa, Sri Lanka, Sudan, Suriname, Syria, Tajikistan, Tanzania, Thailand, Togo, Tonga, Trinidad and Tobago, Tunisia, Turkmenistan, Uganda, Ukraine, United Arab Emirates, Uruguay, Uzbekistan, Venezuela, Vietnam, Zambia, and Zimbabwe</li> 

  
  
  
 </ol>
 
 
 </p>

  

OUR WEB APPLICATION:  https://huntersfromnasa.co/


PROBLEM: Worlds Population is increasing , going to be 9 billion soon. No of people to feed is increasing. On the other hand, there is famine or starvation in the world with todays 7 billion population. UN plans 17 SDGs. 1st is FOOD i.e. to reduce famine. While due to current COVID-19 situation, food production, distribution ,etc has been severely affected. If such worldwide lockdown situation has to be elongate, there will be severe food scarcity in the world.

Middle Eastern, Medditerinean and esp fertile land of Indo Pak South Asian Region is more severely affected during this time. Locust ( an insect)  has returned in 27 years. It is destroying all the crops of people in that region. Due to COVID-19 fear and lockdown situation people haven't been able apply effective means/methods to get rid of them. For eg, some farmers in Pakistan started killing them manually and feeding them to their Poultry. It is massively supported and promoted by government. But, not much effective progress has been achieved. It is not the permanent solution. Locust are spreading very rapidly in those areas.


SOLUTION: We thought if we could track the movement/migration of Locust , and work according to those statistics, much effective measures can be acheived in controlling them. We study their suitable habitat comparing it to different factors like rainfall, temperature, soil moisture, green vegetation,etc and predict their next potential habitat.

We use Imageprocessing and some modern Machine Learning, Neural Networks , etc technique for data analysis for this prediction. We use those Image data and other data from NASA, MODIS, RAMSES, etc. 


ABSTRACT:

Desert locusts (Schistocerca gregaria) represent a major threat for agro-pastoral
resources and food security over almost 30 million km2
from northern Africa to the Arabian
peninsula and India. Given the differential food preferences of this insect pest and the extent
and remoteness of the their distribution area, near-real-time remotely-sensed information
on potential habitats support control operations by narrowing down field surveys to areas
favorable for their development and prone to gregarization and outbreaks. The development
of dynamic greenness maps, which detect the onset of photosynthetic vegetation, allowed
national control centers to identify potential habitats to survey, as locusts prefer green
and fresh vegetation. Their successful integration into the daily control operations led to
a new need: the near-real-time identification of the onset of dryness, a synonym for the
loss of habitat attractiveness, likely to be abandoned by locusts. The timely availability of
this information would enable control centers to focus their surveys on areas more prone
to gregarization, leading to more efficiency in the allocation of resources and in decision
making.
In this context, this work developed an original method to detect in near-real-time the onset of 
vegetation senescence. The design of the detection relies on the temporal
behavior of two indices: the Normalized Difference Vegetation Index, depending on the
green vegetation, and the Normalized Difference Tillage Index, sensitive to both green
and dry vegetation. The method is demonstrated in Mauritania, an ever-affected country,
with 10-day MODIS mean composites for the years 2010 and 2011. The discrimination
performance of three classes (“growth”, “density reduction” and “drying”) were analyzed for
three classification methods: maximum likelihood (61.4% of overall accuracy), decision tree
(71.5%) and support vector machine (72.3%). The classification accuracy is heterogeneous
in both time and space and is affected by several factors, such as vegetation density, the
north-south climatic gradient and the relief. Smoothing the vegetation time series resulted
in an increase of the overall accuracy of about 5% at the expense of a loss in timeliness of
ten days. To simulate near-real-time monitoring conditions, the decision tree was applied to
the decade of 2010. Overall, the seasonal vegetation cycle appeared clear and consistent.
The results obtained pave the way for an operational implementation of the senescence
dynamic mapping and, consequently, to further strengthen the capacity of the locust
control management.

METHODS USED BY MODIS:
1. Support Vector Machine (72.3% Accuracy)
2. Decision Tree (71.5%)

OUR IDEA( Methods We used):
1. Neural Network/Backpropagation Algorithm(Around 96.7%):
We propose to use previous data from MODIS and train them, and use the model for other untrained data ( and check with result). We kept factors like temperature, rainfall,soil moisture, vegetation, wind direction, etc as input and Green vs  Dry(Brown) coloring as output.
2. Principal Component Representation (Mapping Visualization)(Around 96.7%):
We reduced above multidimensional or multifactor(temp, rainfall, etc ) plot into simple PCA plot.


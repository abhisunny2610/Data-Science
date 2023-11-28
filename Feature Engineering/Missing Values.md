# Missing Data
---
Dealing with missing data is a common and inherent issue in data collection, especially when working with large datasets. There are various reasons for missing data, such as incomplete information provided by participants, non-response from those who decline to share information, poorly designed surveys, or removal of data for confidentiality reasons.


# Types of missing data
---
1. Missng completely at random (MCAR)
2. Missing at random (MAR)
3. Missing not at random (MNAR)

## Missing Completely at random (MCAR)
---
When data are missing completely at random (MCAR), the probability of any particular value being missing from your dataset is unrealted to anything else. \
The missing values are randomly distributed, so they can come from anywhere in the whole distribution of your values. These MCAR data are also unrealted to other unobserved variables.

`Example: Imagine providing a child with Lego of different colors to build a house. Each Lego represents a piece of information, like shape and color. The child might lose some Legos during the game. These lost legos represent missing information, just like when they can’t remember the shape or the color of the Lego they had. That information was lost randomly, but they do not change the information the child has on the other Legos`


## Missing at random (MAR)
---
Data missing at random (MAR) are not actually missing at random; this term is a bit of a misnomer.

This type of missing data systematically differs from the data you’ve collected, but it can be fully accounted for by other observed variables.

The likelihood of a data point being missing is related to another observed variable but not to the specific value of that data point itself.

## Missing not at random (MNAR)
---
MNAR is considered to be the most difficult scenario among the three types of missing data. It is applied when neither MAR nor MCAR apply. In this situation, the probability of being missing is completely different for different values of the same variable, and these reasons can be unknown to us. 

`An example of MNAR is a survey about married couples. Couples with a bad relationship might not want to answer certain questions as they might feel embarrassed to do so.`


## Methods for identifying missing data
|Function|Descriptions|
|------|-------|
|.isnull()|This function returns a pandas dataframe, where each value is a boolean value True if the value is missing, False otherwise.|
|.notnull()|Similarly to the previous function, the values for this one are False if either NaN or None value is detected.|
|.info()|This function generates three main columns, including the “Non-Null Count” which shows the number of non-missing values for each column.|
|.isna()|This one is similar to isnull and notnull. However it shows True only when the missing value is NaN type.|
